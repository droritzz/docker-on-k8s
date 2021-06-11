# This project contains an excersie for Docker and K8s.

### Tasks:
- create a Dockerfile that sets up an nginx server based on Alpine Linux and includes an index.html in JS that tells the date - WORKS
- build an image and push it to Docker Hub - WORKS
- deployment code to deploy the image to K8s - WORKS PARTIALLY
- create a script to test that the container works - STILL IN PROGRESS
------------------
### Requirements:
- Python 3.6 ++
- Docker 
    - full information on how to install docker depending on your distribution is in the [docker documentation](https://docs.docker.com/engine/install/)
- kubectl 
- Minikube
    - installation instruction for [minikube and kubectl](https://kubernetes.io/docs/tutorials/hello-minikube/)
    - basic info about what is K8s and how not to loose your head is on [Tech World with Nana](https://www.youtube.com/watch?v=VnvRFRk_51k&list=PLy7NrYWoggjziYQIDorlXjTvvwweTYoNC)
 
-------------------
### HOW TO USE THIS PROJECT:
- clone the project from the repository
- build the docker image (pay attention to the dot at the end!!)
    - `docker build -t droritzz/alpinex:1.9 .`
### NOT FINISHED:
- deploy the image to k8s
    - `kubectl create -f deployment.yaml`
- write and run testing.py script, according to this [tutorial](https://theautomatic.net/2019/01/19/scraping-data-from-javascript-webpage-python/)
    - `python3 testing.py`




