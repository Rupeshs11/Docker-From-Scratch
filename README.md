# 🐳 Docker From Scratch

> A complete, hands-on Docker learning repository — from absolute zero to deploying multi-container production-grade apps.

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

---

## 📖 About This Repository

This repository documents my complete Docker learning journey — starting from the basics of containerization all the way to orchestrating multi-container applications with Docker Compose and Kubernetes. Each project is designed to teach specific Docker concepts through practical, real-world applications.

**What you'll find here:**

- ✅ Beginner-friendly Docker practicals
- ✅ Advanced multi-container setups
- ✅ Multi-stage Docker builds
- ✅ Docker Compose orchestration
- ✅ Nginx reverse proxy configurations
- ✅ Database containers with health checks
- ✅ Kubernetes deployment manifests
- ✅ Real-world project architectures (Django, Flask, Spring Boot, Node.js, Java)

---

## 📂 Repository Structure

```
Docker-From-Scratch/
│
├── 📘 Docker-Notes/                    # Docker reference PDFs & notes
│   ├── Docker.pdf
│   └── Docker_TWS.pdf
│
├── 🟢 Docker-praticals/                # Beginner-level Docker projects
│   ├── Simple-pyapp/                   # Python app with volume persistence
│   ├── Api-demo/                       # Containerized API consumer
│   └── database-demo/                  # Python + MySQL with Docker Compose
│
└── 🔴 Docker-Advanced-praticals/       # Advanced Docker projects
    ├── simple-java-docker/             # Basic Java containerization
    ├── flask-app-ecs/                  # Flask app with multi-stage build
    ├── two-tier-flask-app/             # Flask + MySQL two-tier architecture
    ├── todo-app/                       # Node.js app + Kubernetes manifests
    ├── django-notes-app/               # Django + React + Nginx + MySQL (full stack)
    └── Expenses-Tracker-WebApp/        # Spring Boot + MySQL (multi-stage build)
```

---

## 🟢 Beginner Practicals

### 1. Simple Python App — Volume Persistence

| Detail | Info |
|--------|------|
| **Path** | `Docker-praticals/Simple-pyapp/` |
| **Stack** | Python 3 |
| **Concept** | Dockerfile basics, Volumes, Data persistence |

A CLI app that stores user names to a file. Demonstrates how data is lost when containers are removed and how **Docker volumes** solve this problem.

```bash
# Build
docker build -t pyapp:1.0 ./Docker-praticals/Simple-pyapp/

# Run (interactive, with volume)
docker run -it -v mydata:/pyapp pyapp:1.0

# Verify data persists after container restart
docker run -it -v mydata:/pyapp pyapp:1.0
```

**Concepts Learned:**
- Writing a `Dockerfile` (FROM, WORKDIR, COPY, RUN, CMD)
- Building and tagging images
- Container ephemeral nature
- Docker volumes for data persistence

---

### 2. API Demo — External API Access from Container

| Detail | Info |
|--------|------|
| **Path** | `Docker-praticals/Api-demo/` |
| **Stack** | Python 3, `requests` library |
| **Concept** | Installing dependencies, Internet access from containers |

A containerized Python app that fetches random cat facts from a public API.

```bash
# Build
docker build -t api-demo:1.0 ./Docker-praticals/Api-demo/

# Run
docker run api-demo:1.0
```

**Concepts Learned:**
- Installing pip packages during image build (`RUN pip install`)
- Containers can access the internet by default
- Docker image layering
- Reproducible environments

---

### 3. Database Demo — Python + MySQL with Docker Compose

| Detail | Info |
|--------|------|
| **Path** | `Docker-praticals/database-demo/` |
| **Stack** | Python 3, MySQL 8.0, Docker Compose |
| **Concept** | Compose, Networking, Health checks, `depends_on` |

An interactive Python CLI that connects to a MySQL container, creates a table, and stores user data.

```bash
cd Docker-praticals/database-demo/

# Build the Python image first
docker build -t pyapp:2.0 .

# Start MySQL (wait for health check to pass)
docker compose up -d mydb

# Check MySQL health status
docker inspect Mysqldb --format='{{.State.Health.Status}}'

# Run the Python app interactively
docker compose run myapp
```

