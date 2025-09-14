# Zootopia-with-API

Zootopia-with-API is a Python + HTML project that fetches animal data from an external API and renders a website or static pages using that data, instead of loading from local JSON files.

---

## Features

- Fetches data about animals (or whatever entities are used) from an API via `data_fetcher.py`.  
- Generates HTML output using templates (for example via `animals_template.html` + `animals_web_generator.py`).  
- You can view the HTML files locally or serve them via a simple HTTP server.

---

## File Structure

Zootopia-with-API/
├── .env # Environment variables (e.g. API keys, endpoints)
├── data_fetcher.py # Module to make API calls and gather data
├── animals_web_generator.py # Script that takes fetched data + template → HTML
├── animals_template.html # HTML template file
├── animals.html # Generated HTML output
├── .gitignore
└── README.md

---

## Setup

1. **Clone the repository**

   
   git clone https://github.com/fcuriel66/Zootopia-with-API.git
   cd Zootopia-with-API

2. **Install dependencies
   
pip install -r requirements.txt



