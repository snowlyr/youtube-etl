import sqlite3
from sqlalchemy import create_engine
import pandas

def load_data(df, db_path='data/youtube.db'):
    # SQLite version
    conn = sqlite3.connect(db_path)
    df.to_sql('trending_videos', conn, if_exists='append', index=False)
    conn.close()

    # PostgreSQL version (alternative)
    # engine = create_engine('postgresql://user:password@localhost:5432/youtube')
    # df.to_sql('trending_videos', engine, if_exists='append', index=False)
