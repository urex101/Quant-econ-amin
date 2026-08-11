data_file = open('us_cities.txt', 'r')
for line in data_file:
    city, population = line.split(':')         #
    city = city.title()                       
    population = f'{int(population):,}'     
    print(city.ljust(15) + population)
data_file.close()