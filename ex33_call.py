from datetime import datetime
startTime = datetime.now()

def while_loop(start, stop, increment):
	numbers = []
	while start < stop:
		print "At the top i is %d" % start
		numbers.append(start)

		start = start + increment
		print "Numbers now: ", numbers
		print "At the bottom start is %d" % start

print while_loop(0, 4000, 1)

print datetime.now() - startTime