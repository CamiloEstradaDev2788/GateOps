from typing import List
from uuid import UUID
from src.project_workspace.domain.entities.project import Project
from src.project_workspace.domain.ports.project_repository_port import ProjectRepositoryPort

class InMemoryProjectRepository(ProjectRepositoryPort):

    def __init__(self):
        self._projects: List[Project] = []

    def save(self, project: Project) -> None:
        self._projects.append(project)

    def get_all(self) -> List[Project]:
        return self._projects
    
    def get_by_id(self, project_id: UUID) -> Project | None:
        for project in self._projects:
            if project.id == project_id:
                return project
        return None