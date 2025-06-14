from datetime import datetime
import logging
#from scripts import *
from etl_core.extract import *
from etl_core.transform import *
from etl_core.load import *
#from dags.youtube_etl import *

# Declaring Globals
LOG_FILEPATH = './logs/etl.log'

def run_pipeline():
    logging.basicConfig(filename=LOG_FILEPATH, level=logging.INFO)
    print(f"[INFO] Started logging at {LOG_FILEPATH}")
    try:
        logging.info(f"Starting ETL at {datetime.now()}")

        # Extract
        raw_path = extract_data(YT_API_KEY)
        logging.info(f"Extracted data to {raw_path}")
        print(f"[INFO] Successfully extracted YouTube Data")

        # Transform
        df = transform_data(raw_path)
        logging.info(f"Transformed {len(df)} records")
        print(f"[INFO] Successfully transformed YouTube Data")

        # Load
        load_data(df)
        logging.info("Data loaded successfully")
        print(f"[INFO] Successfully loaded YouTube Data")

    except Exception as e:
        logging.error(f"ETL failed: {str(e)}")
        raise

if __name__ == "__main__":
    run_pipeline()
