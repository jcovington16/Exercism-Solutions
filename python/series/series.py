def slices(series, length):
    results = []
    if len(series) < length:
        raise ValueError("The length number is larger length of series number")
    if length < 1:
        raise ValueError("Length is not a positive number")
    for i in range(len(series) - length + 1):
        results.append(series[i:i+length])
    return results
