def my_func(string):
    result = ""
    for k in range(1, len(string) + 1):
        result = result + string[-k]
    return result

# Alternative und sehr elegante Lösung
def my_func(string):
    return string[::-1]
