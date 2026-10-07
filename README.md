# Playwright Infinite Scroll Scraper

A robust, commercial-grade asynchronous Python web scraper built using **Playwright**. This script specializes in handling modern web layouts that load content dynamically via infinite scrolling, ensuring full DOM mutation tracking before structured data extraction.

## 🚀 Features

- **Dynamic Scroll Calculation:** Recursively measures `scrollHeight` to accurately detect the true absolute bottom of an infinite scroll page.
- **Fingerprint Masking:** Fully integrated context emulation parameters (custom User-Agent, specific viewport view dimensions, locale, and timezone settings) paired with `playwright-stealth` to pass advanced browser sandboxes.
- **Nested Element Mapping:** Extracts multi-layered data points cleanly using nested child parent combinators and text content filters.
- **Structured Data Export:** Automatically flushes objects into a structured, well-indented local JSON storage format.

## 🛠️ Prerequisites & Installation

Make sure you have Python installed on your system. Install the required dependencies using your local terminal window:

```bash
pip install playwright playwright-stealth
playwright install chromium
```

## 💻 How To Run

Execute the main script file directly from your terminal:

```bash
python your_script_name.py
```

## 📊 Extracted Schema Output

The pipeline saves data into a structured `car2.json` file following this clean nested dictionary schema layout:

```json
[
    {
        "Title": "Mercedes-Benz W123 280E 1955",
        "Details": {
            "Description": "Uncompromising Stuttgart saloon",
            "Price": "USD 228 511",
            "Year": "1955",
            "Country": "United Kingdom",
            "Mileage": "104 338 km",
            "For more info link is here": {
                "Link": "https://webscraper.io..."
            }
        }
    }
]
```

## 📝 License

This project is open-source and available under the MIT License.
