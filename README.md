# Z Dating App

This repository contains a minimal prototype for a dating application built with **FastAPI** and **Flutter**. It demonstrates a simple authentication flow using JWT tokens.

## Backend

- **Python 3.10** with [FastAPI](https://fastapi.tiangolo.com)
- Asynchronous PostgreSQL access via `asyncpg`
- User registration and login endpoints
- JWT token generation (access & refresh)

## Frontend

The Flutter project provides only a skeleton at this stage. `lib/main.dart` runs a basic app that can be extended with actual UI screens.

## Running locally

1. Install Python dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Copy `.env` and adjust values as needed.
3. Start the API:
   ```bash
   uvicorn app.main:app --reload
   ```

Flutter code can be launched using the standard `flutter run` command inside the `frontend` directory.

