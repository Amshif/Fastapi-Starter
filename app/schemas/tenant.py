from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TenantResponse(BaseModel):
   
    tenant_id: int
    tenant_name: str
    tenant_domain: Optional[str]
    plan_type: str
    created_at: datetime
