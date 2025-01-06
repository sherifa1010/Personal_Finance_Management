# Personal_Finance_Management
# Final Project - Backend Development

# PERSONAL FINANCE MANAGEMENT

# AUTHORS
.SHERIFATU ABDUL RAZAK

.AMINA MOHAMMED RABIU

# TABLE OF CONTENTS
1.Project Description

2.Features

3.startup and installation

# Project Description
PERSONAL FINANCE MANAGEMENT is the practice of effectively planning and managing your financial resources to achieve your life goals. It involves understanding your income, expenses, savings, and investments to make informed decisions about how
to allocate your money wisely.

# FEATURES
 1.Budgeting and Expense Tracking; Helps you allocate income toward expenses, savings, and investments.
 
 2.Income Management;Users can add, update, and delete income records based on specific criteria (e.g., source or date).
   It also identify increase earnings in career growth.
   
 3.Technology Integration; Offers real-time tracking and budgeting.
 
 4.Risk Management; Recommends appropriate insurance coverage like;health, life, property, etc.
 
 5.Financial Literacy; Builds awareness of financial concepts to make informed decisions.

 # Setup and Installation
 1.Prerequisites
 
  .Python 3
  
  .MySQL
  
  .Virtual Environment

  # Installation steps
 1.clone the repository
    git clone https://github.com/sherifa1010/Personal_Finance_Management.git
    
 2.move to te clone directory
    cd PERSONAL_FINANCE_MANAGEMENT
    
 3.create a virtual environment and activate it
    sudo apt install python3-venv
    python -m venv ~/myenv
    source ~/myenv/bin/activate
    
 4.Install dependencies:
    pip install mysql-connector-python sqlachemy flask flask-login
    
 5.Setup the database
    configure the database connection in config/config.py
    
 6.Initialize the database
    python3 models.py
    
 7.Run  the Flask  application
   export FLASK_APP=app
   export FLASK_DEBUG=1
   flask run
   
 8.open your browser and navigate
   http://127.0.0.1:5000


