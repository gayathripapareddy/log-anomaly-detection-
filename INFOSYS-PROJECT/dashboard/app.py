import streamlit as st
from processing.distributed_parser import process_logs
from anomaly_detection.anomaly_detector import detect_anomalies

st.title("📊 Log Monitoring Dashboard")

logs = process_logs("sample_logs/logs.txt")
anomalies = detect_anomalies(logs)

st.subheader("All Logs")
st.write(logs)

st.subheader("🚨 Anomalies")
st.write(anomalies)