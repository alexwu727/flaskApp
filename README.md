# flaskApp

### How to build a docker image
`docker build -t <image tag> .`

### How to start a volumn with docker image
`docker run -dp 5005:5000 -w /app -v "$(pwd):/app" <image tag>`