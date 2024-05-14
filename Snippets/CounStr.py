def CountStr(s1,s2):
    String_Found= False
    indx=[]
    for i in range(len(s1)):
        if s1[i:i + len(s2)] == s2:
            indx.append(i)
            String_Found = True
 
    if String_Found == False:
        return -1
    else:
        return indx
print(CountStr("svdcsfgvshfvukwhkwufhuihfuihf","v"))          
        
