# Quote API on MicroK8s

A stateless REST API built with Flask that returns random quotes. Deployed on MicroK8s with full cloud-native features including auto-scaling, self-healing, and ingress routing.

## Tech Stack
- Python / Flask
- Docker
- MicroK8s (Kubernetes)
- NGINX Ingress
- Horizontal Pod Autoscaler (HPA)

## Project Structure
quote-api-microk8s/
├── app.py
├── Dockerfile
├── requirements.txt
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── hpa.yaml

## API Endpoints
- GET / — Returns a random quote
- GET /health — Health check endpoint

## Run Locally with Python
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py

Test it:
curl http://localhost:5000

## Run with Docker
docker build -t quote-api .
docker run -p 5000:5000 quote-api

## Deploy on MicroK8s

1. Enable required addons
microk8s enable dns registry ingress metrics-server

2. Build and push image to local registry
docker build -t localhost:32000/quote-api:latest .
docker push localhost:32000/quote-api:latest

3. Deploy everything
microk8s kubectl apply -f k8s/

4. Add quote.local to hosts file
echo "127.0.0.1 quote.local" | sudo tee -a /etc/hosts

5. Verify everything is running
microk8s kubectl get pods
microk8s kubectl get svc
microk8s kubectl get ingress
microk8s kubectl get hpa

## Demo Commands

Registry proof
curl http://localhost:32000/v2/quote-api/tags/list
microk8s kubectl describe deployment quote-api | grep Image

Traffic visualization
for i in {1..10}; do curl -s http://quote.local/; echo; done

Chaos test - open two terminals
Terminal 1: microk8s kubectl get pods -w
Terminal 2: microk8s kubectl delete pod <pod-name>
The deleted pod is automatically replaced by Kubernetes.

Scaling
microk8s kubectl scale deployment quote-api --replicas=5
microk8s kubectl get pods
microk8s kubectl scale deployment quote-api --replicas=3

## Kubernetes Features Demonstrated
- Multiple Replicas - 3 pods running by default
- Liveness Probe - restarts unhealthy containers automatically
- Readiness Probe - only sends traffic to pods that are ready
- Resource Limits - CPU and memory limits defined per pod
- HPA - auto scales between 2 and 5 replicas based on CPU usage
- Ingress - routes external traffic via quote.local
- Local Registry - image stored in private MicroK8s r

cat > ~/quote-api-microk8s/README.md << 'EOF'
# Quote API on MicroK8s

A stateless REST API built with Flask that returns random quotes. Deployed on MicroK8s with full cloud-native features including auto-scaling, self-healing, and ingress routing.

## Tech Stack
- Python / Flask
- Docker
- MicroK8s (Kubernetes)
- NGINX Ingress
- Horizontal Pod Autoscaler (HPA)

## Project Structure
quote-api-microk8s/
├── app.py
├── Dockerfile
├── requirements.txt
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── hpa.yaml

## API Endpoints
- GET / — Returns a random quote
- GET /health — Health check endpoint

## Run Locally with Python
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py

Test it:
curl http://localhost:5000

## Run with Docker
docker build -t quote-api .
docker run -p 5000:5000 quote-api

## Deploy on MicroK8s

1. Enable required addons
microk8s enable dns registry ingress metrics-server

2. Build and push image to local registry
docker build -t localhost:32000/quote-api:latest .
docker push localhost:32000/quote-api:latest

3. Deploy everything
microk8s kubectl apply -f k8s/

4. Add quote.local to hosts file
echo "127.0.0.1 quote.local" | sudo tee -a /etc/hosts

5. Verify everything is running
microk8s kubectl get pods
microk8s kubectl get svc
microk8s kubectl get ingress
microk8s kubectl get hpa

## Demo Commands

Registry proof
curl http://localhost:32000/v2/quote-api/tags/list
microk8s kubectl describe deployment quote-api | grep Image

Traffic visualization
for i in {1..10}; do curl -s http://quote.local/; echo; done

Chaos test - open two terminals
Terminal 1: microk8s kubectl get pods -w
Terminal 2: microk8s kubectl delete pod <pod-name>
The deleted pod is automatically replaced by Kubernetes.

Scaling
microk8s kubectl scale deployment quote-api --replicas=5
microk8s kubectl get pods
microk8s kubectl scale deployment quote-api --replicas=3

## Kubernetes Features Demonstrated
- Multiple Replicas - 3 pods running by default
- Liveness Probe - restarts unhealthy containers automatically
- Readiness Probe - only sends traffic to pods that are ready
- Resource Limits - CPU and memory limits defined per pod
- HPA - auto scales between 2 and 5 replicas based on CPU usage
- Ingress - routes external traffic via quote.local
- Local Registry - image stored in private MicroK8s registry
