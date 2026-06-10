# Sales Intelligence Automator

Author: Sakshi Shah

## Overview

Sales Intelligence Automator is an AI-powered lead research tool that automates the process of gathering company information and generating sales-ready insights.

The application accepts company leads, collects information from company websites, analyzes the content using Google's Gemini LLM, and generates structured sales briefs that help sales representatives prepare for discovery calls.

---

## Features

* Upload company leads via CSV
* Automatic website scraping
* Content extraction and cleaning
* AI-powered company analysis using Gemini
* B2B qualification assessment
* Automatic generation of sales discovery questions
* Simple Streamlit web interface

---

## Project Structure

```text
sales-intelligence-automator/

├── app.py
├── requirements.txt
├── README.md
├── .env

├── ai/
│   ├── analyzer.py
│   ├── gemini_client.py
│   └── prompts.py

├── data/
│   ├── leads.csv
│   └── output.json

├── models/
│   ├── lead.py
│   └── sales_brief.py

├── scraper/
│   ├── web_scraper.py
│   ├── content_extractor.py
│   └── content_cleaner.py

├── services/
│   ├── company_resolver.py
│   └── lead_processor.py

├── utils/
│   ├── helpers.py
│   └── logger.py
```

---

## Technologies Used

* Python 3.11+
* Streamlit
* Google Gemini 2.5 Flash
* BeautifulSoup4
* Requests
* Pandas
* Pydantic
* Python-dotenv

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd sales-intelligence-automator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## How to Use

1. Upload a CSV file containing lead information.
2. Click "Analyze Leads".
3. The system:

   * Scrapes company websites
   * Extracts relevant content
   * Cleans website noise
   * Sends content to Gemini
   * Generates a structured sales brief
4. View the generated results directly in the UI.

---

## Sample Output

```json
{
  "company_name": "Houston Roofing Online",
  "company_overview": "Provides roofing services for residential and commercial properties.",
  "core_product_service": "Roof installation and repair",
  "target_customer": "Homeowners and businesses",
  "b2b_qualified": true,
  "sales_questions": [
    "How do you currently acquire new customers?",
    "Do you use a CRM system?",
    "What are your biggest sales challenges?"
  ]
}
```

---

## Design Notes

The application follows a modular architecture where each component has a single responsibility. The scraping layer retrieves and extracts website content, the AI layer handles prompt management and LLM interaction, and the services layer orchestrates the overall workflow. This separation improves maintainability and allows individual components to be replaced independently.

Google Gemini 2.5 Flash was selected because it offers strong reasoning capabilities, fast response times, and a free development tier. Pydantic models are used to validate AI-generated responses and ensure that outputs remain structured and reliable.

The system handles imperfect inputs by separating lead normalization from processing logic. Website content is cleaned before being sent to the LLM to reduce noise from navigation menus, cookie banners, and repetitive marketing content. If additional time were available, future improvements would include multi-page crawling, asynchronous processing, CRM integration, and enhanced lead scoring capabilities.

---

## Future Improvements

* Multi-page website crawling
* Parallel processing for faster execution
* CRM integration (HubSpot/Salesforce)
* Advanced lead scoring
* Export to Excel/PDF
* Historical lead analysis

---

## License

This project was developed as part of a technical assessment assignment.
