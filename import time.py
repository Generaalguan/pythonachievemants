import time
i =1000
while i> 0:
    print(i)
    i -= 1
    time.sleep(0.01)
if i == 0:
    print(0)
    print("surprise")