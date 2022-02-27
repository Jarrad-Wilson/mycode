#!/usr/bin/env python3
anime = ['naruto', 'bleach', 'one_piece']
manhua = ['solo_leveling', 'overgeared', 'legend_of_the_northern_blade']

print(anime) #print top 3 anime 
print(manhua) #print top 3 manhua

anime.append('hunter_x_hunter')
print(anime)

anime.extend(manhua)
print(anime) # adds favorit manhua to favorite anime list


print(anime)
print(manhua)
