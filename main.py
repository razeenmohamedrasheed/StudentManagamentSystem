from fastapi import FastAPI
from college.routers import registration
import uvicorn

app = FastAPI()

app.include_router(registration.router)



@app.get('/')
def welcome():
    return "Welcome"




if __name__ == "__main__":
    uvicorn.run('main:app',port=8000,host="0.0.0.0")
