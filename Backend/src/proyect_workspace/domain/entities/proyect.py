from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

@dataclass
class Proyect:
    id: UUID
    name: str
    repository_url: str
    created_at: datetime