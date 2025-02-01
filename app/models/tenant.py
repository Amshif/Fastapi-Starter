from sqlalchemy import Column, Integer, String, ForeignKey,BigInteger,TIMESTAMP,func
from app.config.database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    tenant_id = Column(BigInteger, primary_key=True, autoincrement=True)
    tenant_name = Column(String(255), nullable=False)
    tenant_domain = Column(String(255), unique=True)
    plan_type = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())



def read_tenant(tenant_id, db):
    return db.query(Tenant).filter(Tenant.tenant_id == tenant_id).first()