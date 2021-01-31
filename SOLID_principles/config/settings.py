from environs import Env

env = Env()
env.read_env()  # Read .env file, if it exists

# required variables: your gmail credentials
auth_user = env('AUTH_USER')
auth_password = env('AUTH_PASSWORD')
