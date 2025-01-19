from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base

class User(Base):
    __tablename__ = "tenantusers"

    user_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(String, nullable=False)



def read_user(user_id, db):
    return db.query(User).filter(User.user_id == user_id).first()