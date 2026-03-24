def send_alert(anomalies):
    if anomalies:
        print("\n🚨 ALERT! Anomalies detected 🚨")
        for a in anomalies:
            print(a)
    else:
        print("\n✅ No anomalies found")