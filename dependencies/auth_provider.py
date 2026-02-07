from fastapi import Depends
from services.auth_services import AuthService

from dependencies.repository_provider import (
    get_user_repository,
    get_trainee_repository,
    get_company_repository
)

from repositories.user_repository import UserRepository
from repositories.trainee_repository import TraineeRepository
from repositories.company_repository import CompanyRepository


def get_auth_service(
    user_repo: UserRepository = Depends(get_user_repository),
    trainee_repo: TraineeRepository = Depends(get_trainee_repository),
    company_repo: CompanyRepository = Depends(get_company_repository),
) -> AuthService:
    return AuthService(
        user_repo=user_repo,
        trainee_repo=trainee_repo,
        company_repo=company_repo,
    )
