# main_script.py

from Customer import Customer
from Review import Review
from Restaurant import Restaurant

# Create tables
Customer.create_table()
Review.create_table()
Restaurant.create_table()

# Create instances and save data
customer_instance = Customer("John", "Doe")
customer_instance.save()

# Repeat the same for Review and Restaurant instances
