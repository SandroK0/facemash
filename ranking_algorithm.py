# Python 3 program for Elo Rating
import math

# Function to calculate the Probability    
K = 30
d = 1   

def Probability(rating1, rating2):

	return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))


# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(Ra, Rb):
	

	# To calculate the Winning
	# Probability of Player B
	Pb = Probability(Ra, Rb)

	# To calculate the Winning
	# Probability of Player A
	Pa = Probability(Rb, Ra)

	# Case -1 When Player A wins
	# Updating the Elo Ratings
	if (d == 1):
		Ra = Ra + K * (1 - Pa)
		Rb = Rb + K * (0 - Pb)

	# Case -2 When Player B wins
	# Updating the Elo Ratings
	else:
		Ra = Ra + K * (0 - Pa)
		Rb = Rb + K * (1 - Pb)


	
	return round(Ra), round(Rb)
	
    
    


    








