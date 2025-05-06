# batch_ingestor/utils.py

import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "hospital"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "postgres_db"),
        port=os.getenv("POSTGRES_PORT", 5432)
    )

def ingest_csv_to_temp_table(csv_path, temp_table, conn):
    df = pd.read_csv(csv_path)
    if df.empty:
        print(f"No data found in {csv_path}")
        return

    columns = ','.join(df.columns)
    placeholders = ','.join(['%s'] * len(df.columns))
    values = [tuple(row) for row in df.to_numpy()]

    with conn.cursor() as cur:
        cur.execute(f"TRUNCATE TABLE {temp_table}")
        execute_batch(
            cur,
            f"INSERT INTO {temp_table} ({columns}) VALUES ({placeholders})",
            values
        )
    conn.commit()

def upsert_from_temp_to_main