**Concepts Learned:**
- Docker Compose for multi-container apps
- Service-to-service communication via Docker networks
- MySQL initialization with environment variables
- Health checks (`test`, `interval`, `retries`, `start_period`)
- `depends_on` with `condition: service_healthy`
- Difference between `docker compose up` and `docker compose run`

---

## 🔴 Advanced Practicals

### 4. Simple Java Docker App

| Detail | Info |
|--------|------|
| **Path** | `Docker-Advanced-praticals/simple-java-docker/` |
| **Stack** | Java 17, Eclipse Temurin |
| **Concept** | Compiling code inside Docker, lightweight Alpine images |

```bash
docker build -t simple-java-app ./Docker-Advanced-praticals/simple-java-docker/
docker run simple-java-app
```

**Concepts Learned:**
- Running compiled languages in Docker
- Using Alpine-based images for smaller footprint
- Multi-step build process (compile + run) in a single Dockerfile

---

### 5. Flask App (ECS-Ready) — Multi-Stage Build

| Detail | Info |
|--------|------|
| **Path** | `Docker-Advanced-praticals/flask-app-ecs/` |
| **Stack** | Python 3.9, Flask |
| **Concept** | Multi-stage builds, Image size optimization |

```bash
cd Docker-Advanced-praticals/flask-app-ecs/

# Standard build
docker build -t flask-app .

# Multi-stage build (smaller image ~400MB → ~150MB)
docker build -f Dockerfile-multi -t flask-app:slim .

# Run
docker run -p 5000:5000 flask-app:slim

# Compare image sizes
docker images | grep flask-app
```

**Concepts Learned:**
- Multi-stage builds to reduce image size
- `ENTRYPOINT` vs `CMD`
- Health check endpoints (`/health`)
- ECS deployment readiness

---

### 6. Two-Tier Flask App — Flask + MySQL

| Detail | Info |
|--------|------|
| **Path** | `Docker-Advanced-praticals/two-tier-flask-app/` |
| **Stack** | Python 3.9, Flask, MySQL, Docker Compose |
| **Concept** | Two-tier architecture, Compose networking, Multi-stage build |

A message board app with a MySQL backend. Demonstrates a complete two-tier architecture.

```
User → Flask (:5000) → MySQL (:3306)
```

```bash
cd Docker-Advanced-praticals/two-tier-flask-app/

# Standard start
docker compose up -d

# OR use multi-stage optimized build
docker build -f Dockerfile-multistage -t flask-app:optimized .

# Access
# http://localhost:5000
```

**Concepts Learned:**
- Docker Compose `services`, `networks`, `volumes`
- Environment variable injection
- MySQL data persistence with named volumes
- Health checks for both app and database
- Standard vs multi-stage Dockerfile comparison

---

### 7. Todo App — Node.js + Kubernetes

| Detail | Info |
|--------|------|
| **Path** | `Docker-Advanced-praticals/todo-app/` |
| **Stack** | Node.js 12, Docker Compose, Kubernetes |
| **Concept** | Node containerization, K8s Deployments, Services |

```bash
# Docker Compose
cd Docker-Advanced-praticals/todo-app/
docker compose up -d
# Access: http://localhost:8000

# Kubernetes deployment
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
# Access: http://<node-ip>:30003
```

**Kubernetes Manifests Included:**
- `deployment.yml` — 2 replicas with resource limits
- `service.yml` — NodePort service on port 30003

**Concepts Learned:**
- Containerizing Node.js apps
- Transition from Docker Compose to Kubernetes
- K8s Deployments, ReplicaSets, Pods
- K8s Services (NodePort)
- Resource requests and limits

---

### 8. Django Notes App — Full Stack (Django + React + Nginx + MySQL)

| Detail | Info |
|--------|------|
| **Path** | `Docker-Advanced-praticals/django-notes-app/` |
| **Stack** | Django, React, Nginx, MySQL 8.0, Gunicorn |
| **Concept** | Reverse proxy, Multi-service Compose, Production deployment |

