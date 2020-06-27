import time

counter = int(input("Your countdown: "))

for i in range(counter):
    print(counter - i)
    time.sleep(1)
