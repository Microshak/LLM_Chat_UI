
Steps
# Build
docker build -t chat .

## Run
docker run -it -p 5000:5000 chat



```

docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

gunicorn  --bind 0.0.0.0:5000 --workers=10 --threads=10 --timeout 2200  app:app

```

# Docs
## Redis
* 0 db for web call chat
* 1 db for memory
