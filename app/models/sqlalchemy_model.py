# project/app/models/tortoise.py
import datetime

from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TextSummary(Base):
    __tablename__ = "textsummary"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    summary = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __str__(self):
        return self.url


if __name__ == "__main__":
    print("File two executed when ran directly")
else:
    print("File two executed when imported")
