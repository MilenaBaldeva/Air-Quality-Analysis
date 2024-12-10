{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Extracting Data from the PurpleAir API\
\
# Install the necessary libraries: \
\
import requests\
import pandas as pd\
\
# PurpleAir API details\
api_url = "https://api.purpleair.com/v1/sensors"\
api_key = "YOUR_PURPLEAIR_API_KEY"  # Actual PurpleAir API key\
\
headers = \{\
    "X-API-Key": api_key\
\}\
\
# Define the fields you want to extract\
fields = "pm2.5_atm,temperature,humidity,sensor_index,latitude,longitude"\
\
# Add fields as query parameters\
params = \{\
    "fields": fields\
\}\
\
# Make the API request\
response = requests.get(api_url, headers=headers, params=params)\
\
if response.status_code == 200:\
    print("API Request Successful!")\
    data = response.json()\
\
    # Extract columns and data from the API response\
    columns = data.get("fields", [])\
    sensor_data = data.get("data", [])\
\
    # Create a DataFrame\
    df = pd.DataFrame(sensor_data, columns=columns)\
\
    # Save the DataFrame to a CSV file\
    file_path = "purpleair_sensor_locations.csv"\
    df.to_csv(file_path, index=False)\
    print(f"Data saved to \{file_path\}")\
else:\
    print(f"API Request Failed with status code \{response.status_code\}: \{response.text\}")\
}