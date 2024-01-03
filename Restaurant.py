from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from Review import Review

Base = declarative_base()
engine = create_engine('sqlite:///data/restaurant.db', echo=True)  # Use your preferred database URL

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Restaurant(restaurant_name='{self.restaurant_name}', price={self.price})>"

    @classmethod
    def create_table(cls):
        Base.metadata.create_all(engine)

    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self, session):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [f"Review for {self.restaurant_name} by {review.customer.full_name()}: {review.star_rating} stars." for review in reviews]

    def save(self, session):
        session.add(self)
        session.commit()

Base.metadata.create_all(engine)  # Create tables at the module level

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
