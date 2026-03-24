def read_logs(file_path):
    with open(file_path, "r") as f:
        return f.readlines()
if __name__ == "__main__":
    logs = read_logs("sample_logs/logs.txt")
    
    print("Logs:")
    for log in logs:
        print(log.strip())