# Kubernetes Packet Simulator

This project simulates 5G-style packet traffic using a containerized Flask web service deployed on Kubernetes. It demonstrates core DevOps concepts including containerization, service exposure via NodePort, and parallel traffic simulation.

## Features

- Python Flask service that receives and logs incoming packet data
- Kubernetes Deployment and NodePort Service configuration
- Bash script for generating high-volume packet traffic using concurrent curl requests
- Designed for use in local Kubernetes environments such as Minikube or Docker Desktop

## Technologies Used

- Docker
- Kubernetes
- Flask (Python)
- Bash scripting
