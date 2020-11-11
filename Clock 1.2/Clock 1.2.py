import time
import winsound

count = float(input("How long of a wait: "))

while True:

    print(count, end='\r')
    time.sleep(1)
    count = count - 1

    if count == 0:
        break

print("Time is up!")
#The sound can be replaced with any .wav files
winsound.PlaySound("Small Bell Jingle", winsound.SND_FILENAME)