def getKey():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    return key