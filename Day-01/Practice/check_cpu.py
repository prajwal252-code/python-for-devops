import psutil

ip_cpu_th = float(input("Enter the CPU threshold:"))

cpu_th = psutil.cpu_percent(interval=1)
print(f"Current CPU Value is:{cpu_th}")
if cpu_th > ip_cpu_th:
    print("Email Sent....")
else:
    print("CPU within limits...")