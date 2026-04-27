from database import engine
from models import Base, User
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

db = Session(bind=engine)

admin = User(username="admin", password="admin123")
operator = User(username="operator", password="admin123")

db.add(admin)
db.add(operator)

db.commit()

print("user added")