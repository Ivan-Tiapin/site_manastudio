# Initialise environment variables
import environ
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))
print(env('ALLOWED_HOSTS').split(','))
