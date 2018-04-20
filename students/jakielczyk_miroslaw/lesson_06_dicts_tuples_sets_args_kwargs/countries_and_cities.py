n = int(input())
country_and_cities_dict = dict()
for _ in range(n):
    country_and_cities = input().split(' ')
    country_and_cities_dict[country_and_cities[0]] = \
        country_and_cities[1:]

number_of_cities = int(input())
for _ in range(number_of_cities):
    name_of_city = input()
    for country, cities in country_and_cities_dict.items():
        if name_of_city in cities:
            print(country)
