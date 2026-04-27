from sqlalchemy.orm import Session
from database import engine
from models import User

db = Session(bind=engine)

user = db.query(User).filter(User.username == "admin").first()

db.delete(user)
db.commit()