flat_number = 4
entrances = 5
count_flats_in_entrance = 20
count_flats_in_level = 4

flat_entrance = flat_number // count_flats_in_entrance + 1
flat_level = (flat_number % count_flats_in_entrance) // count_flats_in_level

print('flat_entrance = ', flat_entrance,  'flat_level = ', flat_level) 
