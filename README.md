# This project contains an exercise for Docker and K8s.

### Tasks:
- create a Dockerfile that sets up an nginx server based on Alpine Linux, includes an index.html in JS that tells the date and runs as a non-root user - WORKS
- build an image and push it to Docker Hub - WORKS
- deployment code to deploy the image to K8s - Works locally, access from the net is not configured
- create a script to test that the container works - STILL IN PROGRESS
------------------
### Requirements:
- Python 3.6 ++
    - the script is written based on several tutorials. here is [one of them](https://theautomatic.net/2019/01/19/scraping-data-from-javascript-webpage-python/)
    - more info about what [requests-html module](https://pypi.org/project/requests-html/) does
- Docker 
    - full information on how to install docker depending on your distribution is in the [docker documentation](https://docs.docker.com/engine/install/)
    - how to run nginx image with [non-root privileges](https://harsimran-kaur.medium.com/run-nginx-as-unprivileged-user-in-docker-container-on-kubernetes-6e71564cf78b). PAY ATTENTION TO PORTS!!
- Minikube
    - installation instruction for [minikube and kubectl](https://kubernetes.io/docs/tutorials/hello-minikube/)
    - this will automaticaly configure kubectl
    - ingress addon enabled - `minikube addons enable ingress`
    - basic info about what is K8s and how not to loose your head is on [Tech World with Nana](https://www.youtube.com/watch?v=VnvRFRk_51k&list=PLy7NrYWoggjziYQIDorlXjTvvwweTYoNC)
 
-------------------
### HOW TO USE THIS PROJECT:
- clone the project from the repository
- build the docker image (pay attention to the dot at the end!!)
    - `docker build -t droritzz/alpinex:1.13 .`
- deploy the image to k8s
    - `kubectl apply -f deployment.yaml`
    - enter the dashboard to see the pod  `minikube dashboard`

### NOT FINISHED:
- the pod is deployed, the container is running, however there is no connection to the container.
- write and run testing.py script
    - `python3 testing.py`




