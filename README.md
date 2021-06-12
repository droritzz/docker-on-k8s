# This project contains an exercise for Docker and K8s.

### Tasks:
- create a Dockerfile that sets up an nginx server based on Alpine Linux and includes an index.html in JS that tells the date - WORKS
- build an image and push it to Docker Hub - WORKS
- deployment code to deploy the image to K8s - WORKS 
- create a script to test that the container works - STILL IN PROGRESS
------------------
### Requirements:
- Python 3.6 ++
- Docker 
    - full information on how to install docker depending on your distribution is in the [docker documentation](https://docs.docker.com/engine/install/)
- Minikube
    - installation instruction for [minikube and kubectl](https://kubernetes.io/docs/tutorials/hello-minikube/)
    - this will automaticaly configure kubectl
    - ingress addon enabled
    - basic info about what is K8s and how not to loose your head is on [Tech World with Nana](https://www.youtube.com/watch?v=VnvRFRk_51k&list=PLy7NrYWoggjziYQIDorlXjTvvwweTYoNC)
 
-------------------
### HOW TO USE THIS PROJECT:
- clone the project from the repository
- build the docker image (pay attention to the dot at the end!!)
    - `docker build -t droritzz/alpinex:1.9 .`
- deploy the image to k8s
    - `kubectl apply -f deployment.yaml`
    - enter the dashboard to see the pod  `minikube dashboard`

### NOT FINISHED:
- the pod is deployed, the container is running, however there is no connection to the container other than via the terminal
- write and run testing.py script, according to this [tutorial](https://theautomatic.net/2019/01/19/scraping-data-from-javascript-webpage-python/)
    - `python3 testing.py`




