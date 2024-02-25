import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2

def load_and_process_files(file_path, con):
    files = os.listdir(file_path)

    for file in files:
        csv = os.path.join(file_path, file)
        df = pd.read_csv(csv, encoding='utf-8')
        

        df.to_sql(
            file.replace('.csv', ''),
            con,
            schema='public',
            if_exists='replace', index=False
        )

def main():
    load_dotenv()

    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_DB = os.getenv('POSTGRES_DB')

    if not all([POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, POSTGRES_PORT, POSTGRES_DB]):
        raise EnvironmentError("Some environment variables are missing!")

    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data')

    con = create_engine(f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')

    load_and_process_files(file_path, con)

if __name__ == "__main__":
    main()