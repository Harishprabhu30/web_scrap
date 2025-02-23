from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

# Step 1: Request the webpage
url = "https://www.vivo.com.cn/products-accessory.html"
headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get(url, headers=headers)

# Step 2: Parse HTML
soup = BeautifulSoup(page.text, 'html.parser')

# Step 3: Find the container div
container = soup.find("div", class_="pro-series-container")

data_list = []  # List to store extracted data

if container:
    # Step 4: Find the product list
    product_list = container.find("ul", class_="pro-series-list")
    
    if product_list:
        products = product_list.find_all("li")  # Extract all li elements

        for product in products:
            data_track = product.get("data-track")  # Extract the data-track attribute

            if data_track:
                data_list.append(data_track)  # Store extracted data

    else:
        print("❌ Error: Could not find the pro-series-list ul")
else:
    print("❌ Error: Could not find the pro-series-container div")

# Step 5: Save output
if data_list:
    # Save as text file
    with open("vivo_data.txt", "w", encoding="utf-8") as f:
        for item in data_list:
            f.write(item + "\n")
    print("✅ Data saved as vivo_data.txt")

    # Save as JSON file
    with open("vivo_data.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    print("✅ Data saved as vivo_data.json")

    # Save as Excel file
    df = pd.DataFrame({"data-track": data_list})  # Convert list to DataFrame
    df.to_excel("vivo_data.xlsx", index=False)
    print("✅ Data saved as vivo_data.xlsx")

else:
    print("❌ No data extracted.")
