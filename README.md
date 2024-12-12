# Air-Quality-Analysis
Python-based air quality data analysis using APIs and Tableau.

**Overview**

This project combines Python, PurpleAir and Google Maps APIs, and Tableau to analyze air quality data. The goal is to extract, enrich, and visualize air quality insights, providing actionable information for public health and environmental awareness.

**Features**

✅ Data Extraction
Retrieves real-time and historical air quality data using the PurpleAir API.
✅ Data Enrichment
Adds city and country information to sensor data via the Google Maps API.
✅ Scalable Workflow
Designed for efficient handling of large datasets using Python libraries like Pandas and Requests.
✅ Interactive Dashboard
The project includes a Tableau dashboard that visualizes air quality data and offers several interactive features.

**Tableau Dashboard Overview**

*🗺️ Air Quality Map*

• Displays average Air Quality Index (AQI) for each city.
• Color-coded markers based on air quality levels:
Green: Good
Yellow: Moderate
Orange: Unhealthy for Sensitive Groups
Red: Unhealthy
Purple: Very Unhealthy
Maroon: Hazardous
• Interactive filter: Clicking on one or multiple city filters the entire dashboard to show detailed data for that location.

*📈 Line Chart – Average AQI Over Time*
• Shows trends in average AQI over time.
• The line color changes based on AQI levels.
• Can be used as a time filter by selecting a specific date range.

*📊 Top Locations with Poor and Good Air Quality*
• Two tables showing:
  • Top Locations with Poor Air Quality (High AQI)
  • Top Locations with Good Air Quality (Low AQI)
• Displays the Top 5 states and Top 3 cities within each state.
• Clicking on a city or state filters the dashboard to display historical data for that location.

*📉 Air Quality Levels Distribution*
• Bar chart showing the distribution of air quality levels (Good, Moderate, Unhealthy, etc.) for the selected filters.

*🎛️ Filters*
• Time Period Filter: Select a date range to view data within that period.
• State Filter: Dropdown menu to filter by state.
• City Filter: Dropdown menu to filter by city.
• Map Filter: Mini map to select states or specific geographic regions.

*🗂️ Legend*
• Provides a color guide for air quality levels, applicable across all visualizations.


**Technologies Used**

• Programming Language: Python
• APIs:
  • PurpleAir API for sensor data
  • Google Maps API for location enrichment
• Tools: Pandas, Requests, CSV
• Data Visualization: Tableau - Interactive Tableau Dashboard: https://public.tableau.com/views/AIRQualityDashboard/Dashboard12?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


<img src="https://github.com/user-attachments/assets/b33e7a59-84f2-4d12-b9d3-ad80a1b831f5" width="500px" />

<img src="https://github.com/user-attachments/assets/3ff244bc-e557-4904-828a-b5e07c041d22" width="500px" />



/project-repo
│
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
│
├── /scripts            # Python scripts for each functionality
│   ├── extract_data.py # Extracts data from APIs
│   └── enrich_data.py  # Enriches data with location info
│
├── /notebooks          # Jupyter notebooks for analysis
│
└── /visualizations     # Tableau dashboards and screenshots
    └── dashboard.twb
