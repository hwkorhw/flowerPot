from datetime import datetime

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")
year = (now.strftime("%Y"))[2:]
date = now.strftime("%m%d")

print(time)
print(year)
print(date)
