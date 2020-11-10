import time

count = float(input("How long of a wait: "))

while True:

    print(count)
    time.sleep(1)
    count = count - 1

    if count == 0:
        break

print("Time is up!")