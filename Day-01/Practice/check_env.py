def sum_of_num():
    sum1 = int(input("Enter First Number:"))
    sum2 = int(input("Enter Second Number:"))

    print(f"The sum of 2 Numbers is:{sum1+sum2}")

env = input("Enter the environment:")

print(f"The env is:{env}")

if env == "prod":
    sum_of_num()
else:
    print("Invalid Env")