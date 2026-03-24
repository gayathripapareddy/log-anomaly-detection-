from processing.distributed_parser import process_logs
from anomaly_detection.anomaly_detector import detect_anomalies

logs = process_logs("sample_logs/logs.txt")
anomalies = detect_anomalies(logs)

with open("report.txt", "w") as f:
    f.write("ALL LOGS:\n")
    for log in logs:
        f.write(str(log) + "\n")

    f.write("\nANOMALIES:\n")
    for a in anomalies:
        f.write(str(a) + "\n")

print("✅ Report generated: report.txt"),