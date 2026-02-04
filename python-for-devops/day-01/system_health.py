import psutil

def system_health():
    cpu_threshold = int(input("Enter CPU usage threshold (%): "))
    memory_threshold = int(input("Enter Memory usage threshold (%): "))
    disk_threshold = int(input("Enter Disk usage threshold (%): ")) 

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    if cpu_usage > cpu_threshold:
        print(f"ALERT: CPU usage is at {cpu_usage}% which exceeds the threshold of {cpu_threshold}%")
    else:
        print(f"CPU usage is at {cpu_usage}%, within the threshold.")

    if memory_usage.percent > memory_threshold:
        print(f"ALERT: Memory usage is at {memory_usage.percent}% which exceeds the threshold of {memory_threshold}%")
    else:
        print(f"Memory usage is at {memory_usage.percent}%, within the threshold.")

    if disk_usage.percent > disk_threshold:
        print(f"ALERT: Disk usage is at {disk_usage.percent}% which exceeds the threshold of {disk_threshold}%")
    else:
        print(f"Disk usage is at {disk_usage.percent}%, within the threshold.")
        
    print("\nSystem Health Summary:")
    print("-----------------------")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage.percent}%")
    print(f"Disk Usage: {disk_usage.percent}%")

system_health()          