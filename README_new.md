# RPA Bot Monitoring System

A comprehensive dashboard for monitoring, analyzing, and managing RPA (Robotic Process Automation) bots in real-time. This system provides detailed insights into bot performance, error tracking, and predictive analytics for risk assessment.

## 📊 Features & Dashboard Pages

### 1. Overview Dashboard
![Overview Dashboard](screenshots/overview.png)

The main dashboard provides high-level metrics including:
- Total Bots: Real-time count of all bots in the system
- Active Bots: Number of currently running bots
- Success Rate: Overall success percentage of bot executions
- Average Execution Time: Mean execution duration across all bots
- Bot Metrics Over Time: Interactive timeline visualization

### 2. Analytics Dashboard
![Analytics Dashboard](screenshots/analytics.png)

Detailed analytics for each bot with metrics such as:
- Per-bot performance details
- Success rates
- Total runs
- Average execution times
- Error counts
- Bot-specific trends and patterns

**Key Performance Indicators (KPIs):**
- Total Runs: 213,570
- Overall Success Rate: 79.9%
- Average Execution Time: 5.22s
- Total Errors: 18,036

### 3. Performance Metrics
![Performance Dashboard](screenshots/performance.png)

Detailed performance tracking including:
- Success Rate Trend Analysis
- Daily Performance Trends
- Per-bot Performance Details
- Historical Performance Data

The system tracks various performance metrics including:
- Bot execution times
- Success/failure rates
- Resource utilization
- Execution trends over time

### 4. Error Analysis & Logs
![Error Analysis](screenshots/errors.png)

Comprehensive error tracking and analysis:
- Failure by Status Distribution:
  - Failed: 130
  - In Progress: 26
  - Pending: 636
  - Successfully Ran: 138
- Recent Runs Monitoring
- Detailed Error Logs
- Error Pattern Analysis

### 5. Risk Analysis & Predictions
![Risk Analysis](screenshots/risk.png)

Advanced risk assessment and predictive analytics:
- Risk Score Calculation
- Anomaly Detection
- Predictive Maintenance
- Performance Forecasting

**Example Risk Analysis (bot600):**
- Risk Level: MEDIUM RISK
- Risk Score: 52.0%
- Key Contributing Factors:
  - Moderate failure rate (1.1% of runs failed)
  - Moderate absolute failure count
- Performance Metrics:
  - Success Rate: 98.9%
  - Failure Rate: 1.1%
  - Risk Score: 52.0%

## 🤖 Machine Learning Model Performance

The system uses a Random Forest model for risk prediction and anomaly detection.

### Model Evaluation Metrics

| Metric | Score |
|--------|--------|
| Accuracy | 0.97 |
| Precision | 0.886 |
| Recall (Sensitivity) | 0.975 |
| Specificity | 0.969 |
| F1 Score | 0.929 |
| ROC-AUC | 0.997 |
| Negative Predictive Value | 0.994 |

### Confusion Matrix

| | Predicted Negative | Predicted Positive |
|-----------------|-------------------|-------------------|
| Actual Negative | 155 | 5 |
| Actual Positive | 1 | 39 |

### Per-Class Metrics

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Low Risk (0) | 0.994 | 0.969 | 0.981 | 160 |
| High Risk (1) | 0.886 | 0.975 | 0.929 | 40 |

## 🚀 Getting Started

### Prerequisites
- Python 3.12.6
- Node.js (Latest LTS version)
- npm
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/ARYABARAI30123/RPA-Bot-Monitoring-System.git
cd RPA-Bot-Monitoring-System
```

2. Set up the backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

3. Set up the frontend
```bash
cd frontend
npm install
npm run dev
```

The application will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000

## 📋 System Requirements
- Windows/Linux/MacOS
- Minimum 4GB RAM
- Python 3.12+
- Node.js 14+

## 🛠️ Technologies Used
- **Frontend**: React, Material-UI, Recharts
- **Backend**: Flask, Python
- **Database**: SQLite
- **ML**: scikit-learn, pandas, numpy
- **Real-time Processing**: WebSocket

## 📈 Performance Insights
The system provides comprehensive monitoring and analysis capabilities:
- Real-time bot monitoring
- Historical performance analysis
- Predictive maintenance
- Risk assessment
- Error pattern detection
- Resource utilization tracking

## 🔒 Security Features
- Secure API endpoints
- Data encryption
- User authentication
- Role-based access control
- Audit logging

## API Endpoints

- `/api/analytics/dashboard` - Main analytics dashboard data
- `/api/summary` - Bot performance summary
- `/api/analysis/<bot_id>` - Individual bot analysis
- `/api/errors` - Error tracking
- `/api/performance` - Performance metrics

## Project Structure

```
RPA-Bot-Monitoring-System/
├── backend/
│   ├── database/
│   │   ├── models.py
│   │   └── database.py
│   ├── analytics.py
│   ├── app.py
│   ├── ml_utils.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   └── package.json
└── README.md
```

## Contributors
- ARYA BARAI (@ARYABARAI30123)