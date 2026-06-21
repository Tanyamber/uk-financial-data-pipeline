# End-to-End UK Financial Transactions Data Pipeline

## 🏆 Project Architecture & Summary
An automated, multi-tiered data engineering pipeline designed to ingest unstructured transactional logs from an upstream endpoint, execute validation transformations, stream the normalized dataset into a cloud warehouse layer, and serve operational metrics to business intelligence suites.

---

## 🛠️ Tech Stack & Systems Architecture
* **Ingestion Core:** Python (Pandas, Requests Engine, OS Directory Management)
* **Storage Layer:** Local File-System Target Ingestion (Staging Layer / CSV Parsing)
* **Cloud Infrastructure:** Google BigQuery Data Warehouse Sandbox Environment
* **Transport Optimization:** Apache Arrow Binary Engine (`pyarrow` Columnar Stream serialization)
* **Presentation Layer:** Power BI Desktop Suite (Cloud Database Data Modeling)
* **Security & Governance:** Automated `.gitignore` configuration guarding private IAM Service Account keys (`gcp_credentials.json`)

---

## 🚰 Data Lineage Pipeline Execution Stages

### 1. Extraction & Local Staging (`ingest_pipeline.py`)
* Establishes secure connection parameters with public REST API endpoints.
* Parses unstructured JSON arrays into localized relational data frames.
* Implements robust anomaly screening rules to deduplicate incoming `transaction_id` records.
* Automatically creates system runtime directories to write clean CSV payloads into isolated target staging zones.

### 2. Cloud Ingestion Layer (`load_to_cloud.py`)
* References a secure local service key account payload to establish authentication parameters with Google Cloud.
* Converts tabular structures into Apache Arrow memory maps for low-latency streaming uploads.
* Streams clean staging tables directly into targeted Cloud Data Warehousing datasets (`reporting_staging`).
* Configures overwriting rules (`WRITE_TRUNCATE`) to handle record initialization and safeguard state synchronization.

### 3. Business Intelligence & Modeling (`UK_Transaction_Analytics.pbix`)
* Establishes a direct connection protocol between Power BI and BigQuery cloud warehouse repositories.
* Models data dimensions into high-performance reporting memory tables.
* Configures executive monitoring parameters, mapping total operational volume metrics, transactional settlement distributions, and detailed audit logging tables.