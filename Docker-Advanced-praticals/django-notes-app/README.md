# Django Notes App — Dockerized with Docker Compose

A **Django + React** notes app running with **Nginx**, **Django (Gunicorn)**, and **MySQL** using Docker Compose.

```
Client → Nginx (:80) → Django (:8000) → MySQL (:3306)
```

---

## Prerequisites

- Docker & Docker Compose installed
- Git

---

## Setup

```bash
# Clone the repo
git clone https://github.com/Rupeshs11/Docker-From-Scratch.git
cd Docker-From-Scratch/Docker-Advanced-praticals/django-notes-app

# Build and start all containers
docker compose up --build -d

# Check status
docker compose ps
```

---

## Access

| URL | Description |
|-----|-------------|
| `http://localhost` | App via Nginx |
| `http://localhost:8000` | Django API (Direct) |
| `http://localhost:8000/admin` | Django Admin Panel |

---

## Useful Commands

```bash
docker compose up -d              # Start services
docker compose down               # Stop services
docker compose logs -f            # View logs
docker compose up --build -d      # Rebuild & restart
docker exec -it django_cont bash  # Shell into Django container
docker compose down -v            # Stop & remove volumes
```

---

## Project Structure

```
django-notes-app/
├── api/                 # Django REST API
├── mynotes/             # React frontend
├── nginx/               # Nginx reverse proxy config
├── notesapp/            # Django project settings
├── docker-compose.yml   # Multi-container setup
├── Dockerfile           # Django container
├── .env                 # Environment variables
└── requirements.txt     # Python dependencies
```

---

## Docker Concepts Covered

- Multi-container orchestration with Docker Compose
- Nginx reverse proxy
- MySQL with persistent volumes
- Health checks for containers
- Environment variables via `.env`
- Service dependency management (`depends_on`)

---

**Author:** [@Rupeshs11](https://github.com/Rupeshs11)

