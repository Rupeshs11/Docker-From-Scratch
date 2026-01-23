# Node.js Todo App 📝

A simple and lightweight Todo application built with **Node.js** and **Express**, fully containerized with **Docker** for easy deployment and scalability.

![Node.js](https://img.shields.io/badge/Node.js-12.2.0-green?logo=node.js)
![Express](https://img.shields.io/badge/Express-4.14.0-blue?logo=express)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)

---

## ✨ Features

- ✅ **Add** new todo items
- ✏️ **Edit** existing todos
- 🗑️ **Delete** completed tasks
- 🐳 **Docker** support for easy deployment
- 🎨 Clean and responsive UI with **EJS templates**
- 🧪 Built-in **testing** with Mocha & Chai

---

## 🚀 Quick Start

### 🐳 Run with Docker

```bash
# Build the Docker image
docker build -t node-todo-app .

# Run the container
docker run -p 8000:8000 node-todo-app
```

### 💻 Run Locally

```bash
# Install dependencies
npm install

# Start the application
npm start
# OR
node app.js
```

### 🧪 Run Tests

```bash
npm test
```

📍 Visit **http://localhost:8000** in your browser.

---

## 📁 Project Structure

```
node-todo/
├── app.js           # Main Express application
├── Dockerfile       # Docker configuration
├── package.json     # Project dependencies & scripts
├── README.md        # Project documentation
└── views/           # EJS templates
    ├── todo.ejs         # Main todo list view
    └── edititem.ejs     # Edit item view
```

---

## 🛠️ Tech Stack

| Technology       | Purpose             |
| ---------------- | ------------------- |
| **Node.js**      | Runtime environment |
| **Express**      | Web framework       |
| **EJS**          | Templating engine   |
| **Docker**       | Containerization    |
| **Mocha & Chai** | Testing framework   |

---

## 📦 Dependencies

### Production

- `express` - Fast, minimalist web framework
- `ejs` - Embedded JavaScript templates
- `body-parser` - Parse incoming request bodies
- `method-override` - HTTP verb support (PUT/DELETE)
- `sanitizer` - Input sanitization

### Development

- `mocha` - Testing framework
- `chai` - Assertion library
- `supertest` - HTTP testing
- `nyc` - Code coverage

---

## 🐳 Docker Commands

```bash
# Build image
docker build -t node-todo-app .

# Run container
docker run -p 8000:8000 node-todo-app

# Run in detached mode
docker run -d -p 8000:8000 node-todo-app

# Stop container
docker stop <container_id>
```

---

## 📝 License

This project is open source and available for learning purposes.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---
