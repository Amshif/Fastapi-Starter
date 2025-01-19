from pydantic import BaseModel

class UserResponse(BaseModel):
    user_id: int
    tenant_id: int
    email: str
    role: str
