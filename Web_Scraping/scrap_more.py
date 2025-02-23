from pathlib import Path
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def extract_details(save_file_name, url,chrome_driver_path = Path("/Users/harishprabhu/Desktop/Web_Scraping/chromedriver-mac-x64/chromedriver")):
    """Function extracts page params"""

    # Set up WebDriver Service
    service = Service(str(chrome_driver_path))
    driver = webdriver.Chrome(service=service) 

    # Open a web page
    driver.get(url)

    # path to Specification page
    # prod_name = driver.find_element(By.CSS_SELECTOR, "div.topNavMaxScreen.J_detail_naviFUN.newNav div.topNavBox div.phoneNameFUN").text
    # print(prod_name)
    
    # Extract page params
    page_params = driver.find_element(By.CSS_SELECTOR, "div.page-params").text

    with open(f"/Users/harishprabhu/Desktop/Web_Scraping/extracted_products/{save_file_name}.txt", "w", encoding="utf-8") as file:
        file.write(f"Product Details:\n\n{page_params}")
    
    input("Press Enter to exit...")  # Keeps the browser open until you press Enter
    driver.quit()  # Close browser

def main():
    
    # Define the correct ChromeDriver path
    # chrome_driver_path = Path("/Users/harishprabhu/Desktop/Web_Scraping/chromedriver-mac-x64/chromedriver")

     # Check if URL is provided as a command-line argument
    if len(sys.argv) < 3:
        print("Usage: python script.py <output-file-name> <URL>")
        sys.exit(1)

    output_file_name = sys.argv[1]
    url = sys.argv[2]  # Get the URL from command-line input
    extract_details(save_file_name = output_file_name, url = url)
    print(f"Extraction completed! Data Saved in {output_file_name}.txt File")

if __name__ == '__main__':
    main()