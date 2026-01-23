# Simple Java Docker Project

A simple Java application that runs inside a Docker container.

## 📋 Description

This project demonstrates how to containerize a basic Java application using Docker. The application prints a greeting message along with the current date.

## 🛠️ Technologies Used

- Java 17 (Eclipse Temurin)
- Docker

## 📁 Project Structure

```
simple-java-page/
├── Dockerfile
├── README.md
└── src/
    └── Main.java
```

## 🐳 Docker Commands

### Build the Docker Image

```bash
docker build -t simple-java-app .
```

### Run the Container

```bash
docker run simple-java-app
```

## 📤 Expected Output

```
Hello, Knox! Current date: Mon Jan 20 05:43:52 UTC 2026
Welcome to the container
```

## 📝 Dockerfile Explained

| Instruction                          | Description                                 |
| ------------------------------------ | ------------------------------------------- |
| `FROM eclipse-temurin:17-jdk-alpine` | Uses lightweight Alpine-based Java 17 image |
| `WORKDIR /app`                       | Sets working directory inside container     |
| `COPY src/Main.java ./Main.java`     | Copies source code to container             |
| `RUN javac Main.java`                | Compiles the Java application               |
| `CMD ["java","Main"]`                | Runs the compiled application               |

## 👤 Author

**Knox**

---
