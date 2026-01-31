# Simple Java Docker App

A lightweight Java application designed to demonstrate containerization using Docker. This project compiles and runs a simple Java program that prints a greeting and the current system date/time.

## Features

- **Date & Time Display**: Outputs the current server/container date and time.
- **Dockerized Environment**: Fully containerized for consistent execution across different environments.
- **Simple Logic**: Clean and minimal Java codebase, perfect for learning Docker basics.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.

## Usage

### 1. Build the Docker Image

Navigate to the project directory and build the image:

```bash
docker build -t simple-java-app .
```

### 2. Run the Container

Run the application using the following command:

```bash
docker run simple-java-app
```

## Directory Structure

```
simple-java-docker/
├── Dockerfile      # Docker configuration
├── README.md       # Project documentation
└── src/
    └── Main.java   # Java source code
```
