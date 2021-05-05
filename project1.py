import pandas as pd

#Dictionary of high budget movies
highBudget = {'Avengers: End Game': {'budget': 400000000,'rating': 94},
				'Happy Feet': {'budget': 85000000,'rating': 76},
				'Ready Player One': {'budget': 150000000,'rating': 72},
				'Hansel and Gretel: Witch Hunters': {'budget': 50000000,'rating': 16},
				'Inside Out': {'budget': 175000000,'rating': 98},
				'Prince of Persia: Sands of Time': {'budget': 200000000,'rating': 37},
				'Disney\'s A Christmas Carol': {'budget': 190000000,'rating': 53},
				'Harry Potter and the Half-Blood Prince': {'budget': 250000000,'rating': 84},
				'Inception': {'budget': 160000000,'rating': 87},
				'Wonder Woman': {'budget': 150000000,'rating': 93},
				'Trolls': {'budget': 125000000,'rating': 75},
				'The Revenant': {'budget': 135000000,'rating': 78},
				'Ocean\'s Twelve': {'budget': 110000000,'rating': 54},
				'Sonic The Hedgehog': {'budget': 90000000,'rating': 63},
				'The Secret Life of Pets': {'budget': 75000000,'rating': 72},
				'Furious 7': {'budget': 190000000,'rating': 82},
				'Couples Retreat': {'budget': 60000000,'rating': 10},
				'Zero Dark Thirty': {'budget': 52500000,'rating': 91},
				'The Book of Eli': {'budget': 80000000,'rating': 46},
				'Jurassic World': {'budget': 215000000,'rating': 70}}

#Dictionary of low budget movies
lowBudget = {'Ready or Not': {'budget': 6000000, 'rating': 88},
				'The Gatekeepers': {'budget': 15000000,'rating': 94},
				'47 Meters Down': {'budget': 5300000,'rating': 52},
				'Departure': {'budget': 1100000,'rating': 86},
				'Whiplash': {'budget': 3300000,'rating': 94},
				'Indivisible': {'budget': 2700000,'rating': 74},
				'The Invitation': {'budget': 1000000,'rating': 89},
				'It Follows': {'budget': 2000000,'rating': 95},
				'Searching': {'budget': 880000,'rating': 92},
				'Pheonix Forgotten': {'budget': 2800000,'rating': 42},
				'The Bounce Back': {'budget': 3000000, 'rating':67},
				'The Gift': {'budget': 5000000, 'rating': 91},
				'Cheap Thrills': {'budget': 100000, 'rating': 88},
				'Silent House': {'budget': 2000000, 'rating': 43},
				'Grace Unplugged': {'budget': 1700000, 'rating': 50},
				'Pink Ribbons, Inc.': {'budget': 1200000, 'rating': 89},
				'Overcomer': {'budget': 5000000, 'rating': 53},
				'Area 51': {'budget': 5000000, 'rating': 14},
				'The Boy Next Door': {'budget':4000000,'rating': 12},
				'The Purge': {'budget': 3000000,'rating': 39}}

#Printing the highBudget dictionary
print('\n')
print('HIGH BUDGET MOVIES')
df = pd.DataFrame(highBudget).T
print(df)

#Printing the lowBudget dictionary
print('\n')
print('LOW BUDGET MOVIES')
df2 = pd.DataFrame(lowBudget).T
print(df2)
print('\n')

#Adding up the rating values in the highBudget dictionary
sum1 = 0
for key, value in highBudget.items():
	if value and 'rating' in value.keys():
		sum1 += value['rating']

#Calculating the average
highAverage = float(sum1 / 20)
print("The average rating for the high budget movies is " +str(highAverage)+ "%.")

#Adding up the rating values in the lowBudget dictionary
sum2 = 0
for key, value in lowBudget.items():
	if value and 'rating' in value.keys():
		sum2 += value['rating']

#Calculating the average
lowAverage = float(sum2 / 20)
print("The average rating for the low budget movies is " +str(lowAverage)+ "%.")

			