def mutate_string(string, position, character):
    result=''
    for i in range(len(string)):
        if i==position:
            result+=character
        else:
            result+=string[i]
    return result

