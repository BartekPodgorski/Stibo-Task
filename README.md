How to run app?

Prerequirments:
Docker, k8s on your machine

1. Clone repository to your local environment "git clone https://github.com/BartekPodgorski/Stibo-Task.git"
2. run "docker build -t fastappi-bartek ." to create an image with name fastappi-bartek
3. run "kubectl apply -f deployment.yaml" to run deployment with one pod
4. run "kubectl apply -f service.yaml" to make it accessible from internet
5. check localhost:80/docs in your webbrowser to check endpoint