The most complex project — a full-stack notes application with 4 services orchestrated via Docker Compose.

```
Client → Nginx (:80) → Django/Gunicorn (:8000) → MySQL (:3306)
                ↑
          React Frontend (static files)
```

```bash
cd Docker-Advanced-praticals/django-notes-app/

docker compose up --build -d
docker compose ps

# Access
# http://localhost       → App via Nginx
# http://localhost:8000  → Django API (direct)
```

**Concepts Learned:**
- Multi-container orchestration (4 services)
- Nginx as a reverse proxy
- Gunicorn as WSGI server
- MySQL persistent storage
- `.env` files for secrets
- Health checks across services
- `depends_on` for boot order

---

### 9. Expenses Tracker — Spring Boot + MySQL (Multi-Stage Build)

| Detail | Info |
|--------|------|
| **Path** | `Docker-Advanced-praticals/Expenses-Tracker-WebApp/` |
| **Stack** | Java 17, Spring Boot, Maven, MySQL 8.0 |
| **Concept** | Multi-stage Maven build, Spring Boot containerization |

A production-grade expense tracker with user auth, built with Spring Boot.

```bash
cd Docker-Advanced-praticals/Expenses-Tracker-WebApp/

docker compose up -d
# Access: http://localhost:8080
```

**Dockerfile highlights:**
```dockerfile
# Stage 1: Build JAR with Maven
FROM maven:3.9.12-eclipse-temurin-17 AS builder
RUN mvn clean install -DskipTests=true

# Stage 2: Run JAR with slim JDK
FROM eclipse-temurin:17-jdk-alpine
COPY --from=builder /app/target/*.jar expenseapp.jar
CMD ["java", "-jar", "expenseapp.jar"]
```

**Concepts Learned:**
- Multi-stage builds for Java/Maven projects
- Spring Boot Docker best practices
- Spring environment variables via Docker Compose
- MySQL health checks with `mysqladmin ping`

---

## 🐳 Docker Commands — Complete Reference

### Installation & Setup

```bash
# Check Docker version
docker --version
docker compose version

# Docker system info
docker info

# Login to Docker Hub
docker login
```

### Image Commands

```bash
# Build an image from Dockerfile
docker build -t <image_name>:<tag> .

# Build with a specific Dockerfile
docker build -f Dockerfile-multi -t <image_name>:<tag> .

# List all local images
docker images

# Remove an image
docker rmi <image_name>:<tag>

# Remove all unused images
docker image prune -a

# Pull an image from Docker Hub
docker pull <image_name>:<tag>

# Push an image to Docker Hub
docker push <username>/<image_name>:<tag>

# Tag an image
docker tag <image_id> <username>/<image_name>:<tag>

# Inspect an image
docker image inspect <image_name>

# View image build history
docker history <image_name>
```

### Container Commands

```bash
# Run a container
docker run <image_name>

# Run with port mapping
docker run -p <host_port>:<container_port> <image_name>

# Run in detached mode (background)
docker run -d <image_name>

# Run interactively
docker run -it <image_name>

# Run with a custom name
docker run --name <container_name> <image_name>

# Run with environment variables
docker run -e KEY=VALUE <image_name>

# Run with auto-remove on exit
docker run --rm <image_name>

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container_id>

# Start a stopped container
docker start <container_id>

# Restart a container
docker restart <container_id>

# Remove a container
docker rm <container_id>

# Remove all stopped containers
docker container prune

# Force remove a running container
docker rm -f <container_id>

# View container logs
docker logs <container_id>

# Follow container logs in real-time
docker logs -f <container_id>

# Execute a command in a running container
docker exec -it <container_id> bash

# Inspect container details
docker inspect <container_id>

# View container resource usage
docker stats

# Copy files to/from container
docker cp <file> <container_id>:/path/
docker cp <container_id>:/path/<file> .
```

### Volume Commands

