# 🐳 Dockerized Python–MySQL App

A simple project showing how to connect a **Python application** with **MySQL** using **Docker Compose**, including proper networking and healthchecks.

----------

## 🚀 Features

- Python + MySQL using Docker Compose
- MySQL 8.0 with automatic DB and user creation
- Healthcheck to ensure DB readiness
- Custom Docker network
- Interactive Python CLI app

----------

## 📂 Project Structure

database-demo/
├── docker-compose.yml
├── Dockerfile
├── app.py
├── README.md


----------

## 🛠 Tech Stack

- Python 3
- MySQL 8.0
- Docker & Docker Compose

----------

## ▶️ How to Run

### Clean start
``` bash 
- docker compose down -v
- docker volume prune -f
- Start MySQL
- docker compose up -d mydb
- Check health:

```

``` bash

- docker inspect Mysqldb --format='{{.State.Health.Status}}'
- Run Python app
- docker compose run myapp

```

----------

🧠 Key Concepts Used

- Docker networking (service names)

- Healthchecks for service readiness

- depends_on with service_healthy

- Interactive containers with docker compose run
