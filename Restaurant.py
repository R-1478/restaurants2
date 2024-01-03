from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///data/restaurant.db', echo=True)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Customer(first_name='{self.first_name}', last_name='{self.last_name}')>"

    reviews = relationship("Review", back_populates="customer")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    def __repr__(self):
        return f"<Review(star_rating={self.star_rating})>"

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Restaurant(restaurant_name='{self.restaurant_name}', price={self.price})>"

    reviews = relationship("Review", back_populates="restaurant")

    def save(self, session):
        session.add(self)
        session.commit()


# Create tables
Base.metadata.create_all(engine)

# Sample instances and saving them
Session = sessionmaker(bind=engine)
session = Session()

# Sample instances and saving them
Session = sessionmaker(bind=engine)
session = Session()

restaurant_instance1 = Restaurant(restaurant_name="Chicken Inn", price=45)
restaurant_instance1.save(session)

restaurant_instance2 = Restaurant(restaurant_name="Pizza Hut", price=20)
restaurant_instance2.save(session)

restaurant_instance3 = Restaurant(restaurant_name="Pizza Mojo", price=25)
restaurant_instance3.save(session)

session.close()  # Close the session when done
