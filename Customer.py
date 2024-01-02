# customer.py
import sqlite3
CONN = sqlite3.connect('data/customer.db')
cursor = CONN.cursor()

class Customer:
    def __init__(self, first_name, last_name):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []  # Removed default value
        self.restaurants = []  # Removed default value

    @classmethod
    def create_table(cls):
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )''')
        CONN.commit()

    def save(self):
        cursor.execute('''INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)''', (self.first_name, self.last_name))
        CONN.commit()

    @classmethod
    def delete(cls):
        cursor.execute('''DELETE FROM customers WHERE id = ?''', (cls.id,))
        CONN.commit()

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def favorite_restaurant(self):
        for review in self.reviews:
            if review.star_rating == 5:
                return review.restaurant
        return None
    
    
#   

customer_instance = Customer("John", "Doe")

customer_instance.save()



