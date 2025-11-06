# RPA Bot Monitoring System

A comprehensive dashboard for monitoring, analyzing, and managing RPA (Robotic Process Automation) bots in real-time. This system provides detailed insights into bot performance, error tracking, and predictive analytics for risk assessment.

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

## 📸 Dashboard Screenshots & Detailed Explanations

### 1. Overview Dashboard
<img width="1836" height="862" alt="Screenshot 2025-11-04 154827" src="https://github.com/user-attachments/assets/214ce9d2-9a3c-4f86-bcd7-2750d5ce29ea" />

**What's Happening in This View:**
- **Top Filter Bar**: Comprehensive filtering options including:
  - Bot Type dropdown for categorizing bots
  - Status selector for filtering by operational state
  - Priority level filter for task importance
  - Owner assignment filter for team management
- **Date Range Control**: Custom date selection (Dec 31, 2022 - Feb 19, 2023)
- **Key Metric Cards**:
  - Total Bots: Real-time counter showing total bots in system
  - Active Bots: Number of currently running bots
  - Success Rate: Overall success percentage
  - Avg Execution Time: Mean processing duration
- **Performance Graph**: Multi-metric timeline showing:
  - Bot activity trends over time
  - Success rate variations
  - Execution time patterns
- **Filter Actions**: Apply/Reset buttons for data refinement

### 2. Analytics Dashboard

<img width="1850" height="858" alt="Screenshot 2025-11-04 150835" src="https://github.com/user-attachments/assets/f241952f-6ad4-47b0-ab0c-d7f27246c82c" />

**What's Happening in This View:**
- **User Selection**: Dropdown showing 'user4' specific analysis
- **Bot Performance Table**: Comprehensive metrics showing:
  - Bot Names (bot13 through bot270)
  - Total Runs: Ranging from 152-416 executions
  - Success Rates: Varying from 65.6% to 95.9%
  - Avg Execution Times: Between 7.37s to 9.65s
  - Error Counts: From 0 to 29 incidents
- **Aggregated Statistics**:
  - Total Runs: 213,570 across all bots
  - Overall Success Rate: 79.9%
  - Average Execution: 5.22 seconds
  - Total Errors: 18,036 incidents

### 3. Error Analysis & Logs

<img width="1902" height="873" alt="Screenshot 2025-11-04 143144" src="https://github.com/user-attachments/assets/a8252be5-bbde-4baa-902b-05cbd75df721" />

**What's Happening in This View:**
- **Error Distribution Statistics**:
  - Failed Tasks: 130 incidents
  - In Progress: 26 ongoing tasks
  - Pending Queue: 636 waiting operations
  - Successful Runs: 138 completions
- **Recent Runs Monitoring**:
  - Bot IDs: bot260, bot698, bot262, etc.
  - Current Status: All showing as "pending"
  - Failure Counts: Ranging from 18-26 failures
  - Timestamp Data: Recent runs from 2023-02-17
- **Real-time Updates**: Live status tracking of bot executions

### 4. Performance Metrics
<img width="1916" height="871" alt="Screenshot 2025-11-04 141447" src="https://github.com/user-attachments/assets/62d20f95-7698-4a0b-ab73-01f15df62167" />


**What's Happening in This View:**
- **Success Rate Trend Graph**:
  - X-axis: Timeline from Jan 2023 to Dec 2023
  - Y-axis: Success rate percentage (0-100%)
  - Line graph showing daily/weekly variations
- **Per-bot Performance Details**:
  - Individual bot metrics (bot1 through bot5)
  - Success rates ranging from 63.4% to 75.4%
  - Execution times varying from 1.31s to 9.85s
- **Historical Trend Analysis**: Year-long performance data visualization

### 5. Risk Analysis Dashboard

<img width="1601" height="823" alt="Screenshot 2025-11-04 182432" src="https://github.com/user-attachments/assets/badd0377-c663-4489-a6ee-c28424f59bf1" />

**What's Happening in This View:**
- **Bot Selection**: Analysis of bot600
- **Risk Assessment Panel**:
  - Risk Level: MEDIUM RISK highlighted
  - Risk Score: 52.0% calculated probability
  - Key Metrics:
    - Success Rate: 98.9% operational success
    - Failure Rate: 1.1% error occurrence
    - Risk Score: 52.0% overall risk level
- **Contributing Factors Analysis**:
  - Moderate failure rate (1.1% of runs)
  - Absolute failure count tracking
  - Historical performance patterns
- **Recommendation Engine**:
  - Performance monitoring suggestions
  - Scheduled maintenance prompts
  - Automated testing implementation advice
- **Performance Visualization**:
  - Bar chart showing:
    - Failure Rate: 1.1%
    - Risk Score: 52.0%
    - Success Rate: 98.9%

## 🚀 Getting Started

[Rest of the README content remains the same...]
