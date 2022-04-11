from xmlrpc.client import Boolean


my_list = ['Zaid',24,28.35,True,'A',4,25.3,False,'M','T',False]

i=s=f=c=b=0

l_int=[]
l_float=[]
l_bool=[]
l_str=[]
l_char=[]

for item in my_list:
    if type(item)==int:
        i+=1
        l_int.append(item)
    elif type(item)==float:
        f+=1
        l_float.append(item)
    elif type(item)==bool:
        b+=1
        l_bool.append(item)
    elif type(item)==str and len(item)>1:
        s+=1
        l_str.append(item)
    else:
        c+=1
        l_char.append(item)

print(f"The number of Integers in the list are {i} and elements are {l_int}")
print(f"The number of Float in the list are {f} and elements are {l_float}")
print(f"The number of Boolean in the list are {b} and elements are {l_bool}")
print(f"The number of Strings in the list are {s} and elements are {l_str}")
print(f"The number of Characters in the list are {c} and elements are {l_char}")