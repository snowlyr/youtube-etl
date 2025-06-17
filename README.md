# Intro
A ETL project to extract, transform and load youtube analytics data to a DB, in this case SQLite3

# Installation
This project runs entirely on Python3

## Installing Dependencies
```
pip install -r requirements.txt
```

## Setting up Environment Variables
Create a `.env` file for envirionment variables
```
cd youtube-etl
touch .env
```

Inside `.env`, input your `YT_API_KEY`
```
YT_API_KEY=<yoUrAPIkeY>
```

# Usage
## Extracting Data
Change directory to the root directory and run `etl_pipeline.py`
```
cd youtube-etl
python3 etl_pipeline.py
```

## Analysis
Change directory to the analysis folder and run the python scripts there, test scripts are relative to the directory the script is in
```
cd analysis
python3 testplot.py
python3 testml.py
```
### Plots
Plots are in the `visualisation` directory in `analysis`
