# 🎯 IntentScore API

A sophisticated **Lead Intent Scoring System** that leverages AI to analyze customer leads and predict their purchase intent based on product offers. Built with Django REST Framework and powered by Google's Gemini AI and Transformers.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-4.2.7-green)
![AI](https://img.shields.io/badge/AI-Gemini%20%26%20Transformers-purple)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

## 🚀 Features

- **🤖 AI-Powered Intent Analysis**: Uses Google Gemini AI for intelligent lead intent prediction
- **📊 Multi-Model Scoring**: Combines AI analysis with transformer models for accurate scoring
- **📁 CSV Lead Management**: Upload and process lead data via CSV files
- **🎯 Product Offer Matching**: Match leads against specific product offerings
- **📈 Intent Classification**: Categorizes leads as High, Medium, or Low intent
- **📋 Results Export**: Export scored results back to CSV format
- **🔄 RESTful API**: Complete REST API for integration with other systems
- **🐳 Docker Ready**: Containerized for easy deployment

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7 + Django REST Framework
- **AI/ML**: 
  - Google Generative AI (Gemini 1.5 Flash)
  - Transformers 4.35.0 + PyTorch 2.2.0
- **Data Processing**: Pandas 2.0.3
- **Database**: SQLite (default), PostgreSQL compatible
- **Deployment**: Docker + Gunicorn + WhiteNoise

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/product/offer/` | Create a new product offer |
| `POST` | `/api/leads/upload/` | Upload leads via CSV file |
| `POST` | `/api/score/` | Score leads against product offers |
| `GET` | `/api/results/` | Get scoring results |
| `GET` | `/api/csv/` | Export results to CSV |

## 🏗️ Project Structure

```
IntentScore/
├── IntentScore/                 # Main Django project
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL routing
│   └── wsgi.py                 # WSGI application
├── IntentScoreAPI/             # Main API application
│   ├── models.py               # Data models (Lead, ProductOffer)
│   ├── views.py                # API endpoints
│   ├── serializers.py          # Data serializers
│   ├── services.py             # Business logic
│   ├── ai_integration.py       # AI/ML integration
│   └── urls.py                 # API routing
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── compose.yaml               # Docker Compose
└── manage.py                  # Django management
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Docker (optional)
- Google Gemini API Key

### 1. Clone Repository
```bash
git clone https://github.com/skp3214/IntentScore.git
cd IntentScore
```

### 2. Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secret_key_here
DEBUG=True
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## 🐳 Docker Deployment

### Build and Run with Docker Compose
```bash
# Build and start containers
docker-compose up --build

# Run in background
docker-compose up -d --build
```

### Manual Docker Build
```bash
# Build image
docker build -t intentscore .

# Run container
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key intentscore
```

## 📊 Usage Examples

### 1. Create Product Offer
```bash
curl -X POST http://localhost:8000/product/offer/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AI Analytics Platform",
    "value_props": ["Advanced Analytics", "Real-time Insights"],
    "ideal_use_cases": ["Data Analysis", "Business Intelligence"]
  }'
```

### 2. Upload Leads CSV
```bash
curl -X POST http://localhost:8000/leads/upload/ \
  -F "csv_file=@leads.csv"
```

### 3. Score Leads
```bash
curl -X POST http://localhost:8000/score/ \
  -H "Content-Type: application/json"
```
*Note: The scoring endpoint automatically uses the most recently created product offer and scores all uploaded leads against it.*

### 4. Get Results
```bash
curl http://localhost:8000/results/
```

## 📁 CSV Format

### Input Leads CSV Format:
```csv
name,role,company,industry,location,linkedin_bio
John Doe,Data Scientist,TechCorp,Technology,San Francisco,Passionate about machine learning and data analytics
Jane Smith,Marketing Manager,RetailCo,Retail,New York,Digital marketing expert with focus on customer analytics
```

### Output Results CSV Format:
```csv
name,role,company,industry,location,linkedin_bio,intent,score,reasoning
John Doe,Data Scientist,TechCorp,Technology,San Francisco,Passionate about machine learning...,High,85,Strong background in data science aligns perfectly with AI analytics platform...
```

## 🔧 Configuration

### AI Models Configuration
The system uses two AI approaches:
- **Gemini AI**: For intelligent reasoning and intent analysis
- **Transformers**: For sentiment and text classification

### Scoring Algorithm
- **High Intent**: 70-100 points
- **Medium Intent**: 40-69 points  
- **Low Intent**: 0-39 points

Scoring considers:
- Job role relevance
- Industry alignment
- LinkedIn bio analysis
- Company profile
- Location factors
