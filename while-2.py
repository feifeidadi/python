import time

tired = False
badweather = False
step = 0

while step < 10000:
	print(step)
	if tired == True:
            print("I am tired")
            break
	elif badweather == True:
            print("Bad weather")
            break
	else:
            step = step + 1
            time.sleep(0.7)
            if step == 1000:
                tired = True
