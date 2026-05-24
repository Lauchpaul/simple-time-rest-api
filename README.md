# 🕒 Simple Time REST API

A lightweight, containerized Python REST API built with Flask that returns the current server time in JSON format. This project serves as a practical, hands-on learning environment for Python OOP, decorators, modules, and Docker containerization.

---

## 💡 Python & OOP Learnings

During the development of this project, several core Python and Object-Oriented Programming (OOP) concepts were explored and mastered. Here is a breakdown of the key takeaways from [app.py](file:///home/leon/simple-time-rest-api/app.py):

### 1. Object-Oriented Programming (OOP) & Classes
* **Instantiating Objects**: We import the `Flask` class and create an application object (instance) using:
  ```python
  app = Flask(__name__)
  ```
* **Naming Conventions**: In Python, classes typically follow `PascalCase` (e.g., `Flask`), while modules, functions, and variables follow `snake_case`. However, standard libraries aren't always perfectly consistent—for instance, the `datetime` module contains a class also named `datetime` (lowercase). As noted during learning: python naming conventions can be quirky sometimes! 😉

### 2. Modules & Imports
* **What is a Module?** In Python, a module is simply a `.py` file containing code.
* **Selective Importing**:
  ```python
  from flask import Flask, jsonify
  from datetime import datetime
  ```
  This imports specific classes (`Flask`, `datetime`) and functions (`jsonify`) from their respective modules, keeping our namespace clean.

### 3. Decorators
* **What they do**: Decorators (prefixed with `@`) modify or extend the behavior of a function without changing its source code.
* **Flask Routing**: 
  ```python
  @app.route('/time', methods=['GET'])
  def get_time(): ...
  ```
  The `@app.route` decorator registers the `get_time` function with the Flask web server, mapping the `/time` URL path directly to it. Under the hood, Flask builds a map:
  ```python
  if request.path == "/time":
      return get_time()
  ```
* **JSON Serialization**: The `jsonify()` function serializes a Python dictionary into a JSON-formatted string and automatically configures the appropriate HTTP `Content-Type` header (`application/json`).

### 4. The Magic of `__name__ == '__main__'`
* **Module Execution Context**: `__name__` is a built-in variable that Python automatically sets for every module:
  * If the script is run directly (e.g., `python app.py`), `__name__` is set to `'__main__'`.
  * If the script is imported into another file, `__name__` is set to the actual file/module name.
* **Guard Block**: The condition `if __name__ == '__main__':` ensures the Flask development server only runs when the file is executed directly, not when imported.

### 5. Docker Host Binding
* **Crucial Network Configuration**:
  ```python
  app.run(host='0.0.0.0', port=5000)
  ```
  Binding to `0.0.0.0` tells the Flask app to listen on all available network interfaces. Without this, the app would only accept local connections inside the container (loopback/localhost), making it inaccessible from the host machine.

---

## 🐳 Docker Containerization Guide

Follow this guide to build, launch, access, and clean up your Docker container.

### 🚀 Quick Start Commands

| Action | Command | Description |
| :--- | :--- | :--- |
| **Build** | `sudo docker build -t simple-time-rest-api .` | Builds a Docker image named `simple-time-rest-api` using the local `Dockerfile`. |
| **Run (Interactive)** | `docker run -p 5000:5000 simple-time-rest-api` | Runs the container in the foreground, mapping host port `5000` to container port `5000`. |
| **Run (Detached)** | `docker run -d -p 5000:5000 simple-time-rest-api` | Runs the container in the background (detached mode) and outputs the container ID. |

---

### 1. Build the Image
To build the container image from the `Dockerfile` in the current directory:
```bash
sudo docker build -t simple-time-rest-api .
```

### 2. Launch the Container
Run the container and map host port `5000` to the container's exposed port `5000`:
* **Foreground Mode** (useful to see live server logs):
  ```bash
  docker run -p 5000:5000 simple-time-rest-api
  ```
* **Background / Detached Mode** (runs in the background, freeing your terminal):
  ```bash
  docker run -d -p 5000:5000 simple-time-rest-api
  ```

### 3. Access the API
Once the container is running, open your web browser or use `curl` in a terminal:
* **Browser**: Visit [http://localhost:5000/time](http://localhost:5000/time)
* **Terminal**:
  ```bash
  curl http://localhost:5000/time
  ```
  **Response Format:**
  ```json
  {
    "status": "success",
    "server_time": "2026-05-25 01:52:02",
    "timezone": "UTC"
  }
  ```

---

### 🧹 The Cleanup Process (Clean it! 😉)

When you're done testing, follow these steps to cleanly stop and remove your containers and images.

#### Step A: Find the Running Container ID
To list all active and inactive containers:
```bash
docker ps -a
```
Locate the `CONTAINER ID` of your `simple-time-rest-api` container.

#### Step B: Stop and Remove the Container
Stop the container gracefully and delete its instance:
```bash
# Stop the container
docker stop <Container_ID>

# Remove the container
docker rm <Container_ID>
```
> [!TIP]
> You don't have to type the full Container ID! Just typing the first 3 or 4 characters is usually enough for Docker to identify it.

#### Step C: Clean up the Image
To see all images stored locally:
```bash
docker images
```
To remove the built image:
```bash
docker rmi <Image_ID>
```
*(Or use `docker rmi simple-time-rest-api` to remove it by its tag)*
