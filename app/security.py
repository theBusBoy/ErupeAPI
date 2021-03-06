from os import getenv


class SecurityConfig:
    # YOU MUST SET A SECRET KEY ENVIRONMENT VARIABLE OR YOU ARE EXPOSING YOURSELF TO ATTACKS
    SECRET_KEY = getenv("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
