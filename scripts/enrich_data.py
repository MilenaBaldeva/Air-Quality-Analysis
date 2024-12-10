{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Enriching Data with City and Country\
import pandas as pd\
import requests\
\
# Google Maps API function\
def get_city_country(lat, lon):\
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"  # Actual Google Maps API key\
    base_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng=\{lat\},\{lon\}&key=\{api_key\}"\
    response = requests.get(base_url)\
    if response.status_code == 200:\
        data = response.json()\
        if data['results']:\
            address_components = data['results'][0]['address_components']\
            city, country = None, None\
            for component in address_components:\
                if "locality" in component['types']:\
                    city = component['long_name']\
                elif "country" in component['types']:\
                    country = component['long_name']\
            return city, country\
    return None, None\
\
# Load the PurpleAir data\
file_path = "purpleair_sensor_locations.csv"  # Path to the previously saved CSV\
df = pd.read_csv(file_path)\
\
# Initialize new columns for city and country\
df['city'] = None\
df['country'] = None\
\
# Populate city and country columns\
for index, row in df.iterrows():\
    lat, lon = row['latitude'], row['longitude']\
    city, country = get_city_country(lat, lon)\
    df.at[index, 'city'] = city\
    df.at[index, 'country'] = country\
\
# Save the updated DataFrame to a new CSV file\
output_file_path = "sensor_locations_with_city_country.csv"\
df.to_csv(output_file_path, index=False)\
print(f"Updated file saved to \{output_file_path\}")}