countries_data = {
    'RU': ['white', 'blue', 'red'],
    'US': ['red', 'white', 'blue'],
    'CA': ['red', 'white'],
    'GB': ['red', 'white', 'blue'],
    'FR': ['blue', 'white', 'red'],
    'DE': ['black', 'red', 'gold'],
    'IT': ['green', 'white', 'red'],
    'CN': ['red', 'yellow'],
    'KG': ['red', 'yellow']
}


while True:
    values_to_search = input("Введите цвета флага через пробел (например, 'red white blue'): ").split()
    
    matching_countries = []

    for country_code, flag_colors in countries_data.items():
        if all(color in flag_colors for color in values_to_search):
            matching_countries.append(country_code)

    if matching_countries:
        print(f"Страны, у которых флаг содержит все указанные цвета: {', '.join(matching_countries)}")
    else:
        print("Страны с такими флагами не найдены.")
