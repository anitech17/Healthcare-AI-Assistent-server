# Healthcare AI Backend

## Overview

This project is the backend for an Agentic AI Healthcare Assistant. It is built using FastAPI and PostgreSQL. The goal of this backend is to handle doctor data, process user inputs, and later integrate AI-driven decision making for healthcare recommendations.

---

## Current Scope (Phase 1)

Right now, the system focuses on:

* Setting up a clean backend architecture
* Connecting FastAPI with PostgreSQL
* Creating and managing doctor data
* Building basic APIs to fetch doctor information

This is the foundation for future AI-driven workflows.

---

## Project Structure

```
app/
├── api/
│   ├── functions/        # Reserved for reusable helper functions (future use)
│   └── routes/           # API route definitions
│       └── health.py     # Health check + test endpoints
│
├── core/
│   └── config.py         # Environment variables and configuration
│
├── db/
│   ├── models.py         # Database models (Doctor table)
│   ├── session.py        # Database connection setup
│   └── seed.py           # Script to insert dummy doctor data
│
├── schemas/              # Pydantic schemas (to be used later)
│
├── main.py               # Entry point of the FastAPI app
```

---

## How the System Works (Current Flow)

### 1. Server Start

When you run the server:

```
uvicorn app.main:app --reload
```

* FastAPI app initializes
* Database connection is established
* Tables are created using SQLAlchemy

---

### 2. Database Connection Flow

* `config.py` loads environment variables from `.env`
* `session.py` creates:

  * Database engine
  * SessionLocal (DB session)
  * Base (for models)

---

### 3. Doctor Table

Defined in `models.py`

Fields:

* id
* name
* specialty
* experience
* latitude
* longitude
* rating
* city

---

### 4. Data Seeding Flow

Run:

```
python -m app.db.seed
```

What happens:

* Connects to DB
* Inserts 20–25 doctors
* Avoids duplicates
* Commits data

---

### 5. API Flow

Example endpoint:

```
GET /all
```

Flow:

* Request hits route (`health.py`)
* DB session is injected
* Query runs:

  ```python
  db.query(Doctor).all()
  ```
* Data returned as response

---

## Environment Setup

### 1. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

### 3. Create `.env` File

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/health_ai
```

---

## PostgreSQL Setup

### Open PostgreSQL

```
psql -U postgres
```

### Create Database

```
CREATE DATABASE health_ai;
```

### List Databases

```
\l
```

### Exit

```
\q
```

---

## Running the Application

### Start Server

```
uvicorn app.main:app --reload
```

### Open Swagger Docs

```
http://127.0.0.1:8000/docs
```

---

## Common Errors & Fixes

### 1. ModuleNotFoundError (app not found)

* Add `__init__.py` files
* Run from project root

### 2. DATABASE_URL is None

* Check `.env`
* Ensure `load_dotenv()` is used

### 3. Database does not exist

* Create DB using PostgreSQL

### 4. sqlalchemy not found

* Activate virtual environment

### 5. NameError (Doctor not defined)

* Import model in route file

---

## What’s Coming Next

Next phase will include:

* Doctor filtering by specialty
* Ranking doctors (rating + distance)
* Symptom → specialty mapping
* AI integration (LLM)
* Multi-agent architecture (LangGraph)

---

## Future System Flow (Planned)

```
User Input
   ↓
AI Symptom Extraction
   ↓
Specialty Mapping
   ↓
Doctor Query
   ↓
Ranking Engine
   ↓
Response
```

---

## Key Design Principles

* Keep AI for understanding, not data filtering
* Use backend for logic and performance
* Build modular services (future agents)
* Keep system scalable from start

---

## Final Note

This is the foundation layer of the system. Once stable, AI and agent-based workflows will be integrated on top of this backend.