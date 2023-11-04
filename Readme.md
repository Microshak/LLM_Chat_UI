
Steps
# Build
docker build -t chat .

## Run
docker run -it -p 5000:5000 chat



```

docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

gunicorn  --bind 0.0.0.0:5000 --workers=10 --threads=10 --timeout 2200  chat:app

```

# Docs
## Redis
* 0 db for web call chat
* 1 db for memory
* 2 db for image list


# Prompts Templates
https://madgicx.com/blog/chatgpt-prompts-for-marketing


# Login
LDAP
https://soshace.com/integrate-ldap-authentication-with-flask/


# Container
## Computer
To get docker to work with Nvidia you need to install the Nvidia container tool kit.
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html


More info
https://github.com/NVIDIA/nvidia-container-toolkit

## Build Run
```
sudo docker build -t work .
docker run --gpus all -it -t work

```


https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html#framework-matrix-2023


# TODO 

https://smith.langchain.com/hub/gitmaxd/synthetic-training-data/playground?organizationId=70e5b93e-41f9-5efa-a842-2e4db5e113ed
