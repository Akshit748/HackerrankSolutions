def minion_game(string):
    # game mechanics
    string=string.upper()
    kevscore=stuscore=0
    vowels='AEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            kevscore+=len(string)-i
        else:
            stuscore+=len(string)-i
    #result
    if kevscore>stuscore:
        print("Kevin", kevscore)
    elif stuscore>kevscore:
        print("Stuart", stuscore)
    else:
        print('Draw')

