# Joshua Phillips
# 10/28/24
# List Basic Stats

# QUIZ SCORES PRACTICE:
# chemistry_quizes = [98, 79, 83, 91, 62, 95]

# countchemistry_quizes = float(len(chemistry_quizes))

# sumchemistry_quizes = float(sum(chemistry_quizes))

# average = sumchemistry_quizes / countchemistry_quizes
# average_round = round(average, 2)
# print(f'The average quiz score from the stored quizes: {average_round}')

# DRIVING DISTANCES PRACTICE:

distances = [12.64, 14.00, 25.14, 9.38, 14.26]
places = ['Lakes Of North', 'Alba', 'Kalkaska', 'Williamsburg', 'Acme', 'Traverse City']

print(f'The distances for a round trip between citys on the way to Traverse from LOTN are: {distances} all in miles. the locations are in order here: {places}.')
shortest = min(distances)
print(f'The shortest round trip between citys on the way to Traverse from LOTN is: {shortest}miles.')

longest = max(distances)
print(f'The longest round trip between citys on the way to Traverse from LOTN is: {longest}miles.')

total_traveled = sum(distances)
print(f'The sum round trip between citys on the way to Traverse from LOTN is: {total_traveled}mi.')

number_of = len(distances)
average = total_traveled / number_of
print(f'THe average distance between cities in miles is : {average}.')