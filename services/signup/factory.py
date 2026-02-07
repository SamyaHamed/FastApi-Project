from services.signup.company_strategy import CompanySignUp
from services.signup.trainee_strategy import TraineeSignUp
from app_enums.UserRole import UserRole

class SignUpStrategyFactory :
        strategies = {
                UserRole.Trainee : TraineeSignUp,
                UserRole.Company : CompanySignUp
        }

        """@classmethod
        def get_strategy(cls, role : UserRole):
                strategy_class = cls.strategies.get(role)
                if not strategy_class:
                    raise ValueError(f"No strategy defined for role: {role}")

                return strategy_class()"""
        @staticmethod
        def get_strategy(
                role: UserRole,
                user_repo,
                trainee_repo=None,
                company_repo=None
        ):
                if role == UserRole.Trainee:
                        return TraineeSignUp(user_repo, trainee_repo)

                elif role == UserRole.Company:
                        return CompanySignUp(user_repo, company_repo)

                raise ValueError(f"No strategy defined for role: {role}")