```bash
# Create a named volume
docker volume create <volume_name>

# List all volumes
docker volume ls

# Inspect a volume
docker volume inspect <volume_name>

# Remove a volume
docker volume rm <volume_name>

# Remove all unused volumes
docker volume prune

# Run container with named volume
docker run -v <volume_name>:/path/in/container <image_name>

# Run container with bind mount
docker run -v /host/path:/container/path <image_name>
```

### Network Commands

```bash
# List all networks
docker network ls

# Create a custom network
docker network create <network_name>

# Inspect a network
docker network inspect <network_name>

# Connect a container to a network
docker network connect <network_name> <container_id>

# Disconnect a container from a network
docker network disconnect <network_name> <container_id>

# Remove a network
docker network rm <network_name>

# Remove all unused networks
docker network prune
```

### Docker Compose Commands

```bash
# Start services (detached)
docker compose up -d

# Start with build
docker compose up --build -d

# Stop services
docker compose down

# Stop and remove volumes
docker compose down -v

# View running services
docker compose ps

# View logs
docker compose logs -f

# View logs for a specific service
docker compose logs -f <service_name>

# Run a one-off command
docker compose run <service_name> <command>

# Restart a specific service
docker compose restart <service_name>

# Scale a service
docker compose up -d --scale <service_name>=<count>

# Build without starting
docker compose build

# Pull latest images
docker compose pull
```

### System & Cleanup Commands

```bash
# View disk usage
docker system df

# Remove all unused data (images, containers, volumes, networks)
docker system prune -a

# Remove all unused volumes
docker volume prune -f

# Remove all stopped containers
docker container prune -f

# Remove all unused images
docker image prune -a -f

# Remove all unused networks
docker network prune -f
```

---

## 📘 Docker Concepts — Learning Guide

### 1. What is Docker?

Docker is a platform for building, shipping, and running applications inside **containers** — lightweight, isolated environments that package an app with all its dependencies.

```
Traditional Deployment          Docker Deployment
┌──────────────────┐           ┌──────────────────┐
│   App A  │ App B │           │ ┌──────┐ ┌──────┐│
│          │       │           │ │Cont A│ │Cont B││
│  Shared Libraries│           │ │ Libs │ │ Libs ││
│                  │           │ └──────┘ └──────┘│
│   Host OS        │           │   Docker Engine   │
│   Hardware       │           │   Host OS         │
└──────────────────┘           └──────────────────┘
```

### 2. Docker Architecture

```
┌─────────────────────────────────────────────────┐
│                Docker Client (CLI)               │
│         docker build / run / pull / push         │
└─────────────────┬───────────────────────────────┘
                  │ REST API
┌─────────────────▼───────────────────────────────┐
│              Docker Daemon (dockerd)              │
│                                                   │
│  ┌───────────┐  ┌───────────┐  ┌──────────────┐ │
│  │  Images    │  │ Containers│  │   Networks    │ │
│  └───────────┘  └───────────┘  └──────────────┘ │
│  ┌───────────┐  ┌──────────────────────────────┐ │
│  │  Volumes   │  │      Docker Registry         │ │
│  └───────────┘  │      (Docker Hub)             │ │
│                  └──────────────────────────────┘ │
└───────────────────────────────────────────────────┘
```

### 3. Docker Image vs Container

| Aspect | Image | Container |
|--------|-------|-----------|
| **What** | Blueprint / Template | Running instance of an image |
| **State** | Immutable (read-only) | Mutable (read-write layer) |
| **Analogy** | Class | Object |
| **Created by** | `docker build` | `docker run` |
| **Stored in** | Registry (Docker Hub) | Host machine |

### 4. Dockerfile Instructions

| Instruction | Purpose | Example |
|-------------|---------|---------|
| `FROM` | Base image | `FROM python:3.9-slim` |
| `WORKDIR` | Set working directory | `WORKDIR /app` |
| `COPY` | Copy files from host | `COPY . /app` |
| `ADD` | Copy + extract archives | `ADD archive.tar.gz /app` |
| `RUN` | Execute command during build | `RUN pip install -r requirements.txt` |
| `CMD` | Default command at runtime | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | Fixed command at runtime | `ENTRYPOINT ["python", "app.py"]` |
| `EXPOSE` | Document port (metadata) | `EXPOSE 8000` |
| `ENV` | Set environment variable | `ENV DEBUG=true` |
| `ARG` | Build-time variable | `ARG VERSION=1.0` |
| `VOLUME` | Create mount point | `VOLUME /data` |
| `HEALTHCHECK` | Container health check | `HEALTHCHECK CMD curl -f http://localhost/` |
| `LABEL` | Add metadata | `LABEL version="1.0"` |

