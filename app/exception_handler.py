from fastapi import  HTTPException, Request
from fastapi.responses import JSONResponse
from datetime import datetime




async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "code": exc.status_code,
            "message": exc.detail or "An error occurred",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "path": str(request.url.path),
        },
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "code": 500,
            "message": "Internal server error",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "path": str(request.url.path),
        },
    )