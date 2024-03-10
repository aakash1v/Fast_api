# python virtual environments..   --isolated environment..
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user,post,auth,votes
from .config import settings
from .database import engine
from .import models

# models.Base.metadata.create_all(bind=engine)  --to create table..
# origins =["https://www.google.com","https://www.youtube.com"]
origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)




@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}