### 5. CMD vs ENTRYPOINT

```dockerfile
# CMD — can be overridden at runtime
CMD ["python", "app.py"]
# docker run myapp python other.py  ← overrides CMD

# ENTRYPOINT — cannot be easily overridden
ENTRYPOINT ["python", "app.py"]
# docker run myapp  ← always runs python app.py

# Combined — ENTRYPOINT is fixed, CMD provides defaults
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run myapp         ← runs: python app.py
# docker run myapp test.py ← runs: python test.py
```

### 6. Multi-Stage Builds

Multi-stage builds reduce final image size by separating the build environment from the runtime environment.

```dockerfile
# Stage 1: Build (large image with build tools)
FROM maven:3.9 AS builder
WORKDIR /app
COPY . .
RUN mvn clean package

# Stage 2: Run (slim image with only runtime)
FROM eclipse-temurin:17-jdk-alpine
COPY --from=builder /app/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]
```

**Result:** Final image contains only the JAR file + JDK, not Maven or source code.

### 7. Docker Networking

| Network Type | Description | Use Case |
|-------------|-------------|----------|
| `bridge` | Default network, isolated | Single-host container communication |
| `host` | Shares host network stack | Performance-sensitive apps |
| `none` | No networking | Isolated batch jobs |
| `overlay` | Multi-host networking | Docker Swarm / multi-node |
| `custom bridge` | User-defined bridge | Compose services (DNS resolution) |

```bash
# Containers on the same custom network can talk via service names
docker network create my-net
docker run --network my-net --name db mysql
docker run --network my-net --name app myapp
# "app" can reach "db" using hostname "db"
```

### 8. Docker Volumes — Data Persistence

```
Container lifecycle:    Created → Running → Stopped → Removed
Data WITHOUT volume:    Created → Running → Stopped → 💥 LOST
Data WITH volume:       Created → Running → Stopped → ✅ PERSISTED
```

| Type | Syntax | Use Case |
|------|--------|----------|
| Named Volume | `-v mydata:/app/data` | Database storage, shared data |
| Bind Mount | `-v /host/path:/container/path` | Development, config files |
| tmpfs Mount | `--tmpfs /tmp` | Temporary data, secrets |

### 9. Docker Compose

Docker Compose is a tool for defining and running **multi-container** Docker applications using a YAML file.

```yaml
# docker-compose.yml structure
services:
  web:                          # Service name
    build: .                    # Build from Dockerfile
    ports:
      - "8080:8080"            # Port mapping
    environment:                # Environment variables
      - DB_HOST=db
    depends_on:                 # Start order
      - db
    networks:                   # Network attachment
      - app-net
    restart: always             # Restart policy
    healthcheck:                # Health monitoring
      test: ["CMD", "curl", "-f", "http://localhost:8080"]
      interval: 10s
      timeout: 5s
      retries: 5

  db:
    image: mysql:8.0           # Pre-built image
    volumes:
      - db-data:/var/lib/mysql # Persistent storage
    networks:
      - app-net

volumes:
  db-data:                     # Named volume declaration

networks:
  app-net:                     # Custom network declaration
```

### 10. Health Checks

Health checks tell Docker whether a container is functioning properly.

```yaml
healthcheck:
  test: ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]
  interval: 10s       # Time between checks
  timeout: 5s         # Max time for a single check
  retries: 5          # Failures before "unhealthy"
  start_period: 30s   # Grace period after container start
```

**Health States:** `starting` → `healthy` / `unhealthy`

### 11. Docker Best Practices

