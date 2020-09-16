def likes(namelist):
    if len(namelist) == 0:
        return "no one likes this"
    elif len(namelist) == 1:
        return namelist[0] + " likes this"

    elif len(namelist) == 3:
        return ", ".join(namelist[:-1]) +" and " + namelist[-1] + " like this"
    elif len(namelist) == 2:
        return " and ".join(namelist) + " like this"
    else:
        return ", ".join(namelist[0:2])+ " and " +    str( len(namelist)-2) + " others like this"
