countries = input().split(", ")
capitals = input().split(", ")
countries_capitals_dict = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in countries_capitals_dict.items():
    print(f"{country} -> {capital}")