| Practice | Why |
|----------|-----|
| Use `.dockerignore` | Exclude unnecessary files from build context |
| Use specific image tags | `python:3.9-slim` not `python:latest` |
| Minimize layers | Combine `RUN` commands with `&&` |
| Use multi-stage builds | Smaller, more secure final images |
| Don't run as root | Use `USER` instruction for security |
| Use health checks | Enable proper orchestration |
| Order Dockerfile by change frequency | Leverage build cache (least changing → most changing) |
| Use `--no-cache-dir` for pip | Smaller images |
| Clean up apt lists | `rm -rf /var/lib/apt/lists/*` |

---

## 🏗️ Project Architecture Summary

| # | Project | Stack | Docker Concepts |
|---|---------|-------|----------------|
| 1 | Simple Python App | Python | Dockerfile, Volumes |
| 2 | API Demo | Python, Requests | Dependencies, Internet access |
| 3 | Database Demo | Python, MySQL | Compose, Networks, Health checks |
| 4 | Simple Java App | Java 17 | Alpine images, Compile in Docker |
| 5 | Flask ECS App | Flask | Multi-stage builds, ENTRYPOINT |
| 6 | Two-Tier Flask | Flask, MySQL | Two-tier arch, Compose, Multi-stage |
| 7 | Todo App | Node.js | K8s Deployment, Services, NodePort |
| 8 | Django Notes App | Django, React, Nginx, MySQL | Reverse proxy, 4-service Compose |
| 9 | Expenses Tracker | Spring Boot, Maven, MySQL | Multi-stage Maven build, Spring in Docker |

---

## 🚀 Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac) or Docker Engine (Linux)
- [Git](https://git-scm.com/)

### Clone the Repository

```bash
git clone https://github.com/Rupeshs11/Docker-From-Scratch.git
cd Docker-From-Scratch
```

### Recommended Learning Path

```
Start Here
    │
    ▼
1. Simple-pyapp          → Learn Dockerfile basics & volumes
    │
    ▼
2. Api-demo              → Learn dependency installation & layers
    │
    ▼
3. database-demo         → Learn Docker Compose & networking
    │
    ▼
4. simple-java-docker    → Learn multi-language containerization
    │
    ▼
5. flask-app-ecs         → Learn multi-stage builds
    │
    ▼
6. two-tier-flask-app    → Learn two-tier architecture
    │
    ▼
7. todo-app              → Learn Kubernetes basics
    │
    ▼
8. django-notes-app      → Learn full-stack multi-service deployment
    │
    ▼
9. Expenses-Tracker      → Learn production Java/Spring Boot Docker
    │
    ▼
  🎉 You're Docker Proficient!
```

---

## 📚 Reference Materials

| Resource | Location |
|----------|----------|
| Docker PDF Notes | `Docker-Notes/Docker.pdf` |
| Docker TWS Notes | `Docker-Notes/Docker_TWS.pdf` |
| [Docker Official Docs](https://docs.docker.com/) | Web |
| [Docker Hub](https://hub.docker.com/) | Web |
| [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/) | Web |
| [Compose File Reference](https://docs.docker.com/compose/compose-file/) | Web |

---

## 🧰 Quick Cheatsheet

```
┌─────────────────────────────────────────────────────────────┐
│                    DOCKER CHEATSHEET                         │
├──────────────────┬──────────────────────────────────────────┤
│ Build image      │ docker build -t name:tag .               │
│ Run container    │ docker run -d -p 8080:8080 name:tag      │
│ List containers  │ docker ps -a                             │
│ View logs        │ docker logs -f <container>               │
│ Shell into       │ docker exec -it <container> bash         │
│ Stop container   │ docker stop <container>                  │
│ Remove container │ docker rm <container>                    │
│ Compose up       │ docker compose up -d                     │
│ Compose down     │ docker compose down -v                   │
│ System cleanup   │ docker system prune -a                   │
└──────────────────┴──────────────────────────────────────────┘
```

---

## 👤 Author

**Rupesh** — [@Rupeshs11](https://github.com/Rupeshs11)

---

## ⭐ Support

If this repository helped you learn Docker, please consider giving it a **star** ⭐ — it motivates me to add more projects and content!

---

## 📄 License

This project is open source and available for learning purposes.
