
from time import sleep
i = 1
while True:
    print(i)
    sleep(1) #sleep for one sec
    i = i * 2

#Python doesn't have a limited amout to stop overflow so the loop will go forever till it takes over all memory
