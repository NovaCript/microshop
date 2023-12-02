from microshop.shemas import CreateUser


def create_user(user_id: CreateUser):
    user = user_id.model_dump()
    return {
        "succes": True,
        "user": user
    }
