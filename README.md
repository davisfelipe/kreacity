# Kreacity Project

## Run Project as Docker
Before run project, create `.env` file for the environment variables
```dotenv
HOST=0.0.0.0
PORT=5000
MONGO_URI=mongodb://kreacity_user:kreacity_pass@mongo:27017/kreacity_db?authSource=kreacity_db
JWT_TOKEN=kreacity_token
```
by default, docker compose will create 3 containers with the next command
```shell
docker-compose up
```
verify if you have the ports 80, 27017 are enabled, if you any port busy, you can change in the file docker-compose in
the nginx service or the mongo service.
To stop all services you can set `ctrl+c` and set
```shell
docker-compose down
```

## Run python test
For run python test in local, you have to create a new virtual environment in your project
```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
after that, you can run python test as:
```shell
pytest --cov-report=html --cov=. --cov-config=.coveragerc
```