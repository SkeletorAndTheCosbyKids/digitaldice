import numpy
GUESSES = 24
REPLICATES = 1000000
totalcorrect = 0

for x in range(0,REPLICATES):
	correct = 0
	term = numpy.random.permutation(GUESSES)
	for j in range(0,GUESSES):
		if term[j] == j:
			correct = correct+1
	totalcorrect = totalcorrect + correct
avg_correct = totalcorrect / REPLICATES
print(avg_correct)

