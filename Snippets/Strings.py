def Freq(ch):
    ch2=ch.lower()
    st2=st.lower()
    print(f"Frequency of '{ch}' in {st} is '{st2.count(ch2)}'")
    
def ReplaceCh(ch):
    ch2=input(">>>What do you want to replace it with:")
    try:
        st1=st.replace(ch,ch2)
    except:
        print("Invalid Inputs, try again...")
    return st1
        
def RemoveAll(ch,st):
    st=st.replace(ch,"")
    return st
    
def RemoveOnce(ch,st):
    st=st.replace(ch,"",1)
    return st
    
try:
    ch=input(">>>Enter Character:")
    st=input(">>>Enter String:")
    assert len(ch)==1
    Freq(ch)
    Newst= ReplaceCh(ch)
    print("New replaced string:",Newst)
    print(RemoveOnce(ch,st))
    print(RemoveAll(ch,st))
except AssertionError:
    print("ValueOutOfBoundError: Operations can be performed only for Single Characters. Please Enter only Single Charachters")
