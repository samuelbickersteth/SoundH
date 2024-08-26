
# Python Web Application with Kubernetes and Prometheus Monitoring

This repository contains a simple Python web application that exposes a REST API and is containerized using Docker. The application is deployed to a Kubernetes cluster and monitored using Prometheus. Logging and custom metrics are also implemented.

## Table of Contents

* [Prerequisites](#prerequisites)
* [Build and Run the Docker Container Locally](#build-and-run-the-docker-container-locally)
* [Kubernetes Deployment](#kubernetes-deployment)
* [Setting Up and Accessing Prometheus](#setting-up-and-accessing-prometheus)
* [Assumptions](#assumptions)
* [Improvements](#improvements)
* [CI/CD Setup (Optional)](#cicd-setup-optional)

## Prerequisites

Before you begin, ensure you have the following installed:

* Docker
* Kubernetes (Minikube, MicroK8s, or any Kubernetes cluster)
* kubectl
* Terraform 

## Build and Run the Docker Container Locally

1. **Build the Docker image:**
   ```bash
   docker build -t python-web-app .
   ```
2. **Run the Docker container:**

   ``` bash 
   docker run -p 5000:5000 -e MESSAGE="Hello, World!" python-web-app
   ```

   The application will be accessible at `http://localhost:5000/api/message`.
3. **Access the REST API:**

   Visit `http://localhost:5000/api/message` in your browser or use `curl`:

   ``` bash 
   curl http://localhost:5000/api/message
   ```
4. **Access the Prometheus metrics:**

   Visit `http://localhost:5000/metrics` to see the custom metrics exposed by the application.

## Kubernetes Deployment

1. **Deploy the application:**

   Apply the Kubernetes manifests to your cluster:
   ``` bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```
2. **Verify the deployment:**

   Check if the pods are running:
   ``` bash
   kubectl get pods
   ```
3. **Access the application:**
   * If you are using Minikube, you may need to run `minikube tunnel` to access the Ingress.
   * Visit the application using the Ingress URL or `minikube service list` to get the external URL.

## Setting Up and Accessing Prometheus

1. **Deploy Prometheus to Kubernetes:**

   Apply the Prometheus manifests:
   
   ``` bash

   cd task2
   
   kubectl apply -f config.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml

   ```
   
2. **Access Prometheus:**

   * Forward the Prometheus port to your local machine:
     
     ``` bash
     kubectl port-forward deploy/prometheus-server 9090:9090
     ```
     
   * Access Prometheus in your browser at `http://localhost:9090`.

3. **Query the custom metrics:**

   In Prometheus, use the query `request_count` to view the number of requests made to the `/api/message` endpoint.

## Assumptions

* The Python web application uses Flask, and the Prometheus client library is used for metrics.
* The Kubernetes manifests assume a basic cluster setup and may need adjustments for production environments.

## Improvements

Given more time, I would implement the following improvements:

* **Security Enhancements:** Implement TLS/SSL for the Ingress, secure environment variables, and restrict access to the Prometheus endpoint.
* **Scalability:** Configure Horizontal Pod Autoscaling (HPA) based on CPU or memory usage.
* **Advanced Monitoring:** Integrate Grafana with Prometheus for better visualization and alerting.
* **Load Testing:** Use a tool like `locust` or `k6` to perform load testing on the application.
* **Logging Improvements:** Centralize logging using a solution like Elasticsearch, Logstash, and Kibana (ELK stack) or Fluentd and Grafana Loki.

## CI/CD Setup (Optional)

To set up a CI/CD pipeline for this project:

1. **CI/CD Platform:**
   * Use GitHub Actions, GitLab CI, AWS Codepipeline or Jenkins for the CI/CD pipeline.
2. **Pipeline Steps:**
   * **Build:** Automatically build the Docker image on every commit.
   * **Test:** Run unit tests for the Python application.
   * **Push:** Push the Docker image to a container registry (Docker Hub, AWS ECR, etc.).
   * **Deploy:** Deploy the application to a Kubernetes cluster using `kubectl` or a Helm chart.
   * **Monitor:** Trigger alerts if the deployment fails or metrics exceed defined thresholds.
3. **Infrastructure as Code (IaC):**
   * Use Terraform to manage the Kubernetes cluster, networking, and other infrastructure resources.
4. **Versioning:**
   * Tag releases and maintain a changelog to track updates and improvements.

---

This `README.md` provides an overview of how to get the Python web application running locally and in a Kubernetes environment, with monitoring through Prometheus. It also outlines potential improvements and a suggested CI/CD setup.
