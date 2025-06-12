from datetime import datetime
import logging
#from scripts import *
from etl_core.extract import *
from etl_core.transform import *
from etl_core.load import *
#from dags.youtube_etl import *

def run_pipeline():
    logging.basicConfig(filename='./logs/etl.log', level=logging.INFO)

    try:
        logging.info(f"Starting ETL at {datetime.now()}")

        # Extract
        raw_path = extract_data(YT_API_KEY)
        logging.info(f"Extracted data to {raw_path}")

        # Transform
        df = transform_data(raw_path)
        logging.info(f"Transformed {len(df)} records")

        # Load
        load_data(df)
        logging.info("Data loaded successfully")

    except Exception as e:
        logging.error(f"ETL failed: {str(e)}")
        raise

if __name__ == "__main__":
    run_pipeline()
