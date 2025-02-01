from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.tenant import TenantResponse
from app.models.tenant import read_tenant
from app.config.database import get_db


tenant = APIRouter()


@tenant.get("/{tenant_id}", response_model=TenantResponse)
def get_user(tenant_id: int, db: Session = Depends(get_db)):

    tenant = read_tenant(tenant_id, db)

    if not tenant:
        raise HTTPException(status_code=404, detail="User not found")
    return tenant
