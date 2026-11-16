#  Python Multi-Container Docker Bridge Project

A lightweight, multi-container Docker application built using **Core Python**, designed to demonstrate Docker Networking, Named Volumes, Environment Variables, and Container Communication without relying on complex frameworks.

---

##  Project Architecture
This project consists of two Python containers running in parallel inside a custom Docker bridge network, communicating and sharing data via a Docker Named Volume:
1. **Writer Container (`py-writer`)**: Generates timestamped logs with a customized user environment variable and writes them into a shared volume every 5 seconds.
2. **Reader Container (`py-reader`)**: Reads data from the shared volume in real-time and outputs the logs.

---

##  Tech Stack & Concepts Covered
* **Core Python** (File I/O, loops, os environment variables)
* **Docker Images & Dockerfile** (`python:3.11-slim`)
* **Docker Networks** (Bridge driver for container isolation and communication)
* **Docker Volumes** (Named volumes for persistent data sharing)
* **Environment Variables** (`-e` flag for dynamic configuration)

---

##  Prerequisites
Make sure you have **Docker Desktop** installed and running on your machine.

---

##  Step-by-Step Execution Guide

### 1. Build the Docker Image
Navigate to the project folder and build the image:
bash
docker build -t py-bridge:v1 .


2. Create a Custom Docker Network
Bash
docker network create bridge-net


3. Create a Docker Named Volume
Bash
docker volume create shared-logs


4. Run the Writer Container
Pass an environment variable (USER_NAME) and mount the named volume:

Bash
docker run -d --name py-writer --network bridge-net -e USER_NAME="Hitakshi" -v shared-logs:/shared_data py-bridge:v1 python writer.py


5. Run the Reader Container
Run the second container connected to the same network and volume:

Bash
docker run -d --name py-reader --network bridge-net -v shared-logs:/shared_data py-bridge:v1 python reader.py
Verification & Debugging
Check running containers:

Bash
docker ps
View live logs from the reader container:

Bash
docker logs -f py-reader
Inspect inside the container (exec):

Bash
docker exec -it py-reader /bin/bash
cat /shared_data/logs.txt
exit


Cleanup Commands
To stop and remove containers, networks, and volumes:

Bash
docker stop py-writer py-reader
docker rm py-writer py-reader
docker volume rm shared-logs
docker network rm bridge-net# python-docker-bridge
