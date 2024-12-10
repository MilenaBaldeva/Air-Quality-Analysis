{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
import pandas as pd\
import time\
import io  # Import io for StringIO\
\
# API details\
api_key = "************************"\
base_url = "https://api.purpleair.com/v1/sensors/\{sensor_index\}/history/csv"\
headers = \{"X-API-Key": api_key\}\
\
# Load the CSV file with sensor indexes\
file_path = "/USA_Sensor_Index.csv"\
sensor_df = pd.read_csv(file_path)\
\
# Ensure column name matches\
sensor_df.rename(columns=\{"Sensor_Index": "sensor_index"\}, inplace=True)\
\
# Parameters for historical data\
start_timestamp = "2023-11-26T00:00:00Z"\
end_timestamp = "2024-11-26T00:00:00Z"\
average = 1440\
fields = "pm2.5_atm"\
\
# Initialize a DataFrame to store results\
fetched_data = pd.DataFrame()\
\
# Iterate through the sensor indexes\
for index, row in sensor_df.iterrows():\
    sensor_index = row["sensor_index"]\
    url = base_url.format(sensor_index=sensor_index)\
\
    params = \{\
        "start_timestamp": start_timestamp,\
        "end_timestamp": end_timestamp,\
        "average": average,\
        "fields": fields,\
    \}\
\
    try:\
        # Make the API request\
        response = requests.get(url, headers=headers, params=params)\
        if response.status_code == 200:\
            print(f"Successfully fetched data for sensor \{sensor_index\}")\
            # Use io.StringIO to read CSV data from response\
            temp_df = pd.read_csv(io.StringIO(response.text))\
            temp_df["sensor_index"] = sensor_index  # Add sensor index column\
            fetched_data = pd.concat([fetched_data, temp_df], ignore_index=True)\
        else:\
            print(f"Failed for sensor \{sensor_index\}, status code: \{response.status_code\}")\
        \
        # Save data every 1000 sensors\
        if index % 1000 == 0 and index != 0:\
            partial_file_path = f"fetched_data_partial_\{index\}.csv"\
            fetched_data.to_csv(partial_file_path, index=False)\
            print(f"Saved progress to \{partial_file_path\} up to sensor \{sensor_index\}")\
            fetched_data = pd.DataFrame()  # Clear fetched data to save memory\
\
        # Be polite to the API (rate limiting)\
        time.sleep(1)  # Adjust based on rate limits or error codes\
    except Exception as e:\
        print(f"Error fetching data for sensor \{sensor_index\}: \{e\}")\
\
# Save the final data\
fetched_data.to_csv("fetched_data_final.csv", index=False)\
print("Final data saved!")}