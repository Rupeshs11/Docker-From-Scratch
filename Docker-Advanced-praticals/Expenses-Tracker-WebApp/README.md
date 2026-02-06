# Expenses Tracker - Docker Practical

A containerized Spring Boot application for tracking personal expenses with MySQL database.

## Tech Stack

- **Backend:** Java 17, Spring Boot, Spring Security, Spring Data JPA
- **Frontend:** Thymeleaf, Bootstrap
- **Database:** MySQL 8.0
- **Containerization:** Docker, Docker Compose

## Features

- User authentication and authorization
- Add, view, update, and delete expenses
- Filter expenses by category/date
- Responsive Bootstrap UI

## Quick Start

### Prerequisites

- Docker & Docker Compose installed

### Run with Docker Compose

```bash
# Clone and navigate to the project
cd Expenses-Tracker-WebApp

# Start the containers
docker-compose up -d

# Check container status
docker-compose ps
```

Access the app at: `http://localhost:8080`

### Stop Containers

```bash
docker-compose down
```

## Project Structure

```
Expenses-Tracker-WebApp/
├── src/                    # Java source code
├── Dockerfile              # Multi-stage build for Java app
├── docker-compose.yml      # Container orchestration
├── pom.xml                 # Maven dependencies
└── sql_script.sql          # Database schema
```

## Docker Architecture

| Service    | Container   | Port | Description             |
| ---------- | ----------- | ---- | ----------------------- |
| `java_app` | expensesapp | 8080 | Spring Boot application |
| `mysql_db` | mysql       | 3306 | MySQL database          |

## Environment Variables

| Variable                     | Default                                  | Description             |
| ---------------------------- | ---------------------------------------- | ----------------------- |
| `SPRING_DATASOURCE_URL`      | jdbc:mysql://mysql:3306/expenses_tracker | Database connection URL |
| `SPRING_DATASOURCE_USERNAME` | root                                     | Database username       |
| `SPRING_DATASOURCE_PASSWORD` | Test@123                                 | Database password       |

## License

MIT License
