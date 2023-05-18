#!/bin/bash
docker stop bot
docker rm bot
docker rmi -f $(docker images -q) 
docker build -t bot-shopify .
docker run --name bot -p 4444:4444 -p 5900:5900 --shm-size=2g --restart=always -d -it bot-shopify
sleep 5
# docker exec -it bot bash -c "while true; do /usr/bin/python3 /app/shop.py; sleep 3600; done" 
# docker exec -d bot bash -c "while true; do /usr/bin/python3 /app/shop.py >> /app/shop.log 2>&1; sleep 3600; done"
