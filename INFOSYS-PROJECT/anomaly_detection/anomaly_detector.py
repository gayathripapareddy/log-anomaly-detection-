def detect_anomalies(logs):
    anomalies = []

    for log in logs:
        # Server error
        if log["status"] == "500":
            anomalies.append(log)

        # Unusual status
        elif log["status"] not in ["200", "404"]:
            anomalies.append(log)

    return anomalies