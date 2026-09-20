import os
import sys
import uvicorn

# Add the project/src directory to the Python path so it can find your backend code
sys.path.append(os.path.join(os.path.dirname(__file__), "project", "src"))

from project.main import app

if __name__ == "__main__":
    # Hugging Face Spaces routes web traffic to port 7860
    uvicorn.run(app, host="0.0.0.0", port=7860)
