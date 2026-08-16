# 🩺 Healthcare AI Assistant — Backend API

The backend service for an **Agentic AI Healthcare Assistant** — built with **FastAPI** and **PostgreSQL**. Handles doctor data today, with AI-driven symptom-to-specialist recommendations planned as the next phase.

---

## 📖 Overview

This service is the foundation layer for a healthcare assistant that will eventually take a user's symptoms, understand them with an LLM, and recommend the right doctor. Phase 1 (this repo, current state) focuses on getting the backend architecture, database, and core doctor-data APIs production-ready before AI reasoning is layered on top.

**Current Scope — Phase 1**

- 🏗️ Clean, modular backend architecture
- 🐘 FastAPI connected to PostgreSQL via SQLAlchemy
- 👨‍⚕️ Doctor data model, seeding, and retrieval
- 🌱 Dummy data seeding for local development and testing

---

## ✨ Features

- ⚡ **FastAPI** app with auto-generated Swagger/OpenAPI docs
- 🐘 **PostgreSQL** persistence via SQLAlchemy engine + session management
- 👨‍⚕️ **Doctor model** — name, specialty, experience, location (lat/long), rating, and city
- 🌱 **Seed script** — inserts 20–25 sample doctors, duplicate-safe, for local dev
- 🧩 **Modular structure** — routes, config, db, and schemas kept in separate layers, ready to extend
- 🔮 **AI-ready architecture** — designed from the start to have LLM/agent workflows layered on top without a rewrite

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Config | python-dotenv |
| Server | Uvicorn |

---

## 📁 Project Structure

```
app/
├── api/
│   ├── functions/          # Reserved for reusable helper functions (future use)
│   └── routes/
│       └── health.py       # Health check + doctor-data endpoints
│
├── core/
│   └── config.py            # Environment variables and configuration
│
├── db/
│   ├── models.py             # Database models (Doctor table)
│   ├── session.py            # Database connection setup
│   └── seed.py                # Script to insert dummy doctor data
│
├── schemas/                  # Pydantic schemas (to be used later)
│
└── main.py                   # Entry point of the FastAPI app
```

---

## 🔄 How It Works

### 1️⃣ Server Start

```bash
uvicorn app.main:app --reload
```

- FastAPI app initializes
- Database connection is established
- Tables are created via SQLAlchemy

### 2️⃣ Database Connection Flow

- `config.py` loads environment variables from `.env`
- `session.py` creates the database engine, `SessionLocal`, and the declarative `Base` for models

### 3️⃣ Doctor Table

Defined in `models.py`, with fields:

`id` · `name` · `specialty` · `experience` · `latitude` · `longitude` · `rating` · `city`

### 4️⃣ Data Seeding Flow

```bash
python -m app.db.seed
```

Connects to the DB, inserts 20–25 sample doctors, skips duplicates, and commits.

### 5️⃣ API Request Flow

Example: `GET /all`

```
Request → route (health.py) → DB session injected → db.query(Doctor).all() → JSON response
```

---

## ⚡ Getting Started

### 1️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

### 3️⃣ Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/health_ai
```

### 4️⃣ Set up PostgreSQL

```bash
psql -U postgres
CREATE DATABASE health_ai;
\l    # list databases
\q    # exit
```

### 5️⃣ Seed sample data

```bash
python -m app.db.seed
```

### 6️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000` 🎉

---

## 📚 API Documentation

- 🟢 **Swagger UI:** `http://127.0.0.1:8000/docs`

---

## 🧯 Troubleshooting

| Issue | Fix |
|---|---|
| `ModuleNotFoundError` (app not found) | Add `__init__.py` files; run from project root |
| `DATABASE_URL is None` | Check `.env` exists and `load_dotenv()` is called |
| Database does not exist | Create it in PostgreSQL first (`CREATE DATABASE health_ai;`) |
| `sqlalchemy not found` | Activate the virtual environment |
| `NameError: Doctor not defined` | Import the model in the route file |

---

## 🗺️ Roadmap

- [ ] Doctor filtering by specialty
- [ ] Ranking doctors by rating + distance
- [ ] Symptom → specialty mapping
- [ ] LLM integration for symptom understanding
- [ ] Multi-agent architecture with LangGraph

**Planned system flow:**

```
User Input → AI Symptom Extraction → Specialty Mapping → Doctor Query → Ranking Engine → Response
```

---

## 🧠 Design Principles

- 🤖 Use AI for *understanding*, not for data filtering
- ⚙️ Keep the backend responsible for logic and performance
- 🧩 Build modular services so future agents plug in cleanly
- 📈 Design for scale from day one

---

## 📄 Note

This is the foundation layer of the system. AI and agent-based workflows will be integrated on top of this backend in the next phase.
