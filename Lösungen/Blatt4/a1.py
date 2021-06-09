def merge_dict(first_dict, second_dict):
    result = {}
    for key, value in first_dict.items():
        result[key] = value
    for key, value in second_dict.items():
        result[key] = value
    return result
