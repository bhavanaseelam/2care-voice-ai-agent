# 2Care Voice AI Agent

An AI-powered multilingual healthcare voice assistant built using FastAPI, Python, and frontend technologies.

The system can:
- Book appointments
- Cancel appointments
- Reschedule appointments
- Detect multiple languages
- Support speech-to-text
- Generate AI-based responses
- Provide voice responses
- Store patient memory
- Track API latency
- Display real-time frontend interaction

---

# Features

## AI Reasoning Engine
- Intent detection
- Doctor type extraction
- Slot extraction
- Patient memory handling

## Appointment Scheduler
- Appointment booking
- Double booking prevention
- Rescheduling
- Cancellation

## Multilingual Support
- English
- Hindi
- Telugu
- Tamil
- Mixed language support

## Voice AI
- Speech-to-text
- Text-to-speech responses

## FastAPI Backend
- REST API endpoints
- Swagger API documentation

## Frontend
- Real-time AI interaction
- Response visualization
- Latency display

## Latency Monitoring
- API response timing
- Performance logging

---

# Tech Stack

## Backend
- Python
- FastAPI

## Frontend
- HTML
- CSS
- JavaScript

## AI Logic
- Regex-based reasoning engine
- Rule-based intent detection

## Voice Services
- SpeechRecognition
- pyttsx3

---

# Project Structure

```text
2care-voice-ai-agent/
│
├── backend/
│   ├── agent/
│   ├── memory/
│   ├── scheduler/
│   ├── services/
│   ├── main.py
│
├── frontend/
│   ├── index.html
│
├── docs/
│   ├── architecture.md
│
├── requirements.txt
├── README.md
```

---

# API Endpoints

## Home Endpoint

```http
GET /
```

## Voice AI Endpoint

```http
POST /voice-agent
```

## Get Appointments

```http
GET /appointments
```

---

# How to Run Project

## Step 1

Clone repository

```bash
git clone https://github.com/bhavanaseelam/2care-voice-ai-agent.git
```

## Step 2

Open backend folder

```bash
cd backend
```

## Step 3

Create virtual environment

```bash
python -m venv venv
```

## Step 4

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 5

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6

Run FastAPI server

```bash
uvicorn main:app --reload
```

---

## Step 7

Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Preview

The frontend provides:
- Message input
- Real-time AI responses
- Latency monitoring
- Appointment booking interaction

---

# Future Improvements

- Real LLM integration
- Database integration
- WhatsApp reminders
- Cloud deployment
- Authentication system
- Advanced voice assistant

---

# Author

Bhavana Seelam