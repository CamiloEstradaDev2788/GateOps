from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from project_workspace.domain.entities.project import Project


class ProjectRepositoryPort(ABC):

    @abstractmethod
    def save(self, project: Project) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Project]:
        pass

    @abstractmethod
    def get_by_id(self, project_id: UUID) -> Project | None:
        pass
