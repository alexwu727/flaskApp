# CONTRIBUTING

## How to run the Dockerfile locally

```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run"
```

## How to run the worker
```
docker run -w /app flask sh -c "rq worker -u REDIS_URL emails"
```