import os
import pandas as pd
from sqlalchemy import create_engine

# Define the PostgreSQL connection details
db_user = 'postgres'  # username
db_password = 'Sharon@44'  # password, URL encode special characters
db_password_encoded = db_password.replace('@', '%40')  # Encode '@' as '%40'
db_host = 'localhost'
db_port = '5432'
db_name = 'sales_inventory'

# Directory containing your CSV files
#csv_directory = r'C:\Users\lenovo\Desktop\SQL+PYTHON+POWERBI PROJECT'
csv_directory = r"C:\Users\lenovo\Desktop\SQL+PYTHON+POWERBI PROJECT\data"

# Use the encoded password in the connection string
engine = create_engine(f'postgresql://{db_user}:{db_password_encoded}@{db_host}:{db_port}/{db_name}')

def load_csv_to_postgres(file_path, table_name):
    """Load a single CSV file to PostgreSQL"""
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Push DataFrame to PostgreSQL table
        df.to_sql(table_name, engine, index=False, if_exists='replace')  # Replace 'replace' with 'append' if you want to add data

        print(f"Successfully loaded {file_path} into table {table_name}")
    except Exception as e:
        print(f"Failed to load {file_path}: {e}")

def push_all_csvs_to_postgres():
    """Iterate through CSV files and push them to PostgreSQL"""
    for file_name in os.listdir(csv_directory):
        if file_name.endswith('.csv'):
            file_path = os.path.join(csv_directory, file_name)
            table_name = os.path.splitext(file_name)[0]  # Use file name (without extension) as table name

            # Load each CSV into its respective table in PostgreSQL
            load_csv_to_postgres(file_path, table_name)

if __name__ == "__main__":
    push_all_csvs_to_postgres()