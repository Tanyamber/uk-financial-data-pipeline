import requests
import pandas as pd
import os

def run_extraction_pipeline():
    print("🚀 [START] Initializing UK Financial Data Extraction Pipeline...")
    
    # 1. THE SOURCE: A reliable open public API containing mocked transactional logs
    # In an enterprise, this would be an ANZ banking server endpoint or an AWS S3 bucket.
    api_url = "https://jsonplaceholder.typicode.com/todos" 
    
    try:
        # 2. EXTRACT: Fetch raw, unstructured data over the network
        print(f"📡 Connecting to data stream: {api_url}...")
        response = requests.get(api_url, timeout=10)
        
        # Check if HTTP connection is 200 OK
        response.raise_for_status() 
        raw_json_data = response.json()
        print("✅ Data successfully downloaded over network protocol.")
        
        # 3. TRANSFORM (Stage 1): Map unstructured JSON array into a relational tabular layout
        # This uses your academic knowledge of structural data schemas!
        df = pd.DataFrame(raw_json_data)
        
        # Let's clean the columns to make them match enterprise database naming standards
        df = df.rename(columns={
            'userId': 'user_id',
            'id': 'transaction_id',
            'title': 'transaction_description',
            'completed': 'is_settled'
        })
        
        # Check for missing data or duplicates (Data Validation Stage)
        initial_row_count = len(df)
        df = df.drop_duplicates(subset=['transaction_id'])
        print(f"🧹 Data cleaning complete. Validated {len(df)} transactions (Dropped {initial_row_count - len(df)} duplicate records).")
        
        # 4. LOAD (Stage 1): Create a landing folder on our machine and save as a clean file
        output_folder = "landing_zone"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        output_path = os.path.join(output_folder, "cleaned_transactions.csv")
        df.to_csv(output_path, index=False)
        
        print(f"💾 [SUCCESS] Clean database destination file written to: {output_path}")
        print(df.head(3)) # Print the top 3 rows to show our relational table structure
        
    except Exception as e:
        print(f"❌ [ERROR] Pipeline execution failed. Log analysis details: {str(e)}")

# This tells Python to run the function automatically when we execute the file
if __name__ == "__main__":
    run_extraction_pipeline()