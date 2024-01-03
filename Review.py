# review.py
import sqlite3

CONN = sqlite3.connect('data/reviews.db')
cursor = CONN.cursor()

class Review:
    def __init__(self, star_rating, review):
        self.id = None
        self.star_rating = star_rating
        self.review = review
        self.restaurant = None  # Added to establish relationship
        self.customer = None  # Added to establish relationship

    @classmethod
    def create_table(cls):
        cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            star_rating INTEGER NOT NULL,
            review TEXT NOT NULL,
            restaurant_id INTEGER,
            customer_id INTEGER,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )''')
        CONN.commit()

    def save(self):
        cursor.execute('''INSERT INTO reviews (star_rating, review, restaurant_id, customer_id)
            VALUES (?, ?, ?, ?)''', (self.star_rating, self.review, self.restaurant, self.customer))
        CONN.commit()

    def full_review(self):
        return f'Review for {self.restaurant.restaurant_name} by {self.customer.full_name()}: {self.star_rating} stars.'

Review.create_table()
review_instance = Review(4, "Great place!")
review_instance.save()

review_instance2 = Review(5, "Great place!")
review_instance2.save()

