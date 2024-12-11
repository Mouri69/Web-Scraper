# Page Scraper

Page Scraper is a Python-based application that allows users to extract all links and images from a given webpage. It includes a graphical user interface (GUI) for ease of use and organizes the extracted data into an easily searchable format. The application can save the results into a JSON file for further analysis.

## Features

- Fetches HTML content from a user-provided URL.
- Extracts:
  - Links (internal and external).
  - Images.
- Organizes links into internal and external categories.
- Saves results in a well-structured JSON file.
- User-friendly GUI built with Tkinter.

## Requirements

- Python 3.7 or higher.
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `tkinter` (built-in with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/page-scraper.git](https://github.com/Mouri69/Web-Scraper
   cd extractweb
   ```
2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the application:
   ```bash
   python webextract.py
   ```

## Usage

1. Launch the application.
2. Enter the URL of the webpage you want to scrape.
3. Click the **Scrape URL** button.
4. Choose a location to save the results in JSON format.

## Creating an Executable

To create a standalone executable file:

1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Generate the executable:
   ```bash
   pyinstaller --onefile --windowed extractweb.py
   ```
3. The `.exe` file will be located in the `dist` directory.

## JSON Output Format

The JSON file will include the following structure:
```json
{
  "internal_links": ["/about", "/contact"],
  "external_links": ["https://example.com"],
  "images": ["/images/logo.png", "https://example.com/banner.jpg"]
}
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Created by [Mouri69](https://github.com/Mouri69).

