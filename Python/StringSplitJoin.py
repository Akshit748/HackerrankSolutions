def split_and_join(line):
    # write your code here
    result = ""
    
    for i in line:
        if i.isspace():
            result += "-"
        else:    
            result += i
    
    return result
    

