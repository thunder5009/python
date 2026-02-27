#lst=[1,2,3]
#ans=[]
#for i in lst:
#    ans.append(i*i)
#print(ans)
#ans=[i**2 for i in lst]  
#print(ans)
#lst_name=['dhruv','parthiv']
#lst_upper=[i.upper() for i in lst_name ]
#print(lst_upper)
#lst_city=['ahmedabad','rajkot']
#lst_len=[len(i) for i in lst_city]
#print(lst_city)
#for i in lst:
#    if i%2==0:
#       ans1.append(i**2)
#print("Square of even number ", ans1)
#ans1=(i**2 for i in lst if i%2==0)
#print("Square of even numbers ",ans1)
lst_city=['ahmedabad','rajkot']
ans2=[]
ans2=[i.upper() for i in lst_city if len(i)>5]
print(ans2)
        