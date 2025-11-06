# RPA Bot Monitoring System

A full-stack analytics dashboard for monitoring and analyzing RPA bot performance. Built with React, Flask, and Machine Learning.

## Features

- Real-time bot performance monitoring
- Risk analysis using Random Forest model
- User-specific bot filtering
- Performance metrics visualization
- Anomaly detection
- Success rate tracking
- Execution time analysis

## Tech Stack

### Frontend
- React with Material-UI
- Recharts for visualizations
- Vite for build tooling

### Backend
- Flask REST API
- Pandas for data processing
- Scikit-learn for ML models
- SQLAlchemy for database

## Setup

1. Backend Setup:
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

2. Frontend Setup:
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

- `/backend` - Flask server and ML models
- `/frontend` - React application
- `RPA_Bot_Data_Synthetic_800_Rows.csv` - Sample data
- `bot_monitoring.ipynb` - Jupyter notebook for analysis

## API Endpoints

- `/api/analytics/dashboard` - Main analytics dashboard data
- `/api/summary` - Bot performance summary
- `/api/analysis/<bot_id>` - Individual bot analysis
- `/api/errors` - Error tracking
- `/api/performance` - Performance metrics

## Contributors
- ARYA BARAI (@ARYABARAI30123)