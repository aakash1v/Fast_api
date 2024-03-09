from sqlalchemy import Column,Integer,String,Boolean ,TIMESTAMP ,text,ForeignKey
from sqlalchemy.orm import DeclarativeBase  ,relationship

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__= "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String(40),nullable=False)
    content = Column(String(60),nullable=False) 
    published = Column(Boolean,nullable=False,server_default=text('True'))
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")

class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String(40),unique=True,nullable=False)
    password  =Column(String(100),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class Vote(Base):
    __tablename__="votes"
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)    