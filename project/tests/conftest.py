import os
from pathlib import Path
from dotenv import load_dotenv

# Load the .env file located at the root (Enviromental Resercher/.env)
root_dir = Path(__file__).resolve().parent.parent.parent
env_path = root_dir / ".env"

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
