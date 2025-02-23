# Mobile Phone Specifications Scraper

## Project Overview
This project is a web scraping tool designed to extract mobile phone specifications using **BeautifulSoup** and **Selenium**. The extracted data is saved in a text file for further use. The script allows users to specify the output file name and the target URL via command-line arguments. This project serves as an introductory exploration of web scraping techniques and dynamic content extraction.

## Features
- Extracts mobile phone specifications from a given URL.
- Uses **BeautifulSoup** to parse static HTML and **Selenium** for handling dynamic content.
- Saves extracted data into a text file.
- Command-line interaction allows users to specify output file name and URL dynamically.
- Supports a configurable ChromeDriver path (default set to the project directory).
- Modular and scalable code structure to support future enhancements.

## Requirements
Before running the script, ensure you have the following installed:

- **Python** (>=3.x)
- **Google Chrome** (latest version recommended)
- **ChromeDriver** (compatible with your Chrome version)
- Required Python libraries (install using `requirements.txt`):

  ```bash
  python -m venv web_scrap_env
  source web_scrap_env/bin/activate
  pip install -r requirements.txt
  ```

## Installation
### 1. Setting Up the Environment
It is recommended to run this project inside a virtual environment to keep dependencies isolated.

```bash
python -m venv web_scrap_env
source web_scrap_env/bin/activate  # For macOS/Linux
web_scrap_env\Scripts\activate  # For Windows (PowerShell)
```

Once activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Download and Install ChromeDriver
- Check your Chrome version by navigating to `chrome://settings/help`.
- Download the corresponding ChromeDriver from [ChromeDriver official site](https://sites.google.com/chromium.org/driver/).
- Place the downloaded executable in a stable location (For this project, it is placed inside the project folder).
- Update the script with the correct ChromeDriver path if necessary.

### 3. Clone the Repository
```bash
git clone https://github.com/Harishprabhu30/web_scrap.git
cd web_scrap
```

## Usage
Run the script from the command line by specifying the output file and the target URL:

```bash
python scrap_more.py output_file.txt "https://example.com/phone-details"
```

### Script Arguments:
1. **output_file.txt** - The name of the output text file where extracted data will be saved.
2. **URL** - The webpage URL containing mobile phone specifications.

Example usage:
```bash
python scrap_more.py extracted_data.txt "https://www.example.com/mobiles"
```

## Code Structure
```
├── scrap_more.py    # Main script for web scraping
├── requirements.txt # List of dependencies
├── README.md        # Project documentation
├── extracted_data/  # Folder containing sample extracted text files
├── chromedriver/    # Folder for ChromeDriver (for your reference)
└── other_exploration_files/ # Additional scripts used for learning
```

## How It Works
1. **Setup ChromeDriver**: The script initializes Selenium using the provided ChromeDriver path.
2. **Navigate the HTML Structure**: It identifies `<a>` tags and `<div>` containers to extract relevant phone specifications.
3. **Save Data**: Extracted specifications are stored in a text file specified via command-line input.
4. **Command-Line Interaction**: Users provide an output file name and URL dynamically when running the script.
5. **Repetitive Extraction**: The script currently requires manual execution for multiple pages, but automation is planned in future iterations.

## Future Improvements
- Implement a pipeline with `config.yaml` and `main.py` for autonomous extraction.
- Enable automatic navigation through multiple web pages and data extraction in a structured format.
- Support multiple output formats such as **CSV, JSON, or a database**.
- Develop an error-handling mechanism for robust execution and logging.
- Optimize scraping speed and efficiency by minimizing redundant Selenium interactions.

## License
This project is open-source and available under the MIT License.

## Contributions
Contributions are welcome! If you find a bug, have suggestions, or want to improve functionality, feel free to submit a pull request or open an issue.

## Contact
For any queries, collaborations, or suggestions, feel free to connect via [LinkedIn](https://www.linkedin.com/in/harishprabhu3007/).

