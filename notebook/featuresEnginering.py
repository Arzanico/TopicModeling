def descriptionMatch(desc, vs):

    # desc = Descripcion de base type = str
    # vs = la descripcion con la que se comparara type = list

    if type(desc) != str:
        error = "desc no es un string"
        return error
    elif type(vs) != list:
        error = "vs no es una lista"
        return error

    descLi = desc.split()
    descLen = len(descLi)
    matches = dict()

    for li in vs:
        vsLi = li.split()
        match = 0
        for w in vsLi:
            if w in descLi:
                match += 1
            else:
                continue
        # proporcion de macheo
        prop = round((match/descLen), 2)

        matches.update({desc:(prop, li)})

    return matches
