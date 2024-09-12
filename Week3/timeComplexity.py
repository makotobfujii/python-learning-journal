import time

startTime = time.time()
count = 0
for i in range(100):
    count += 1
print("Total time was: ", time.time() - startTime)