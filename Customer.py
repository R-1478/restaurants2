from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///data/customer.db', echo=True)  # Use your preferred database URL

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Customer(first_name='{self.first_name}', last_name='{self.last_name}')>"

    @classmethod
    def create_table(cls):
        Base.metadata.create_all(engine)

    def save(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def delete(cls, session):
        session.delete(cls)
        session.commit()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, session):
        for review in self.reviews:
            if review.star_rating == 5:
                return review.restaurant
        return None

Base.metadata.create_all(engine)  # Create tables at the module level

# Sample instances and saving them
Session = sessionmaker(bind=engine)
session = Session()

customer_instance = Customer(first_name="John", last_name="Doe")
customer_instance.save(session)

customer_instance2 = Customer(first_name="Jane", last_name="Doe")
customer_instance2.save(session)

customer_instance3 = Customer(first_name="Jose", last_name="Gusto")
customer_instance3.save(session)

session.close()  # Close the session when done
