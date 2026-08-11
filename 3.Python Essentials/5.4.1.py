with open('us_cities.txt', 'r') as data_file:
    for line in data_file:
        city, population = line.split(':')         #
        city = city.title()                       
        population = f'{int(population):,}'     
        print(city.ljust(15) + population)
data_file.close()