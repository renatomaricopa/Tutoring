# from datetime import datetime 
# start_time = datetime.now()
# duration = datetime.now()-start_time
# duration = duration.total_seconds()
# while duration <= 10:
#     print(duration)
#     duration = datetime.now()-start_time
#     duration = duration.total_seconds()
# print("final duration" , duration)


// Copy and paste your work, or start typing.# TODO copy your work above here. 
# TODO translate the following pseudocode, expanding your work from above 
import time
from datetime import datetime
max_runtime = 2
start_time = datetime.now()

NUM_STEPS = 20
RISKY_STEPS = [3, 7, 15, 16, 20]
next_risky = RISKY_STEPS.pop(0)
for step in range(1, NUM_STEPS+1):
    print("EXECUTING STEP" , step)
    time.sleep(1) #seconds
    if step == next_risky-1:
        print("Risky step coming up next, backing up work." )
        next_risky = RISKY_STEPS.pop(0)

duration = datetime.now()-start_time
duration = duration.total_seconds()
while duration <= max_runtime:
    duration = datetime.now()-start_time
    duration = duration.total_seconds()
print("final duration" , duration)
print("We are running out of time in the job! Saving progress and exiting.")