from fastapi import FastAPI,Depends,HTTPException
from app.routes.user import user
from app.routes.auth import auth
from app.middleware import log_request_middleware
from app.exception_handler import http_exception_handler,general_exception_handler
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.middleware('http')(log_request_middleware)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

app.include_router(user)
app.include_router(auth)