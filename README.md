# Sales Intelligence Automator

**Author:** Sakshi Shah

## Overview

Sales Intelligence Automator is an AI-powered lead intelligence platform that automates company research, ICP qualification, and sales brief generation.

The application accepts company leads, scrapes company websites, extracts relevant business information, enriches analysis using a Retrieval-Augmented Generation (RAG) knowledge base, and generates structured sales intelligence reports using Google Gemini.

The goal is to help sales teams quickly identify qualified prospects, understand business pain points, detect buying signals, and prepare personalized discovery conversations.

---

## Key Features

### Lead Research & Enrichment

* Upload leads through CSV
* Automatic company website processing
* Website content extraction and cleaning
* Structured company profiling

### AI-Powered Sales Intelligence

* Google Gemini-powered company analysis
* B2B lead qualification
* Industry classification
* Company size estimation
* Target customer identification

### ICP (Ideal Customer Profile) Matching

* Qualification scoring
* Target role identification
* Pain point detection
* Buying signal detection
* Trigger event identification
* Tech stack signal detection
* ICP match explanation

### Retrieval-Augmented Generation (RAG)

* Local knowledge base support
* Semantic search using embeddings
* Context retrieval using vector similarity
* AI analysis enhanced with retrieved business knowledge

### Sales Enablement

* Personalized discovery questions
* Structured sales briefs
* Downloadable JSON output
* Interactive Streamlit dashboard

---

## Architecture

```text
Lead CSV
    │
    ▼
Website Scraper
    │
    ▼
Content Extractor
    │
    ▼
Content Cleaner
    │
    ▼
RAG Retrieval Layer
    │
    ├── Knowledge Base
    ├── Embeddings
    └── Vector Search
    │
    ▼
Gemini Analysis Engine
    │
    ▼
ICP Qualification
    │
    ▼
Sales Brief Generation
    │
    ▼
Streamlit Dashboard
```

---

## Project Structure

```text
sales-intelligence-automator/

├── app.py
├── README.md
├── requirements.txt
├── .env

├── ai/
│   ├── analyzer.py
│   ├── gemini_client.py
│   └── prompts.py

├── config/
│   └── default_icp.py

├── data/
│   ├── leads.csv
│   └── output.json

├── knowledge/
│   └── company_services.txt

├── models/
│   ├── icp_profile.py
│   ├── lead.py
│   └── sales_brief.py

├── rag/
│   ├── embedder.py
│   ├── retriever.py
│   └── vector_store.py

├── scraper/
│   ├── web_scraper.py
│   ├── content_extractor.py
│   └── content_cleaner.py

├── services/
│   ├── company_resolver.py
│   └── lead_processor.py
```

---

## Technologies Used

### Backend

* Python 3.11+
* Pydantic
* Pandas
* Requests
* BeautifulSoup4

### AI & RAG

* Google Gemini 2.5 Flash
* Sentence Transformers
* all-MiniLM-L6-v2
* Scikit-Learn
* Retrieval-Augmented Generation (RAG)

### Frontend

* Streamlit

---

## Installation

### Clone Repository

```bash
git clone https://github.com/sakshu18/sales-intelligence-automator.git

cd sales-intelligence-automator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

## Running the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## How It Works

### Step 1: Upload Leads

Upload a CSV file containing:

```csv
company_name,website_url,location
Houston Roofing Online,https://www.houstonroofingonline.com,Houston
```

### Step 2: Website Research

The system:

* Downloads website content
* Extracts visible text
* Removes navigation and noise
* Creates a clean company profile

### Step 3: RAG Retrieval

The application:

* Loads business knowledge from the knowledge base
* Converts text into embeddings
* Performs semantic similarity search
* Retrieves relevant context

### Step 4: AI Analysis

Gemini analyzes:

* Company overview
* Industry
* Company size
* Core services
* Target customers
* B2B qualification

### Step 5: ICP Qualification

The system evaluates:

* Decision makers
* Pain points
* Buying signals
* Trigger events
* Technology indicators
* Qualification score

### Step 6: Sales Brief Generation

Produces:

* Structured sales intelligence
* Discovery questions
* Qualification reasoning
* Actionable sales insights

---

## Sample Output

```json
{
  "company_name": "Houston Roofing Online",
  "industry": "Construction",
  "company_size": "SMB",
  "core_product_service": "Residential and Commercial Roofing",
  "target_customer": "Homeowners and Property Managers",
  "b2b_qualified": true,

  "icp": {
    "qualification_score": 88,
    "target_roles": [
      "Owner",
      "Operations Manager"
    ],
    "pain_points": [
      "Lead generation",
      "Operational efficiency"
    ],
    "buying_signals": [
      "Online quote requests",
      "Growth initiatives"
    ]
  },

  "sales_questions": [
    "How do you currently generate new leads?",
    "What tools do you use to manage customer relationships?",
    "What operational challenges are limiting growth?"
  ]
}
```

---

## Why RAG?

Traditional prompting relies only on website content.

This project enhances AI analysis by retrieving relevant business knowledge before sending data to Gemini.

Benefits:

* More consistent qualification
* Better ICP matching
* Improved sales recommendations
* Reduced hallucinations
* Domain-specific context injection

---

## Future Improvements

* Multi-page website crawling
* Async processing
* CRM integrations (HubSpot, Salesforce)
* Vector database support (FAISS, ChromaDB)
* PDF and Excel exports
* Lead scoring dashboard
* Historical lead analytics
* Multi-tenant knowledge bases

---

## License

This project was developed as part of a technical assessment assignment and is intended for educational and demonstration purposes.
