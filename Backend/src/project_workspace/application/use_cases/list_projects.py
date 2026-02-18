from project_workspace.domain.ports.project_repository_port import ProjectRepositoryPort

class ListProjectsUseCase:

    def __init__(self, repository: ProjectRepositoryPort):
        self.repository = repository
    
    def execute(self):
        return self.repository.get_all()