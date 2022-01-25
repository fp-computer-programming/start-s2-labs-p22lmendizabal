#author: LM (AMDG) 1/24/22
def comes_after(st, l):
    #setting variables both upper and lower case

    lowercase = ("abcdefghijklmnopqrstuvwxyz") 
    uppercase = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #this is a blank string 
    return_st = ""
    #for loop to iterate through lower case letters
    if l in lowercase:
        #new variable that sets letters the same
        l_shift = uppercase[lowercase.index(l)]
    else:
        l_shift = lowercase[uppercase.index(l)]
        #for loop to go through string. n - 1    
    for i in range(len(st)-1):
        #if letter index value equals letter or equals l shift     
        if st[i] == l or st[i] == l_shift:
            #then if  next index is in the lower or uppercase variable then it adds that to the empty string
            if st[i+1] in lowercase or st[i+1] in uppercase:
                return_st += st[i+1]
    return return_st

print(comes_after('meellele', 'e'))