# TorontoTransitMap
A Django rest API project fetching go train and TTC information and cross referencing go transit stops along TTC routes

# OpenData Toronto TTC Schedules Downloader

This Python script allows you to download and extract TTC (Toronto Transit Commission) Routes and Schedules data from the OpenData Toronto CKAN instance.

## Prerequisites

- Python 3
- Requests library (`pip install requests`)

## Usage

1. cd to the scripts folder (`/scripts`).
2. Open the terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script by executing the command:

   ```bash
   python fetch_ttc_schedules.py
   ```
5. The data will now be available in the TransitData Folder