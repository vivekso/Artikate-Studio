# Mini Decision Engine API

A Django-based rule evaluation engine that accepts structured input, applies configurable rules, and returns deterministic decisions with explanations.

---

## Features

- Rule-based evaluation with weighted scoring
- Mandatory hard-reject rules
- Deterministic output for the same input
- State persistence using SQLite
- Safe, explainable, and extendable

---

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd decision_engine
```

## Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

## Install dependencies:  
```bash
pip install -r requirements.txt
```
## Apply migrations:
```bash
python manage.py migrate
```
## Run the server:

```bash
python manage.py runserver
```
## API Endpoints
## POST /evaluate

## Request Body
```bash
{
  "user_id": "abc123",
  "attributes": {
    "age": 29,
    "country": "IN",
    "account_age_days": 180,
    "monthly_volume": 75000,
    "kyc_verified": true
  }
}
```
## Response

```bash
{
  "user_id": "abc123",
  "attributes": {
    "age": 29,
    "country": "IN",
    "account_age_days": 180,
    "monthly_volume": 75000,
    "kyc_verified": true
  }
}
```

