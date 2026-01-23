# 🐳 Docker Practice Summary

This repository contains my Docker practice work where I explored how containers are used in real-world scenarios.  
The goal of these exercises was to understand **core Docker concepts**, not just run containers.

---

## 📘 What I Practiced

### 1️⃣ Python + Database (MySQL)

In this practice, I connected a Python application with a MySQL database running inside a Docker container.

**What I learned:**
- How containers communicate with each other using Docker networks
- How environment variables are used to configure MySQL automatically
- Why service names are used instead of `localhost` inside containers
- How database users and schemas are created during container initialization
- How to avoid race conditions using Docker healthchecks
- The difference between a container being *running* and being *ready*
- How `depends_on` works with `service_healthy`

---

### 2️⃣ File Persistence using Docker Volumes (users.txt)

In this practice, I stored user data in a text file and persisted it using Docker volumes.

**What I learned:**
- Containers are ephemeral by default
- Data inside a container is lost when the container stops
- How Docker volumes preserve data outside the container lifecycle
- How host files can be mounted into containers
- How volumes are useful for logs, configs, and user data

---

### 3️⃣ API Container (External API Access)

In this practice, I created a Python application that consumes a public API from inside a Docker container.

**What I learned:**
- Containers can access the internet by default
- How to install external Python dependencies inside Docker images
- Why dependencies must be installed during image build
- How Docker images are built layer by layer
- How containerized apps behave the same across different systems

---

## 🧠 Key Docker Concepts I Understood

- Docker images vs containers
- Container lifecycle (build, run, stop, remove)
- Dockerfile basics
- Docker Compose for multi-container applications
- Networking between containers
- Environment variables in containers
- Volumes for data persistence
- Healthchecks for service readiness
- Difference between `docker compose up` and `docker compose run`

---

## 🎯 Outcome

Through these practices, I gained hands-on experience with Docker and learned how containerization is used in backend development and DevOps workflows.

This repository reflects my learning journey and practical understanding of Docker fundamentals.

---

## 👤 Author

**Knox**
