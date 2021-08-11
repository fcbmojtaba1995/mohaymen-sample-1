
# Mohaymen Sample Project 1

A sampele project for Mohaymen corp.\
The project create some initial files (csv) and store metadata files in Redis database (Hash type) and create again files (new) and store new files in Redis.

### Built With:

- Python 3.9.6
- Redis 6.2.5
- Docker
- Docker Compose
## Getting Started:

### Prerequisites:
- docker for download docker in [link](https://docs.docker.com/engine/install/)
- docker-compose for download docker in [link](https://docs.docker.com/compose/install/)
- STOP redis server in local
    ```bash
    sudo systemctl stop redis
    ```
- You need to create local_config.py file in the project root file with default values.

    ```bash
    REDIS_HOST = 'redis'
    REDIS _PORT = '6379'
    REDIS_DB = 0
    REDIS_PASSWORD = ''
    ```
### Run Service:
```bash
docker-compose up -d
```
## Authors

- [@fcbmojtaba1995](https://www.github.com/octokatherine)

  