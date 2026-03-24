# 🌦 Weather App API — Phase 1 (Brazil)

A FastAPI backend with full **CRUD**, OpenWeatherMap integration, YouTube & Google Maps enrichment, and JSON export. Scoped to Brazil in Phase 1.

---

## Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Framework   | FastAPI 0.111           |
| Database    | MySQL 8 + SQLAlchemy 2  |
| HTTP client | httpx (async)           |
| Validation  | Pydantic v2             |
| Fuzzy match | thefuzz                 |

---

## Quick Start

### 1 – Clone & install

```bash
git clone <repo>
cd weather-app
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2 – Configure environment

```bash
cp .env.example .env
# Edit .env and fill in all keys (see below)
```

### 3 – Create the MySQL database

```sql
CREATE DATABASE weatherapp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

SQLAlchemy will create all tables automatically on first startup.

### 4 – Run

```bash
uvicorn app.main:app --reload
```

Open **http://localhost:8000/docs** for the interactive Swagger UI.

---

## API Keys Required

| Service         | Where to get it                              | Env var                |
|-----------------|----------------------------------------------|------------------------|
| OpenWeatherMap  | https://openweathermap.org/api               | `OPENWEATHER_API_KEY`  |
| YouTube Data v3 | https://console.cloud.google.com             | `YOUTUBE_API_KEY`      |
| Google Maps     | https://console.cloud.google.com             | `GOOGLE_MAPS_API_KEY`  |

> **Note:** Historical weather (past dates) requires the **One Call API 3.0** subscription on OpenWeatherMap. Free-tier keys will receive a graceful `N/A` message for those days instead of crashing.

---

## Endpoints at a Glance

### Weather (CRUD)

| Method   | Path                       | Description                           |
|----------|----------------------------|---------------------------------------|
| `GET`    | `/weather/current`         | Live weather — not stored             |
| `POST`   | `/weather/queries`         | **CREATE** query + fetch + store      |
| `GET`    | `/weather/queries`         | **READ** all queries (paginated)      |
| `GET`    | `/weather/queries/{id}`    | **READ** single query with records    |
| `PATCH`  | `/weather/queries/{id}`    | **UPDATE** query, re-fetches data     |
| `DELETE` | `/weather/queries/{id}`    | **DELETE** query and records          |

### Export

| Method | Path                       | Description                  |
|--------|----------------------------|------------------------------|
| `GET`  | `/export/queries`          | Export all queries as JSON   |
| `GET`  | `/export/queries/{id}`     | Export one query as JSON     |

### Integrations

| Method | Path                      | Description                     |
|--------|---------------------------|---------------------------------|
| `GET`  | `/integrations/youtube`   | YouTube videos for a city       |
| `GET`  | `/integrations/maps`      | Google Maps data for a city     |

---

## Example Requests

```bash
# Current weather in Recife
curl "http://localhost:8000/weather/current?location=Recife"

# Create a 7-day query for Fortaleza
curl -X POST http://localhost:8000/weather/queries \
  -H "Content-Type: application/json" \
  -d '{"location":"Fortaleza","date_start":"2024-06-01","date_end":"2024-06-07"}'

# Export query #1 as JSON
curl "http://localhost:8000/export/queries/1?format=json" -o query1.json

# YouTube videos for Salvador
curl "http://localhost:8000/integrations/youtube?city=Salvador"

# Google Maps data for Manaus
curl "http://localhost:8000/integrations/maps?city=Manaus"
```

---
