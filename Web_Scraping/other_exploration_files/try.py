from pathlib import Path
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_details(url, chrome_driver_path):
    """Function extracts page params"""

    # Set up WebDriver Service
    service = Service(str(chrome_driver_path))
    driver = webdriver.Chrome(service=service) 

    # Open a web page
    driver.get(url)

    # click on a specific product
    # ------------------ Product 1 ----------------------
    prod_name = driver.find_element(By.CSS_SELECTOR, ".pro-series-container .pro-series-list li h4.pro-item-title").text
    product_mainpage = driver.find_element(By.CSS_SELECTOR, ".pro-series-container .pro-series-list li a")
    product_mainpage.click()
    
    # path to Specification page
    prod_spec_page = driver.find_element(By.CSS_SELECTOR, "div#series-id.topNavMaxScreen.newNav .topNavBox .tabControl a:nth-of-type(2)")
    prod_spec_url = prod_spec_page.get_attribute("href")
    driver.get(prod_spec_url) # navigates to specification page

    ## page params trial
    page_params = driver.find_element(By.CSS_SELECTOR, "div.page-params").text


    input("Press Enter to exit...")  # Keeps the browser open until you press Enter
    driver.quit()  # Close browser
    return prod_name, page_params



def main():
    
    # Define the correct ChromeDriver path
    chrome_driver_path = Path("/Users/harishprabhu/Desktop/Web_Scraping/chromedriver-mac-x64/chromedriver")
    url = 'https://www.vivo.com.cn/products-accessory.html'
    product_name, product_specs = extract_details(url = url, chrome_driver_path = chrome_driver_path)

    with open("prod_desc.txt", "w", encoding="utf-8") as file:
        file.write(f"Product Name - {product_name}\n\n")
        file.write(product_specs)



if __name__ == '__main__':
    main()