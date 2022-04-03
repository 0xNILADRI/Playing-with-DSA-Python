def collectStrings(obj):
    # TODO
    result = []
    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        if type(obj[key]) is dict:
            result = result + collectStrings(obj[key])
    return result

obj1 = {
    "num" : '1',
    "test": [],
    "data":{
        "val" : '4',
        "info" : {
            "isRight" : True,
            "random" : '66'
        }
    }
}

print(collectStrings(obj1))