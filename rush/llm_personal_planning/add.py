def add(records):    
    key = input('Key: ')
    value = input('Value: ')

    if key != None and value != None:
        records.update({key: value})

    return records