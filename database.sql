CREATE DATABASE IF NOT EXISTS Finance;
SHOW DATABASES;
USE Finance;

CREATE TABLE IF NOT EXISTS Users(
    user_ID INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50), inique=True, nullable=False
    password VARCHAR(80), nullable=False
);


CREATE TABLE IF NOT EXISTS Income(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    source VARCHAR(50) nullable=False,
    user_ID VARCHAR(50) nullable=False,
    date VARCHAR(default=datetime.utcnow),
    amount DECIMAL(10, 2) nullable=False
);

CREATE TABLE IF NOT EXISTS Expenses(
    ID INT PRIMARY KEY=True,
    amount VARCHAR(50) nullable=False,
    source VARCHAR(50) nullabl=False
    date VARCHAR(default=datetime.utcnow) 
);

INSERT INTO Users( user_ID, username, password)
VALUES ( 234575,'amayakubu', , 3400 ),
       ( 897655, 'kojoabina', 5000 ),
       ( 178654, 'fifisalam', 3054),
       ( 987656, 'nanabeauty', 1001);

INSERT INTO Income( ID, source, user_ID, date, amount)
VALUES (234575,'amayakubu', 'salary', 01-06-2024, 300),
       (897655, 'kojoabina', 'business', 06-04-2024, 500),
       ( 178654, 'fifisalam', 'investment return', 03-08-2024, 500),
       ( 987656, 'nanabeauty', 'gift', 09-08-2024, 200);

INSERT INTO Expenses( ID, amount, source, date)
VALUES (234575, 40, 'salary', 20-06-2024),
       (897655, 20, 'business', 15-04-2024),
       (178654, 50, 'investment return', 20-08-2024)
       (987656, 10, 'gift', 15-08-2024);

SELECT * FROM Users;
SELECT * FROM Income;
SELECT * FROM Expenses;