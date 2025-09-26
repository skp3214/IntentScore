# 🎯 IntentScore API

A sophisticated **Lead Intent Scoring System** that leverages AI to analyze customer leads and predict their purchase intent based on product offers. Built with Django REST Framework and powered by Google's Gemini AI for intelligent lead scoring and classification.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-4.2.7-green)
![AI](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-purple)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![API](https://img.shields.io/badge/API-REST-orange)

## 🚀 Features

- **🤖 AI-Powered Intent Analysis**: Uses Google Gemini 2.0 Flash for intelligent lead intent prediction
- **📊 Hybrid Scoring System**: Combines rule-based scoring with AI analysis for accurate results
- **📁 CSV Lead Management**: Upload and process lead data via CSV files
- **🎯 Product Offer Matching**: Match leads against specific product offerings with detailed analysis
- **📈 Intent Classification**: Categorizes leads as High (70-100), Medium (40-69), or Low (0-39) intent
- **📋 Results Export**: Export scored results back to CSV format with detailed reasoning
- **🔄 RESTful API**: Complete REST API for integration with other systems
- **🐳 Docker Ready**: Containerized for easy deployment and scaling

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7 + Django REST Framework 3.14.0
- **AI/ML**: Google Generative AI (Gemini 2.0 Flash)
- **Data Processing**: Pandas 2.0.3 + NumPy 1.24.4
- **Database**: SQLite (default), PostgreSQL compatible
- **Deployment**: Docker + Gunicorn + WhiteNoise
- **Environment**: Python-dotenv for configuration management

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `product/offer/` | Create a new product offer |
| `POST` | `leads/upload/` | Upload leads via CSV file |
| `POST` | `score/` | Score leads against product offers |
| `GET` | `results/` | Get scoring results |
| `GET` | `csv/` | Export results to CSV |

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

## 📋 API Endpoints

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| `POST` | `product/offer/` | Create a new product offer | ✅ |
| `POST` | `leads/upload/` | Upload leads via CSV file | ✅ |
| `POST` | `score/` | Score leads against product offers | ✅ |
| `GET` | `results/` | Get all leads with their scores | ✅ |
| `GET` | `csv/` | Export results to CSV | ✅ |

## 🏗️ Project Structure

```
IntentScore/
├── IntentScore/                 # Main Django project
│   ├── settings.py             # Django settings & configuration
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI application entry
│   └── asgi.py                 # ASGI application entry
├── IntentScoreAPI/             # Core API application
│   ├── models.py               # Data models (Lead, ProductOffer, ScoringResult)
│   ├── views.py                # API endpoints & business logic
│   ├── serializers.py          # DRF serializers for data validation
│   ├── services.py             # Lead scoring service & rule engine
│   ├── ai_integration.py       # Gemini AI integration layer
│   ├── urls.py                 # API URL routing
│   └── migrations/             # Database migration files
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker container configuration
├── compose.yaml               # Docker Compose orchestration
├── db.sqlite3                 # SQLite database (development)
├── leads.csv                  # Sample lead data
└── manage.py                  # Django management commands
```

---

## 🚀 Setup & Installation

### Prerequisites

- **Python 3.10+** (Recommended: 3.12)
- **pip** package manager
- **Git** for version control
- **Docker** (optional, for containerized deployment)
- **Google Gemini API Key** ([Get one here](https://makersuite.google.com/app/apikey))

### Method 1: Local Development Setup

#### 1. Clone Repository
```bash
git clone https://github.com/skp3214/IntentScore.git
cd IntentScore
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (Command Prompt):
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional (defaults provided)
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

#### 5. Database Setup
```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate

```

#### 6. Run Development Server
```bash
python manage.py runserver
```

🎉 **Success!** API is now running at `http://localhost:8000`

### Method 2: Docker Deployment

#### Quick Start with Docker Compose
```bash
# Clone repository
git clone https://github.com/skp3214/IntentScore.git
cd IntentScore

# Create .env file with your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Build and run containers
docker-compose up --build

# Run in background (detached mode)
docker-compose up -d --build
```

#### Manual Docker Build
```bash
# Build Docker image
docker build -t intentscore-api .

# Run container
docker run -p 8000:8000 -e GEMINI_API_KEY=your_api_key_here intentscore-api
```

### Method 3: Production Deployment

#### Environment Variables for Production
```env
SECRET_KEY=your_production_secret_key_here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com
GEMINI_API_KEY=your_gemini_api_key_here
```

#### Using Gunicorn (Production WSGI Server)
```bash
# Install gunicorn (already in requirements.txt)
pip install gunicorn

# Run with Gunicorn
gunicorn IntentScore.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

---

## 🔧 API Usage Examples

### Base URL
- **Local Development**: `http://localhost:8000`
- **Docker**: `http://localhost:8000`
- **Production**: `https://your-domain.com`

### 1. Create Product Offer

Create a product offer that leads will be scored against.

**cURL Example:**
```bash
curl -X POST http://localhost:8000/product/offer/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AI Analytics Platform Pro",
    "value_props": [
      "Advanced Machine Learning Analytics",
      "Real-time Data Processing",
      "Predictive Business Intelligence",
      "Custom Dashboard Creation"
    ],
    "ideal_use_cases": [
      "Enterprise Data Analysis",
      "Business Intelligence Reporting",
      "Customer Behavior Analytics",
      "Sales Performance Optimization"
    ]
  }'
```

**Postman Collection:**
```json
{
  "name": "Create Product Offer",
  "request": {
    "method": "POST",
    "header": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "body": {
      "mode": "raw",
      "raw": "{\n  \"name\": \"AI Analytics Platform Pro\",\n  \"value_props\": [\n    \"Advanced Machine Learning Analytics\",\n    \"Real-time Data Processing\",\n    \"Predictive Business Intelligence\"\n  ],\n  \"ideal_use_cases\": [\n    \"Enterprise Data Analysis\",\n    \"Business Intelligence Reporting\"\n  ]\n}"
    },
    "url": {
      "raw": "http://localhost:8000/product/offer/",
      "protocol": "http",
      "host": ["localhost"],
      "port": "8000",
      "path": ["product", "offer", ""]
    }
  }
}
```

**Expected Response:**
```json
{
  "id": 1,
  "name": "AI Analytics Platform Pro",
  "value_props": [
    "Advanced Machine Learning Analytics",
    "Real-time Data Processing",
    "Predictive Business Intelligence",
    "Custom Dashboard Creation"
  ],
  "ideal_use_cases": [
    "Enterprise Data Analysis",
    "Business Intelligence Reporting",
    "Customer Behavior Analytics",
    "Sales Performance Optimization"
  ],
  "created_at": "2025-09-26T10:30:00Z"
}
```

### 2. Upload Leads via CSV

Upload lead data from a CSV file for analysis.

**cURL Example:**
```bash
curl -X POST http://localhost:8000/leads/upload/ \
  -F "csv_file=@leads.csv"
```

**Postman Setup:**
1. Select `POST` method
2. URL: `http://localhost:8000/leads/upload/`
3. Go to `Body` tab
4. Select `form-data`
5. Add key: `csv_file` (select File type)
6. Upload your CSV file

**Sample CSV Format (leads.csv):**
```csv
name,role,company,industry,location,linkedin_bio
John Doe,Senior Data Scientist,TechCorp Analytics,Technology,San Francisco,Passionate about machine learning and predictive analytics. 10+ years experience in data science and AI implementation.
Jane Smith,Marketing Director,RetailMax Inc,E-commerce,New York,Digital marketing leader with expertise in customer analytics and growth strategies. Focus on data-driven marketing decisions.
Mike Johnson,Business Analyst,FinanceFirst,Financial Services,Chicago,Business intelligence specialist with strong background in financial data analysis and reporting automation.
Sarah Wilson,IT Manager,HealthTech Solutions,Healthcare,Boston,Healthcare IT professional managing data systems and analytics infrastructure for patient care optimization.
David Brown,Operations Manager,Manufacturing Plus,Manufacturing,Detroit,Operations expert focused on process optimization and efficiency through data analytics and automation.
```

**Expected Response:**
```json
{
  "message": "Successfully uploaded 5 leads"
}
```

### 3. Score Leads

Analyze and score all uploaded leads against the latest product offer.

**cURL Example:**
```bash
curl -X POST http://localhost:8000/score/ \
  -H "Content-Type: application/json"
```

**Postman Setup:**
1. Select `POST` method
2. URL: `http://localhost:8000/score/`
3. Header: `Content-Type: application/json`
4. No body required (uses latest offer and all uploaded leads)

**Expected Response:**
```json
[
    {
        "name": "John Smith",
        "role": "CEO",
        "company": "TechFlow Inc.",
        "industry": "SaaS",
        "location": "San Francisco",
        "intent": "High",
        "score": 100,
        "reasoning": "John Smith's role as CEO of a SaaS company in San Francisco, coupled with his LinkedIn bio highlighting B2B SaaS experience and focus on growth, strongly aligns with the ideal customer profile and value propositions of the AI-powered sales engagement platform."
    },
    {
        "name": "Sarah Chen",
        "role": "Head of Marketing",
        "company": "DataDrive Solutions",
        "industry": "Technology",
        "location": "New York",
        "intent": "High",
        "score": 100,
        "reasoning": "Sarah's role, industry, and LinkedIn bio all strongly align with the ideal use cases and value propositions of the AI-powered sales engagement platform, indicating a high likelihood of needing and benefiting from the product."
    }
]
```

### 4. Get Scoring Results

Retrieve all leads with their scoring results and analysis.

**cURL Example:**
```bash
curl http://localhost:8000/results/
```

**Expected Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "role": "Senior Data Scientist",
    "company": "TechCorp Analytics",
    "industry": "Technology",
    "location": "San Francisco",
    "linkedin_bio": "Passionate about machine learning and predictive analytics. 10+ years experience in data science and AI implementation.",
    "intent": "High",
    "score": 85,
    "reasoning": "Strong technical background in data science and machine learning aligns perfectly with AI Analytics Platform Pro. Senior role indicates decision-making authority.",
    "created_at": "2025-09-26T11:15:30Z"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "role": "Marketing Director", 
    "company": "RetailMax Inc",
    "industry": "E-commerce",
    "location": "New York",
    "linkedin_bio": "Digital marketing leader with expertise in customer analytics and growth strategies. Focus on data-driven marketing decisions.",
    "intent": "Medium",
    "score": 65,
    "reasoning": "Marketing director with analytics focus shows good fit. However, different industry focus may require more nurturing.",
    "created_at": "2025-09-26T11:15:30Z"
  }
]
```

### 5. Export Results to CSV

Download scoring results as a CSV file.

**cURL Example:**
```bash
curl http://localhost:8000/csv/ \
  --output scored_leads.csv
```

**Postman Setup:**
1. Select `GET` method
2. URL: `http://localhost:8000/csv/`
3. Click `Send and Download` to save the CSV file

**Sample Output CSV (lead_scores.csv):**
```csv
Name,Role,Company,Industry,Location,Intent,Score,Reasoning
John Doe,Senior Data Scientist,TechCorp Analytics,Technology,San Francisco,High,85,"Strong technical background in data science and machine learning aligns perfectly with AI Analytics Platform Pro. Senior role indicates decision-making authority."
Jane Smith,Marketing Director,RetailMax Inc,E-commerce,New York,Medium,65,"Marketing director with analytics focus shows good fit. However, different industry focus may require more nurturing."
```

---

## 🧠 Scoring Logic & AI Prompts

### Hybrid Scoring System

The IntentScore API uses a **hybrid scoring approach** combining rule-based logic with AI-powered analysis for accurate lead intent prediction.

#### 📊 Total Score Calculation

```
Total Score = Rule-Based Score (0-50) + AI Score (0-50) = 0-100
```

### Rule-Based Scoring Engine

The rule-based component analyzes structured lead data using predefined business rules:

#### 1. **Role Relevance Scoring (0-20 points)**

```python
decision_maker_roles = [
    'ceo', 'cfo', 'cto', 'cmo', 'coo', 'president', 
    'vp', 'vice president', 'director', 'head of', 
    'manager', 'founder', 'owner'
]

influencer_roles = [
    'specialist', 'analyst', 'coordinator', 
    'assistant', 'associate'
]

# Scoring Logic:
# Decision Maker Role: +20 points
# Influencer Role: +10 points  
# Other Roles: +0 points
```

**Examples:**
- ✅ "CEO" or "VP of Sales" → **20 points**
- ⚡ "Data Analyst" or "Marketing Specialist" → **10 points**
- ❌ "Intern" or "Student" → **0 points**

#### 2. **Industry Alignment Scoring (0-20 points)**

```python
high_value_industries = ['saas', 'tech', 'technology', 'software']
medium_value_industries = ['business', 'services', 'consulting']

# Scoring Logic:
# High-value Industry Match: +20 points
# Medium-value Industry Match: +10 points
# No Match: +0 points
```

**Examples:**
- ✅ "SaaS" or "Technology" → **20 points**
- ⚡ "Business Services" → **10 points**
- ❌ "Non-profit" → **0 points**

#### 3. **Data Completeness Scoring (0-10 points)**

```python
required_fields = ['name', 'role', 'company', 'industry', 'location']

# Scoring Logic:
# All Required Fields Complete: +10 points
# Missing Fields: +0 points
```

### AI-Powered Analysis (Gemini 2.0 Flash)

The AI component performs sophisticated intent analysis using Google's Gemini 2.0 Flash model:

#### 🤖 AI Prompt Template

```python
def _build_prompt(self, lead_data, offer_data):
    return f"""
    Analyze the buying intent of this prospect for the given product offer.
    
    PRODUCT OFFER:
    - Name: {offer_data.get('name', 'N/A')}
    - Value Propositions: {', '.join(offer_data.get('value_props', []))}
    - Ideal Use Cases: {', '.join(offer_data.get('ideal_use_cases', []))}
    
    PROSPECT DATA:
    - Name: {lead_data.get('name', 'N/A')}
    - Role: {lead_data.get('role', 'N/A')}
    - Company: {lead_data.get('company', 'N/A')}
    - Industry: {lead_data.get('industry', 'N/A')}
    - Location: {lead_data.get('location', 'N/A')}
    - LinkedIn Bio: {lead_data.get('linkedin_bio', 'N/A')}
    
    Classify the buying intent as High, Medium, or Low and provide a brief reasoning (1-2 sentences).
    
    Respond in exactly this format:
    Intent: [High/Medium/Low]
    Reasoning: [1-2 sentence explanation]
    """
```

#### 🎯 AI Scoring Logic

```python
ai_score_mapping = {
    'High': 50,    # Strong intent signals
    'Medium': 30,  # Moderate intent signals  
    'Low': 10      # Weak intent signals
}
```

#### Sample AI Analysis

**Input:**
- **Lead**: Senior Data Scientist at TechCorp Analytics
- **Bio**: "Passionate about machine learning and predictive analytics. 10+ years experience in data science and AI implementation."
- **Offer**: AI Analytics Platform Pro

**AI Response:**
```
Intent: High
Reasoning: Strong technical background in data science and machine learning aligns perfectly with AI Analytics Platform Pro. Senior role indicates decision-making authority and budget access.
```

**Scoring Breakdown:**
- Rule Score: 40 points (20 for senior role + 20 for tech industry)
- AI Score: 50 points (High intent classification)
- **Total: 90 points (High Intent)**

### Intent Classification Thresholds

| Intent Level | Score Range | Description |
|-------------|-------------|-------------|
| **🔥 High** | 70-100 | Strong buying signals, high probability to purchase |
| **⚡ Medium** | 40-69 | Moderate interest, needs nurturing |
| **❄️ Low** | 0-39 | Limited alignment, low priority |

### Reasoning Logic

The AI provides human-readable explanations considering:

1. **Role-Offer Alignment**: How well the person's job relates to the product
2. **Industry Fit**: Whether their industry typically uses such solutions  
3. **Experience Indicators**: Signs of relevant experience in their bio
4. **Decision Authority**: Likelihood they can make purchasing decisions
5. **Company Profile**: Size and type of organization
6. **Pain Point Indicators**: Mentions of challenges the product solves

### Example Scoring Scenarios

#### Scenario 1: High Intent Lead
```json
{
  "name": "Sarah Johnson",
  "role": "VP of Analytics", 
  "company": "DataDriven Corp",
  "industry": "SaaS",
  "bio": "Leading analytics transformation initiatives. Looking for advanced ML platforms to scale our data science capabilities."
}
```
- **Rule Score**: 40 (VP role + SaaS industry)  
- **AI Score**: 50 (Strong intent signals)
- **Total**: 90 (High Intent)
- **Reasoning**: "VP-level decision maker in SaaS with explicit interest in ML platforms. Direct mention of scaling data science capabilities aligns perfectly with the offer."

#### Scenario 2: Medium Intent Lead  
```json
{
  "name": "Mike Chen",
  "role": "Business Analyst",
  "company": "RetailCorp", 
  "industry": "Retail",
  "bio": "Business intelligence professional focused on improving operational efficiency through data insights."
}
```
- **Rule Score**: 10 (Analyst role + non-tech industry)
- **AI Score**: 30 (Moderate alignment)  
- **Total**: 40 (Medium Intent)
- **Reasoning**: "BI background shows data analytics interest, but analyst role suggests limited decision authority. Retail industry may have budget constraints."

#### Scenario 3: Low Intent Lead
```json
{
  "name": "Lisa Brown",
  "role": "Marketing Coordinator",
  "company": "Local Services Inc",
  "industry": "Local Services", 
  "bio": "Coordinating marketing campaigns and social media content for local business growth."
}
```
- **Rule Score**: 0 (Coordinator role + local services)
- **AI Score**: 10 (Limited alignment)
- **Total**: 10 (Low Intent)  
- **Reasoning**: "Role focuses on marketing coordination rather than analytics. Local services industry typically has limited need for advanced AI analytics platforms."

---

## 📝 Error Handling

### Common Error Responses

#### 400 Bad Request
```json
{
  "error": "Missing required columns: ['role', 'industry']"
}
```

#### 404 Not Found  
```json
{
  "error": "No product offer found. Please create an offer first."
}
```

#### 500 Internal Server Error
```json
{
  "error": "AI analysis failed: API quota exceeded"
}
```

---

## 🔧 Configuration Options

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GEMINI_API_KEY` | ✅ Yes | - | Google Gemini API key |
| `SECRET_KEY` | ❌ No | Auto-generated | Django secret key |
| `DEBUG` | ❌ No | `True` | Debug mode toggle |
| `ALLOWED_HOSTS` | ❌ No | `localhost,127.0.0.1` | Allowed hosts |

