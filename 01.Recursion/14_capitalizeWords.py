def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        result.append(arr[0].upper())
        return result + capitalizeWords(arr[1:])

print(capitalizeWords(['jim','rob','adam']))