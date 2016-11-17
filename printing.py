
# Printing functions


import reports

file_name = 'game_stat.txt'
title = 'The Sims 3'
total_copies_sold = '10'
year = '2010'
genre = 'Simulation'
publisher = 'Valve Corporation' 

print("Number of games: %s" % (reports.count_games(file_name)))
print("Is there a game from %s?: %s" %(year, reports.decide(file_name, year)))
print("The latest game on the list is: %s." % (reports.get_latest(file_name)))
print("There is %s game with the genre %s" % (reports.count_by_genre(file_name, genre), genre))
print("The %s game is in the %d-th line." % (title, reports.get_line_number_by_title(file_name, title)))
