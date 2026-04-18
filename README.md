# Cloud Task Manager

A lightweight containerized task management backend built with Flask and Docker.
Project Goal

This project was built to practice containerization, REST API development, and cloud-oriented application deployment using Python and Docker.

## Features

- REST API with Flask
- View all tasks
- Create new tasks
- Dockerized for consistent local deployment

## Tech Stack

- Python
- Flask
- Docker

## API Endpoints

### GET /
Returns the service status.

### GET /tasks
Returns all tasks.

### POST /tasks
Creates a new task.

### Run locally
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py

### Run with Docker
docker build -t cloud-task-manager .
docker run -p 5000:5000 cloud-task-manager
