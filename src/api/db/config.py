from decouple import config as env_config

DATABASE_URL = env_config("DATABASE_URL", default="")
