#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
print(os.getcwd())

datadir='D:\\Projects\\AngelHack\\python\\'
print(datadir)


# In[2]:


f = open(datadir + 'testdata-01.txt', 'r')
contents = f.readline()
contentsplit=contents.split('\t')
print(contentsplit)
print(f.read())
f.closed


# In[3]:


events=[]
filepath = datadir + 'testdata-01.txt'
with open(filepath) as fp:  
    for cnt, line in enumerate(fp):
        linestripped=line.strip()
        linesplit=linestripped.split('\t')
        events.append(linesplit)
        # print(cnt, linesplit)
print(events)


# In[12]:


agentsextract=[]
for cnt, line in enumerate(events):
    agentsextract.append(line[0])
# print(agentsextract)
agentlist = list( dict.fromkeys(agentsextract) )
print(agentlist) 

intervalextract=[]
for cnt, line in enumerate(events):
    intervalextract.append(line[1])
# print(agentsextract)
intervallist = list( dict.fromkeys(intervalextract) )
print(intervallist) 

placeextract=[]
for cnt, line in enumerate(events):
    placeextract.append(line[2])
# print(agentsextract)
placelist = list( dict.fromkeys(placeextract) )
print(placelist) 


# In[46]:



agent = 'Bob'   # agent 'fixed'
print( 'Agent is  ' , agent )
for cnt, interval in enumerate(intervallist): # Iterate over Interval list
    print( agent,  " at Interval:",  interval )
    for cnt2, agentother in enumerate(agentlist): # Iterate over Agent list
        
        if agent != agentother:
            # print( cnt2, agentother  )
            # print( agent != agentother , agent, agentother )
        
            
            for cnt3, event in enumerate(events):  #Find place of current agent
                if event[0] == agent and event[1] == interval:
                    # print(event)
                    agentplace = event[2]
    print('Agent ', agent, ' is at ', agentplace)
    
    score = 0
    for cnt4, event in enumerate(events):  #Find  other agent at place at that interval
        
        if event[1] == interval and event[2] == agentplace and event[0] != agent:
            print( "  ", event[0], ' is also at '  , event[2] )
            score = score + 1
        
    print( agent, ' exposure score during ', interval, ' at ', agentplace,  ' is ' , score)
    print()
            
        


# print( agents)


# In[ ]:





# In[ ]:




