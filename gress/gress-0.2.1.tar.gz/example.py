import time
import gress

# init herd
sheeps = 100

# init bar
bar = gress.Bar("Counting: {count} of {maximum} ({percent}%) {bar} {speed}/s | {timer} | ETA {autoeta}", maximum=sheeps)
bar.start()

# count the sheeps
sleep = 0.1
for i in range(sheeps):
    time.sleep(sleep)
    
    # increment progress
    bar += 1
    
    # count slower while sleeping (50 sheeps and more)
    if bar.current == sheeps / 2:
        bar.write("{time} I should sleep now, so I'm counting slower!")
        sleep *= 2

# finish and make final report
bar.finish("{time} All {count} sheeps counted in {autotimer} with the average rate of {speed}/s.")
