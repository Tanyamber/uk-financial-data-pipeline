import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

def upload_staging_to_bigquery():
    print("🚀 [START] Initializing Cloud Warehousing Pipeline Layer...")
    
    # 1. SECURITY CONFIGURATION: Define your local path parameters securely
    # This path is ignored by GitHub due to our .gitignore configuration shield
    credential_path = "gcp_credentials.json"
    local_data_path = "landing_zone/cleaned_transactions.csv"
    
    # 2. SCHEMA MANAGEMENT: Define your explicit Cloud Database Target coordinates
    # Replace 'uk-financial-pipeline-46' with your EXACT project ID if it varies slightly
    project_id = "uk-financial-data-pipeline" 
    dataset_id = "reporting_staging"
    table_id = "stg_uk_transactions"
    full_table_path = f"{project_id}.{dataset_id}.{table_id}"
    
    try:
        # Validate that credentials exist locally before initializing cloud runtime
        if not os.path.exists(credential_path):
            raise FileNotFoundError(f"Missing security passport file at: {credential_path}")
            
        print("🔑 Authenticating handshake protocol with Google Cloud Engine...")
        credentials = service_account.Credentials.from_service_account_file(credential_path)
        client = bigquery.Client(credentials=credentials, project=project_id)
        
        # 3. EXTRACT (Stage 2): Load your local staging CSV file back into memory
        print(f"📖 Reading target data source: {local_data_path}")
        df = pd.read_csv(local_data_path)
        
        # 4. LOAD (Stage 2): Stream your dataframe directly into cloud database tables
        print(f"📤 Streaming {len(df)} transactions to Cloud Data Warehouse: {full_table_path}...")
        
        # Configure the load behavior (Overwrite table if it already exists to prevent duplicates)
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE", 
            autodetect=True # Automatically map database column data types
        )
        
        # Execute the ingestion streaming pipeline job
        job = client.load_table_from_dataframe(df, full_table_path, job_config=job_config)
        job.result() # Wait for the cloud engine to confirm successful execution
        
        print(f"🏆 [SUCCESS] Cloud target table updated. Schema location: {full_table_path}")
        
    except Exception as e:
        print(f"❌ [ERROR] Cloud pipeline layer broke down. Error trace logs: {str(e)}")

if __name__ == "__main__":
    upload_staging_to_bigquery()