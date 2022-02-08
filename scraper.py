
#Scraper

from ast import dump
from statistics import mean
from turtle import title
import requests
from bs4 import BeautifulSoup
import csv
import json
#This was before I was going to parse through the nav href it is not needed right now 
pagenum=1
letter_counter=1
letter="a"
firstname = []
usage = []
means = []
gender = []
jsonList = []
full_related = []
endnum = -2
    
while pagenum != endnum +1:
    print("This is the page number: ", pagenum)
    #gets the URL needed to gather the information
    URL = "https://behindthename.com/names/letter/" + letter +"/"+ str(pagenum)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    nav = soup.find_all(class_="pgblurb")
    for line in nav:
        for let in line:
            for f in let:
                if f == "f":
                    endnum= int(let[30])
    results = soup.find_all( class_="nll")
    #print(results)








    #This gathers the list of related names for a single name and stores the (rel) list of related names into the full_related list
    
    #The name itself
    numb = 0
    for name in results:  
        #print(name)
        
        for i in name:
            if str(i) != '<span class="nn">1</span>' and str(i) != '<span class="nn">2</span>' and str(i) != '<span class="nn">3</span>' and str(i) != '<span class="nn">4</span>' and str(i) != '<span class="nn">5</span>':
                firstname.append(i)
                #print(i)
                numb= numb+1
                
            #print('<span class="nn">1</span>')
            
           
                #numb= numb+1
        #if len(results[numb]) == 1:
            
            #NAMES IS AT 308 needs to be at 300 why is there 8 more SPANS???
                    
            
    print("Firstname Count importing from Website... " ,numb)



    #This gets the gender of each of the names 
    
    fem = "F"
    masc = "M"
    genders= soup.find_all(class_="listgender")
    count =0
    for i in genders:
        
        #FIX THIS A GENDER CAN BE BOTH 
        if len(genders[count]) > 1:
            gender.append("M & F")
        else:
            for l in i:
                for t in l:
                    if t =="f":
                        gender.append(fem)
                    else:
                        gender.append(masc)
        #print(genders)
        count =count+1
    print("Gender Count importing from website... " ,count)
    #print(gender)
       
                
            
            
        

    #This section gets the usage of the name
    #The usage of where the name comes from
    meaning = soup.find_all(class_="listusage")
    legit= 2
    now=0
    
    check = 0
    for t in meaning:
        check = check +1
        if len(t) == 1:
            
            for i in t:
                for g in i:
                    usage.append(g)
        elif len(t) > 1:
            multi=[]
            for m in t:
                for u in m:
                    if u == "," or u == " ":
                        now = now+1
                    elif now ==2:
                        usage.append(multi)
                        
                    
                    elif now !=2:
                        if m != ",":
                            now = now+1 
                            multi.append(u)
                    elif now ==2:
                        
                        multi.append(u)
                        now = 0
            usage.append(multi)
    print("Final check boiii", len(usage))
                    
        
    print("This is the meanings check", check)           
        
          

    """
    full_related =[]
    rel = []
    #n is each name from the firstname list already gathered
    #Then adds the name to find the URL 
    #That could be the issue of slowing down because I am requesting this page over and over 
    for n in firstname:

        name_URL = "https://www.behindthename.com/name/" +n+"/related"
        page = requests.get(name_URL)
        
        related = BeautifulSoup(page.content, "html.parser")
        relate = related.find_all(class_= "nlc", text =True)
        for i in relate:
            for l in i:
                rel.append(l)
    print(rel)

    full_related.append(rel)   
        #print(full_related) 

    """
    
   
    with open("tester.json", "w") as f:
        
        
        for i in range(0,len(firstname)):
            jsonList.append({ "Usage" : usage[i] , "FirstName": firstname[i],"Gender": gender[i]})
            #jsonList.append({"Full_Names": rel})


        json.dump(jsonList, f)
        
    
    pagenum = pagenum+1
