# 2Care Voice AI Agent Architecture

## System Flow

User
↓
Frontend UI
↓
FastAPI Backend
↓
Language Detection
↓
AI Reasoning Engine
↓
Tool Execution Layer
↓
Appointment Scheduler
↓
Persistent Memory
↓
Response Generator
↓
Frontend Response

---

## Components

### Frontend
- HTML
- CSS
- JavaScript
- Sends API requests
- Displays AI responses

### FastAPI Backend
- Handles API routes
- Processes requests
- Returns JSON responses

### Language Detection
- Detects user language
- Supports multilingual conversations

### AI Reasoning Engine
- Extracts:
  - Intent
  - Doctor type
  - Slot
  - Patient name

### Tool Execution Layer
- Executes appointment actions
- Booking
- Cancellation
- Rescheduling

### Scheduler
- Manages appointment slots
- Prevents double booking

### Memory System
- Stores patient preferences
- Saves booking history

### Response Generator
- Generates human-like responses

### Voice Services
- Speech-to-Text
- Text-to-Speech

### Latency Logger
- Tracks API response time