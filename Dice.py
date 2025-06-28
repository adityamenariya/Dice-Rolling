#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
d=[1,2,3,4,5,6,6,3,1]
k=random.choice(d)
k
l=[]

player=int(input("Enter total player :"))
i=0
while i<player:
    pname=input("enter a player name :")
    l.append(pname)
    i=i+1
move=int(input("press 1 for start game"))
while True:
    
    
    if move==3 or move==1:

        for i in l:
            k=random.choice(d)
            print()
            move=int(input(f"press 3 for {i} chance..."))
            print()

            print(i)
            print(k)
            
            if k==6:
                k=random.choice(d)
                print()
                move=int(input(f"press 3 for {i} chance..."))
                print()
                print(i)
                print(k)
                    
                
                if k==6:
                    k=random.choice(d)
                    print()
                    move=int(input(f"press 3 for {i} chance..."))
                    print()
                    print(i)
                    print(k)
    else:
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




