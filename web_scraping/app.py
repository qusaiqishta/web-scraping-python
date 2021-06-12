import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

jobs=[]
companies=[]
locations=[]
skills=[]
links=[]
salaries=[]


# use requests to fetch the url
result=requests.get(input('enter the page URL: '))

# get the page content
src=result.content
#print(src)

# create soup object to parse content 
soup=BeautifulSoup(src,'lxml')  # lxml package enable me to perform proccessing on a page content 


# find the elements(html elements) containing info we need

job_titles=soup.find_all("h2",{"class":"css-m604qf"}) # return the h2 tags with class=css-m604qf , 
company_name=soup.find_all('a',{'class':'css-17s97q8'})
location_name=soup.find_all('span',{'class':"css-5wys0k"})
job_skills=soup.find_all('div',{'class':'css-y4udm8"'})

#loop over the returned lists to extract the needed text

for i in range(len(job_titles)-1):
    jobs.append(job_titles[i].text)
    links.append(job_titles[i].find('a').attrs('href'))
    companies.append(company_name[i].text)
    locations.append(location_name[i].text)
   

#print(jobs)    

# crate csv file and fill it with values
file_list=[jobs,companies,locations,links,salaries]
exported=zip_longest(*file_list)
with open(r'C:\Users\STUDENT\Desktop\Book1.csv','w') as myfile:
    writer=csv.writer(myfile)
    myfile.writerow(['Job Title','Company Name','Job location' ,'Skills needed','links','salaries'])
    myfile.writerows(exported)


# get the needed content in another pages
for link in links:
    result=requests.get 
    src=result.content
    soup=BeautifulSoup(src,'lxml')
    salary=soup.find('div',{'class':'#'})   
    salaries.append(salary.text.strip())

