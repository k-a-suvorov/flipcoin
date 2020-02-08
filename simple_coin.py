import random
try:

	heads, tails, edges, cotimes_flipped = 0, 0, 0, 0
	timesflipped = 0  # <-- here's what I added.
	while timesflipped < 100:
		flips = random.randrange(3)
		if flips == 0:
			heads += 1
		elif flips == 1:
			tails += 1
		else:
			edges += 1
		timesflipped += 1

	print("Out of 100 flips ", str(heads), " - heads and ", str(tails), " - tails.", str(edges), "- edges")


except ValueError:
    print("You have some mistake of userinput current float Value")
except TypeError:
   print("You have some mistake of userinput float Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )

