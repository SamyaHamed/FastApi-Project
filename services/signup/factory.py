from app_enums.UserRole import UserRole
from services.signup.company_strategy import CompanySignUp
from services.signup.trainee_strategy import TraineeSignUp


class SignUpStrategyFactory:
    strategies = {UserRole.Trainee: TraineeSignUp, UserRole.Company: CompanySignUp}

    @classmethod
    def get_strategy(cls, role: UserRole):
        strategy_class = cls.strategies.get(role)
        if not strategy_class:
            raise ValueError(f"No strategy defined for role: {role}")

        return strategy_class()
