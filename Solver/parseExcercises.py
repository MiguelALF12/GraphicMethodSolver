def parseExcercises(excercises):

    #Find item with 'objetivo' and item with 'restricciones' element
    objetivo_index = 0
    restricciones_index = 0
    for item in excercises:
        if 'objetivo' in item:
            objetivo_index = excercises.index(item)

        if 'restricciones' in item:
            restricciones_index = excercises.index(item)
            break
    #parsing 'objetivo', assuming it will be only one
    excercises[objetivo_index][1] = excercises[objetivo_index][1].split('_')
    # parsing 'restricciones', assuming it will be more than one
    for item in excercises[restricciones_index][1:]:
        restriction_index = excercises[restricciones_index].index(item)
        excercises[restricciones_index][restriction_index] = item.split('_')





