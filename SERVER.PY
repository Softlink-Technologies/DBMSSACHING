import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Insert a new record into the database
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

# Commit the changes to the database
mydb.commit()

# Select records from the database
mycursor.execute("SELECT * FROM customers")

# Fetch all records and print them
result = mycursor.fetchall()
for row in result:
  print(row)
