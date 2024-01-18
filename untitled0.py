# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:23:30 2024

@author: 34894
"""

import csv

# *****problem 1
def cardinality_items( filename):
    auxSet=set()  #initialize a empty set;
    with open(filename,'r') as file:
        curCsv=csv.reader(file)
        for line in curCsv:  #for every line of record in .csv, add elements into set
            for word in line:
                auxSet.add(word.strip())  
    print(len(auxSet))  #length of set is number of different element in .csv
    print(auxSet)
    return auxSet

# *****problem 2
def aux_all_itemsets(items,idx,k):
    n=len(items)
    if(k==1):
        return[[items[idx]]]
    ans=[]
    temp=[]
    tmp=idx
    while(tmp<=n-k):
        temp=aux_all_itemsets(items, tmp+1, k-1)
        for e in temp:
            e.append(items[idx])
        tmp+=1
        ans+=temp
    return ans;


def all_itemsets(items, k):
    n=len(items)
    ans=[]
    for i in range(0,n-k+1):
        ans+=aux_all_itemsets(items,i,k)
    return ans


# *****problem 3
def countingRecord(filePath):
    count=0
    curSet=set()
    early=2050
    old=1900
    with open(filePath,'r') as file:
        for line in file:
            if line.strip().endswith(':'):
                continue;
            count+=1;
            l=line.split(',')
            
            tmp=int(l[2][0:4])
            if(tmp<early):
                early=tmp
            elif(tmp>old):
                old=tmp
            curSet.add(int(l[0]))
                
    file.close()
    return count,curSet,early,old
                
def problem_3():
    count=0;
    early=2050
    old=1900
    usr=set()
    filePath='archive/combined_data_'
    for i in range(1,5):
        c,s,e,o=countingRecord(filePath+str(i)+'.txt')
        usr=usr|s
        if(old<o):
            old=o
        if(early>e):
            early=e
        count+=c
    print('number of records: ' ,count ,' unique users: ' ,len(usr) ,' range of year: ', early,'-',old)
    
    
    
def problem_4():
    movie=dict()
    check=set()
    count=0
    with open('archive/movie_titles.csv',encoding='iso-8859-1') as file:
        for line in file:
          l=line.split(',',2)
          
          name=l[2].strip()
          print (name)
          check.add(name)
          if name in movie:
            movie[name]=movie[name]+1
            if(movie[name]==4) :
              count+=1
            elif(movie[name]==5):
              count-=1
          else :
            movie[name]=1
    file.close()
    return len(check),count


def problem_5():
  usr=dict()
  qualifiedID=set()
  filepath='archive/combined_data_'
  cur=-1
  for i in range(1,5):
    with open(filepath+str(i)+'.txt') as file:
      for line in file:

        l=line.split(',')

        if len(l)==1:
          cur=int(line.strip()[:-1])
          continue

        id=int(l[0].strip())
        score=int(l[1].strip())
        if id in usr:
          usr[id][0]=usr[id][0]+1
          if(usr[id][0]==200):
            qualifiedID.add(id)
          elif(usr[id][0]==201):
            qualifiedID.remove(id)
        else:
          usr[id]=[1,[]]
        if(score==5):
          usr[id][1].append(cur)
    file.close()
  favorateMovie=set(usr[min(qualifiedID)][1])
  favorateName=[]
  print(len(qualifiedID))
  with open('archive/movie_titles.csv',encoding='iso-8859-1') as file:
    for line in file:
      id=int(line.split(',')[0])
      name=line.split(',')[2]
      if(id in favorateMovie):
        favorateName.append(name)
  file.close()


  print(min(qualifiedID))
  return favorateName,len(qualifiedID)




if __name__=='__main__':
    #problem_3()
    #print(problem_4())
    #print((all_itemsets(list(cardinality_items('basket_data.csv')),5)))
    #print(all_itemsets( ["ham", "cheese", "bread"],2))
    problem_5()
    