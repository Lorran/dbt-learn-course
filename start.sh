#!/bin/bash

# # Activate the Python virtual environment
# source env/bin/activate

# # Navigate to the dbt project directory
# cd my_project

# # Run the dbt project
# docker build -t pg_projeto .


# docker run -d -p 5432:5432 --name pg_projeto pg_projeto

# python -c 'import load_data; load_data.load_csv_files_to_postgres()'

# pip install -r requirements.txt




docker build --build-arg POSTGRES_USER=$(grep POSTGRES_USER .env | cut -d '=' -f2) \
             --build-arg POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env | cut -d '=' -f2) \
             --build-arg POSTGRES_DB=$(grep POSTGRES_DB .env | cut -d '=' -f2) \
             --build-arg POSTGRES_PORT=$(grep POSTGRES_PORT .env | cut -d '=' -f2) \
             --build-arg DB_HOST=$(grep DB_HOST .env | cut -d '=' -f2) \
             -t image-dbt-postgres .

docker run -d -p 5432:5432 --name dbt-postgres-lab image-dbt-postgres 