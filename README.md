# Air-Quality-Analysis
Python-based air quality data analysis using APIs and Tableau.

Overview

This project combines Python, PurpleAir and Google Maps APIs, and Tableau to analyze air quality data. The goal is to extract, enrich, and visualize air quality insights, providing actionable information for public health and environmental awareness.

**Features**

• Data Extraction: Retrieves real-time and historical air quality data using the PurpleAir API.
• Data Enrichment: Adds city and country information to sensor data via the Google Maps API.
• Visualization: Presents insights through an interactive Tableau dashboard.
• Scalable Workflow: Designed for efficient handling of large datasets.

**Technologies Used**

• Programming Language: Python
• APIs:
  • PurpleAir API for sensor data
  • Google Maps API for location enrichment
• Data Visualization: Tableau
• Tools: Pandas, Requests, CSV
  
**Project Structure**

/project-repo
│
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── /data                   # CSV files with extracted/enriched data
├── /scripts                # Python scripts for each functionality
├── /notebooks              # Jupyter notebooks for analysis
├── /visualizations         # Tableau dashboards and screenshots
└── /docs                   # Additional documentation
