from uuid import uuid4
from datetime import datetime
from project_workspace.domain.entities.project import Project
from project_workspace.domain.ports.project_repository_port import ProjectRepositoryPort

class CreateProjectUseCase:

    def __init__(self, repository: ProjectRepositoryPort):
        self.repository = repository
    
    def execute(self, name: str, repository_url: str) -> Project:

        project = Project(
            id = uuid4(),
            name = name,
            repository_url=repository_url,
            created_at=datetime.utcnow()
        )

        self.repository.save(project)
        return project