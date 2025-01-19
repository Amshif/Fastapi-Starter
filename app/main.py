from fastapi import FastAPI,Depends
from app.routes.user import user
from app.routes.auth import auth
from app.middleware import log_request_middleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.middleware('http')(log_request_middleware)

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

app.include_router(user)
app.include_router(auth)