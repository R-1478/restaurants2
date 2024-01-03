# restaurant.py
import sqlite3
from Customer import Customer

CONN = sqlite3.connect('data/restaurant.db')
cursor = CONN.cursor()

class Restaurant:
    def __init__(self, restaurant_name, price):
        self.id = None
        self.restaurant_name = restaurant_name
        self.price = price

    @classmethod
    def create_table(cls):
        cursor.execute('''CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_name TEXT NOT NULL,
            price INTEGER NOT NULL
        )''')
        CONN.commit()

    @classmethod
    def fanciest(cls):
        cursor.execute('''SELECT * FROM restaurants ORDER BY price DESC LIMIT 1''')
        result = cursor.fetchone()
        return cls(result[1], result[2])

    def all_reviews(self):
        cursor.execute('''SELECT * FROM reviews WHERE restaurant_id = ?''', (self.id,))
        reviews = cursor.fetchall()
        return [f'Review for {self.restaurant_name} by {Customer.find_by_id(review[4]).full_name()}: {review[1]} stars.' for review in reviews]
    
    def save(self):
        cursor.execute('''INSERT INTO restaurants (restaurant_name, price)
            VALUES (?,?)''', (self.restaurant_name, self.price))
        CONN.commit()
    

restaurant_instance1 = Restaurant("Chicken Inn", 45)

restaurant_instance1.save()

restaurant_instance2 = Restaurant("Pizza Hut", 20)

restaurant_instance2.save()

restaurant_instance3 = Restaurant("Pizza Mojo", 25)

restaurant_instance3.save()

