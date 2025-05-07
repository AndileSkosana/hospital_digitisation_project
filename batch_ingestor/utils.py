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

def upsert_from_temp_to_main(temp_table, main_table, key_columns, conn):
    """
    Upserts data from a temp table to the main table using the specified key columns.
    """
    set_columns = get_set_columns(temp_table, key_columns, conn)
    key_conditions = ' AND '.join([f"main.{col} = temp.{col}" for col in key_columns])

    with conn.cursor() as cur:
        # Update existing records
        update_query = f"""
        UPDATE {main_table} AS main
        SET {set_columns}
        FROM {temp_table} AS temp
        WHERE {key_conditions};
        """
        cur.execute(update_query)

        # Insert new records
        insert_query = f"""
        INSERT INTO {main_table}
        SELECT * FROM {temp_table}
        WHERE NOT EXISTS (
            SELECT 1 FROM {main_table} AS main
            WHERE {key_conditions}
        );
        """
        cur.execute(insert_query)

    conn.commit()

def get_set_columns(temp_table, key_columns, conn):
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = %s;
        """, (temp_table,))
        columns = [row[0] for row in cur.fetchall()]
        set_columns = ', '.join([
            f"{col} = temp.{col}"
            for col in columns if col not in key_columns
        ])
    return set_columns
