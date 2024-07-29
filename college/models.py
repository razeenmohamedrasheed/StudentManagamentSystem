from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from college.database import Base

# Define the model for the 'usertype' table
class UserType(Base):
    __tablename__ = 'usertype'

    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String, unique=True, index=True)

    users = relationship("UserData", back_populates="usertype")

# Define the model for the 'userdata' table
class UserData(Base):
    __tablename__ = 'userdata'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    contact = Column(String)
    password = Column(String)
    usertype_id = Column(Integer, ForeignKey('usertype.id'))

    usertype = relationship("UserType", back_populates="users")
