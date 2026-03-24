from dask import delayed, compute
from ingestion.log_ingestion import read_logs

from anomaly_detection.anomaly_detector import detect_anomalies
from anomaly_detection.alert_system import send_alert


def parse_log(line):
    parts = line.split()
    return {
        "ip": parts[0],
        "method": parts[1],
        "endpoint": parts[2],
        "status": parts[3]
    }


def process_logs(file_path):
    logs = read_logs(file_path)

    tasks = [delayed(parse_log)(log) for log in logs]
    results = compute(*tasks)

    anomalies = detect_anomalies(results)

    print("\nDetected anomalies:")
    for a in anomalies:
        print(a)

    send_alert(anomalies)

    return results


if __name__ == "__main__":
    process_logs("sample_logs/logs.txt")