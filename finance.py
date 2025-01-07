from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime

# Initialize Flask extensions
finance = Flask(__name__)
finance.secret_key = 'supersecretkey'  # Secret key for session management
bcrypt = Bcrypt(finance)     
login_manager = LoginManager(finance)
login_manager.login_view = "login"  # Redirect to login if not authenticated

# In-memory data storage (In a real-world app, use a database)
users = []  # The User class is used to represent a user in the system.

expenses = [
    {"food": "Jollof", "bill": 50, "category": "food", "date": "2024-06-01"},
    {"food": "Rice", "bill": 30, "category": "food", "date": "2024-06-02"},
    {"food": "Pizza", "bill": 100, "category": "food", "date": "2024-06-10"},
    {"rent": "Single room", "bill": 2000, "category": "rent", "date": "2024-06-01"},
    {"entertainment": "Netflix", "bill": 30, "category": "entertainment", "date": "2024-06-01"},
]

incomes = [
    {"id": 234575, "username": 'amayakubu', "source": 'salary', "date": "2024-06-01", "amount": 300},
    {"id": 897655, "username": 'kojoabina', "source": 'business', "date": "2024-04-06", "amount": 500},
    {"id": 178654, "username": 'fifisalam', "source": 'investment return', "date": "2024-08-03", "amount": 500},
]

# User model for Flask-Login 
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Load user from 'users' list based on user ID, 
@login_manager.user_loader
def load_user(user_id):  #The load_user function helps Flask-Login identify the logged-in user.
    return next((user for user in users if user.id == int(user_id)), None)

# Home route
@finance.route("/")
@login_required
def home():
    return render_template("index.html")

# Register new user
@finance.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(id=len(users) + 1, username=username, password=hashed_password)
        users.append(user)
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("login"))
    
    return render_template("register.html")

#We use login_user() to log in a user, and logout_user() to log them out.
# Login route
@finance.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = next((u for u in users if u.username == username), None)
        if user and bcrypt.check_password_hash(user.password, password):  #The passwords are hashed using Flask-Bcrypt to ensure security.
            login_user(user)
            return redirect(url_for("home"))
        
        flash("Invalid username or password", "danger")

    return render_template("login.html")

# Logout route
@finance.route("/logout")
@login_required  #The login_required decorator is used to protect routes that should only be accessible by authenticated users.
def logout():
    logout_user()
    return redirect(url_for("login"))


# Get all expenses
@finance.route("/expenses", methods=["GET"])
@login_required
def get_all_expenses():
    return jsonify(expenses), 200

# Get all income
@finance.route("/incomes", methods=["GET"])
@login_required
def get_all_incomes():
    return jsonify(incomes), 200

# Get expense by bill
@finance.route("/expenses/<int:bill>", methods=["GET"])
def get_expense_by_bill(bill):
    for expense in expenses:
        if expense.get("bill") == bill:
            return jsonify(expense), 200
    return jsonify({"error": "Expense not found"}), 404

# Update expense by bill
@finance.route("/expenses/<int:bill>", methods=["PATCH"])
def update_expense_by_bill(bill):
    updation_data = request.get_json()
    for expense in expenses:
        if expense.get("bill") == bill:
            expense.update(updation_data)  # Updates only the passed keys
            return jsonify(expense), 200
    return jsonify({"error": "Expense not found"}), 404

# Validate expense data
def validate_expense_data(data):
    # Check if required fields are present
    required_keys = ["bill", "category", "date"]
    for key in required_keys:
        if key not in data:
            return jsonify({"error": f"'{key}' is required"}), 400

    # Check if 'bill' is a number
    if not isinstance(data.get("bill"), (int, float)):
        return jsonify({"error": "'bill' must be a number"}), 400

    # Check if 'category' is a valid category (you can expand this with more categories if needed)
    valid_categories = ["food", "rent", "entertainment"]
    if data.get("category") not in valid_categories:
        return jsonify({"error": f"Invalid category. Valid categories are: {', '.join(valid_categories)}"}), 400

    # Check if the 'date' is in correct format
    try:
        datetime.strptime(data.get("date"), "%Y-%m-%d")  # Check if the date format is YYYY-MM-DD
    except ValueError:
        return jsonify({"error": "'date' must be in the format YYYY-MM-DD"}), 400

    return None  # Return None if validation is successful

# Add a new expense
@finance.route("/expenses", methods=["POST"])
def add_expense():
    new_expense = request.get_json()

    # Validate the expense data
    validation_error = validate_expense_data(new_expense)
    if validation_error:
        return validation_error

    expenses.append(new_expense)
    return jsonify({"message": "New expense added", "expense": new_expense}), 201

# Add a new income
@finance.route("/incomes", methods=["POST"])
def add_income():
    new_income = request.get_json()
    incomes.append(new_income)
    return jsonify({"message": "New income added", "income": new_income}), 201

# Update income by source
@finance.route("/incomes/<string:source>", methods=["PATCH"])
def update_income_by_source(source):
    updation_data = request.get_json()
    for income in incomes:
        if income.get("source") == source:
            income.update(updation_data)
            return jsonify(income), 200
    return jsonify({"error": "Income not found"}), 404

# Delete expense by category
@finance.route("/expenses/<string:category>", methods=["DELETE"])
def delete_expense_by_category(category):
    for expense in expenses:
        if expense.get("category") == category:
            expenses.remove(expense)
            return jsonify({"message": f"Expense with category '{category}' has been deleted"}), 200
    return jsonify({"error": "Expense not found"}), 404

# Delete income by date
@finance.route("/incomes/<string:date>", methods=["DELETE"])
def delete_income_by_date(date):
    for income in incomes:
        if income.get("date") == date:
            incomes.remove(income)
            return jsonify({"message": f"Income with date '{date}' has been deleted"}), 200
    return jsonify({"error": "Income not found"}), 404


# Monthly summary
@finance.route("/expenses/summary/<int:year>/<int:month>", methods=['GET'])
@login_required
def get_monthly_summary(year, month):
    total_expenses = 0
    expenses_by_category = {}

    # Loop through the expenses list and filter by the year and month
    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        if expense_date.year == year and expense_date.month == month:
            total_expenses += expense["bill"]
            category = expense["category"]
            if category not in expenses_by_category:
                expenses_by_category[category] = 0
            expenses_by_category[category] += expense["bill"]
    
    return jsonify({
        "total_expenses": total_expenses,
        "expenses_by_category": expenses_by_category
    }), 200


if __name__ == "__main__":
    finance.run(debug=True, port=5003)
