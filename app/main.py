# python virtual environments..   --isolated environment..
from fastapi import FastAPI
import models
from database import engine
from routers import user,post,auth,votes
from config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)



@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}




