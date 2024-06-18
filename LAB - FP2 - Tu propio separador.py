def mysplit(strng):
    if strng == '' or strng.isspace() == True:
        return [ ]
    str_ = []
    new_c = ''
    record = (not strng[0].isspace())
    for c in strng:
        if record:
            if not c.isspace():
                new_c = new_c + c
            else:
                str_.append(new_c)
                record = not True
        else:
            if c.isspace() == False:
                record = not False
                new_c = c
            
    if record == True:
        str_.append(new_c)

    return str_


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    
