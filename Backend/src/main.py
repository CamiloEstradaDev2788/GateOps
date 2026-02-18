from fastapi import FastAPI
from pydantic import BaseModel
from src.project_workspace.application.use_cases.create_project import CreateProjectUseCase
from src.project_workspace.application.use_cases.list_projects import ListProjectsUseCase
from src.project_workspace.Infrastructure.repositories.in_memory_project_repository import InMemoryProjectRepository

app = FastAPI()

repository = InMemoryProjectRepository()

create_project_use_case = CreateProjectUseCase(repository)
list_projects_use_case = ListProjectsUseCase(repository)


class CreateProjectRequest(BaseModel):
    name:str
    repository_url: str


@app.post("/projects")
def create_project(request: CreateProjectRequest):
    return create_project_use_case.execute(
        name = request.name,
        repository_url = request.repository_url
    )


@app.get("/projects")
def list_projects():
    return list_projects_use_case.execute()