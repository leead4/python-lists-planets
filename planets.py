
planet_list = ["Mercury", "Mars"]
# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
# Use the extend() method to add another list of the last two 
# planets in our solar system to the end of the list.
end_two =["Uranus", "Neptune"]
planet_list.extend(end_two)
# Use insert() to add Earth, and Venus in the correct order.

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
# Use append() again to add Pluto to the end of the list.

planet_list.append("Pluto")

# Now that all the planets are in the list, slice the list 
# in order to get the rocky planets into a new list called 
# rocky_planets.
# Being good amateur astronomers, we know that Pluto is now a dwarf planet,
 # so use the del operation to remove it from the end of 
 # planet_list.

rocky_planets = planet_list[0:4]
print("rocky", rocky_planets)
print("pluto spot", planet_list.index("Pluto"))
del planet_list[8]
print("planetList", planet_list)




# Create another list containing tuples. 
# Each tuple will hold the name of a spacecraft 
# that we have launched, and the names of the planet(s) 
# that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
# Iterate over your list of planets, and inside that loop, 

# iterate over the list of tuples. 
# Print, for each planet, which sattelites have visited.
# 

list_o_tups = [('craft1', 'Earth'),('craft2', 'Venus'),('craft3', 'Saturn'),('craft4', 'Mercury'),('craft5', 'Neptune')]
print("tups", list_o_tups)


# visited_list = list()
for potato in planet_list:
	planet_name = potato
	# visited_list.append(planet_name)

	# print("potato", planet_name)
	
	for stuff in list_o_tups:
		# print("stuff", stuff)
		craft_name = stuff[0]
		name_name = stuff[1]
		# visitor_list = list()
		if name_name == planet_name:
			print(planet_name)
			# print("------------------")
			print(craft_name)
			print("------------------")
			# visitor_list.append(craft_name)
			# visited_list.append(craft_name)







			





