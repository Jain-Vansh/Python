def wrap(string, max_width):
    i=0
    str = ""
    while(i<len(string)):
        str += string[i:i+max_width]
        str += "\n"
        i += max_width
    else:
        str += string[i:len(string)]
    return str