def swap_case(s):
    temps=''
    for i in s:
        if i.isalpha():
            if i.islower():
                temps+=i.upper()
            else:
                temps+=i.lower()
        else:
            temps+=i
    return temps
    

