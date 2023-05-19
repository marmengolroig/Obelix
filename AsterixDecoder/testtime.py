import time
i=0
velocity = 3
while i<60:
    # Code to be executed in each iteration
    print("Performing iteration...")
    print(i)
    i=i+1
    # Delay the next iteration by one second
    time.sleep(1/velocity)