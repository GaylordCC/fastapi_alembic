# Create the virtual enviroment
python -m venv venv

# Activate the virtual enviroment
source venv/bin/activate

# Python version of the project
python 3.12.1

# To install the requirements
pip install -r requirements.txt

# Run the fastapi uvicorn server
uvicorn fastapi_project.main:app --reload

# Open the Swagger UI documentation of the project
localhost:8000
localhost:8000/docs

# 
