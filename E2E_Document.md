# End-to-End Workflow

## Step 1: Log Ingestion
Logs are read from sample_logs/logs.txt.

## Step 2: Processing
Logs are converted into structured format.

## Step 3: Anomaly Detection
Logs with status 500/503 are detected as anomalies.

## Step 4: Alert System
Anomalies trigger alert messages.

## Step 5: Report Generation
Logs and anomalies are stored in report.txt.

## Final Flow
Logs → Ingestion → Processing → Detection → Alert → Report
