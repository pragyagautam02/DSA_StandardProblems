def strengthPassword(passw):
    i = 0
    j = 1
    strength = 0
    vowel_set = {'a','e','i','o','u'}
    vowel = 0
    cons = 0
    while(i<len(passw)):
        if passw[i] in vowel_set:
            vowel += 1
        else:
            cons += 1

        if vowel and cons:
            strength += 1
            vowel = 0
            cons = 0
        i+=1

    return strength

passw = "thisisbeautifulplace"   
print(strengthPassword(passw))      
