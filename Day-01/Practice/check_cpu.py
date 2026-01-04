import psutil

ip_cpu_th = float(input("Enter the CPU threshold:"))
ip_disk_th = float(input("Enter the Disk threshold:"))
ip_memory_th = float(input("Enter the Memory threshold:"))

cpu_th = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')


print(f"Current CPU Value is:{cpu_th}")
if cpu_th > ip_cpu_th:
    print("Email Sent....")
else:
    print("CPU within limits...")

print(f"Current memory usage is:{memory_usage}")
if memory_usage > ip_memory_th:
    print("Email Sent....")
else:
    print("Memory within limits...")

print(f"Current disk usage is:{disk_usage}")
if disk_usage > ip_disk_th:
    print("Email Sent....")
else:
    print("Disk within limits...")