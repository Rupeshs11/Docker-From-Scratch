# Two-Tier Flask Application

A simple message board application built with Flask and MySQL, fully containerized using Docker. This project demonstrates a classic two-tier architecture where the Flask application handles the frontend and backend logic, while MySQL serves as the persistent data layer.

## Overview

This application allows users to submit and view messages through a clean, modern web interface. All messages are stored in a MySQL database, ensuring data persistence across container restarts.

## Tech Stack

- **Backend:** Python 3.9, Flask
- **Database:** MySQL
- **Containerization:** Docker, Docker Compose
- **Frontend:** HTML, CSS, JavaScript (jQuery)

## Project Structure

```
two-tier-flask-app/
├── app.py                  # Main Flask application
├── Dockerfile              # Standard Docker build file
├── Dockerfile-multistage   # Optimized multi-stage build
├── docker-compose.yml      # Container orchestration config
├── requirements.txt        # Python dependencies
├── message.sql             # Database schema reference
└── templates/
    └── index.html          # Frontend UI
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone this repository:

2. Start the containers:

   ```bash
   docker-compose up -d
   ```

3. Open your browser and navigate to:

   ```
   http://localhost:5000
   ```

4. To stop the application:
   ```bash
   docker-compose down
   ```

## Docker Configuration

### Standard Build

The `Dockerfile` uses Python 3.9-slim as the base image and installs all necessary dependencies for connecting to MySQL.

### Multi-Stage Build

The `Dockerfile-multistage` provides an optimized build that separates the build and runtime stages, resulting in a smaller final image.

To use the multi-stage build:

```bash
docker build -f Dockerfile-multistage -t flask-app:optimized .
```

## Environment Variables

The application uses the following environment variables (configured in `docker-compose.yml`):

| Variable         | Description           | Default Value |
| ---------------- | --------------------- | ------------- |
| `MYSQL_HOST`     | MySQL server hostname | mysql         |
| `MYSQL_USER`     | Database username     | root          |
| `MYSQL_PASSWORD` | Database password     | root          |
| `MYSQL_DB`       | Database name         | devops        |

## Features

- Submit messages through a modern glassmorphic UI
- Real-time message display using AJAX
- Persistent storage with MySQL
- Health checks for both Flask and MySQL containers
- Automatic database table creation on startup

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available for learning purposes.
