import requests
from io import BytesIO
import zipfile
import os

# URL to the ZIP file
url = 'https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/7795b45e-e65a-4465-81fc-c36b9dfff169/resource/cfb6b2b8-6191-41e3-bda1-b175c51148cb/download/opendata_ttc_schedules.zip'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create a BytesIO object from the content
    zip_data = BytesIO(response.content)

    # Unzip the data
    with zipfile.ZipFile(zip_data, 'r') as zip_ref:
        # Extract all contents to a temporary folder
        extraction_path = 'TransitData'
        zip_ref.extractall(extraction_path)

        # Now, you can process the extracted data as needed
        # For example, print the names of all files in the extracted folder
        for filename in os.listdir(extraction_path):
            print(filename)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
