from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///data/review.db")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=False)
    review = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  # Correct foreign key relationship
    customer_id = Column(Integer, ForeignKey('customers.id'))  # Correct foreign key relationship

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def __repr__(self):
        return f"<Review(star_rating={self.star_rating}, review='{self.review}')>"

# Move the session and sample instances inside a function
def main():
    from Restaurant import Restaurant
    from Customer import Customer

    # Create tables before using them
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Sample instances and saving them
    # Assuming restaurant_instance1 and customer_instance are already created

    review_instance = Review(star_rating=4, review="Great place!")
    review_instance.restaurant = session.query(Restaurant).filter_by(restaurant_name="Chicken Inn").first()
    review_instance.customer = session.query(Customer).filter_by(first_name="John", last_name="Doe").first()
    session.add(review_instance)
    session.commit()

    # Assuming restaurant_instance2 and customer_instance2 are already created
    review_instance2 = Review(star_rating=5, review="Great place!")
    review_instance2.restaurant = session.query(Restaurant).filter_by(restaurant_name="Pizza Hut").first()
    review_instance2.customer = session.query(Customer).filter_by(first_name="Jane", last_name="Doe").first()
    session.add(review_instance2)
    session.commit()

    session.close()  # Close the session when done

if __name__ == "__main__":
    main()
