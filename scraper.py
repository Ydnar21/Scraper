
from statistics import mean
from turtle import title
import requests
from bs4 import BeautifulSoup
import csv
import json
pagenum=2

letter_counter=1
letter="a"
firstname = []
usage = []
means = []
jsonList = []
#for num in pagenum:
        #pages=10
    #for i in pages
    

    
URL = "https://behindthename.com/names/letter/a/" 
try:
    page = requests.get(URL)
except print("End of "):
    pass



soup = BeautifulSoup(page.content, "html.parser")
#print(soup)


mean = soup.find_all(class_="mng")
#print(mean)
results = soup.find_all( class_="nll",href =True, text=True)

for m in mean:
    
    for u in m:
        
        means.append(u)
#print(means)


full_related = []
#The name itself
for name in results:
    for realname in name:
        firstname.append(realname)
    


#must get the genders 
gender = []
fem = "F"
masc = "M"
genders= soup.find_all(class_="listgender")
for i in genders:
    for g in i:
        for t in g:
            if t == "f":
                gender.append(fem)
            if t == "m":
                gender.append(masc)
        
        
    
    
"""
#gender.append(fem)
#print(gender)
#else:
#gender.append(Male)
"""

#The usage of where the name comes from
meaning = soup.find_all(class_="listusage")
for t in meaning:
    for u in t:
        for i in u:
            if i == "," or i == " ":
                pass
            else:
                usage.append(i)   





"""
#to find related names

for i in firstname:
    
    URL = "https://www.behindthename.com/name/" +i +"/related"
    page = requests.get(URL)

    rel = []
    related = BeautifulSoup(page.content, "html.parser")
    relate = related.find_all(class_= "nlc")
    for m in relate:
        for w in m:
            if w == " ":
                pass
            else:

                #print(w)
                rel.append(w)
                #print(related)


    #full_related.append(rel)   
    #print(full_related) 
        """
        




with open('tester.json', "w") as f:
    #dumping to a json file
    
    for i in range(0,len(firstname)):
        jsonList.append({ "Usage" : usage[i] , "FirstName": firstname[i],"Gender": gender[i]})
        


    json.dump(jsonList, f)



    #print(job_elements)
