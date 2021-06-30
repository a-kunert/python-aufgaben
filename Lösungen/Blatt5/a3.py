def filter_countries_by_regions(countries, regions):
    result = []
    for country in countries:
        if country["region"] in regions:
            result.append(country)
    return result
