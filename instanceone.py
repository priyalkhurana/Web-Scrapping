from bs4 import BeautifulSoup
import requests
import time

html_text= requests.get('passte url').text
print(html_text)

soup =BeautifulSoup(html_text,'lxml')  

job= soup.find('li', class_ =' write any specific marking')
# in job find something
company= soup.find('h3', class_='specific conditon').text.replace(' ','')

skills=job.find('span', class_=' conditon').ext
print(skills)
print(company)

#to print more efficiently
print(f'''
      {company} is hiring for {skills}.''')


#for say all the jobs
soup =BeautifulSoup(html_text,'lxml')  

jobs= soup.find('li', class_ =' write any specific marking')
# in job find something
for job in jobs:    
    company= soup.find('h3', class_='specific conditon').text.replace(' ','')

    skills=job.find('span', class_=' conditon').ext
    #print(skills)
    print(company)

    #to print more efficiently
    print(f'''
      {company} is hiring for {skills}.''')
    
    more_info=job.header.h2.a['href'] #dot dot refers to pos
    
    #to avoid any spaces
    print(f"company name: {company.strip()}")
    print(f"skills: {skills.strip()}")

#filter out for a conditon
print('Put some skill that you are not familiar with')
unfamiliar_skill=input('>')
print(f'filtering out {unfamiliar_skill}')

#after whole prog
#if unfamiliar_skill not in skills:
    #print


#print every 10 min, put every thing that is extracting info in def find_jobs
## at the end
# if __name__ =='__main__';
#   while True:
#     find_jobs()
#     time.sleep(60*5)#every five minutes


 soup =BeautifulSoup(response.text,'lxml')
        location_elements = soup.find_all("optgroup")
        for location_ele in location_elements:
            label=location_ele.get("Bank Branch")
            options = location_ele.find_all("option")  # Find all the <option> tags within the <optgroup>
            for option in options:
                value = option.get("value")  # Get the value of the "value" attribute
                text = option.text 

                yield{

                }

from bs4 import BeautifulSoup
import requests


html_text= requests.get('https://bandhanbank.com/banking-outlet-locator').text
soup =BeautifulSoup(html_text,'lxml')
location_elements = soup.find_all("optgroup")
for location_ele in location_elements:
    label=location_ele.get("Bank Branch")
    options = location_ele.find_all("option")  # Find all the <option> tags within the <optgroup>
    for option in options:
        value = option.get("value")  # Get the value of the "value" attribute
        text = option.text  # Get the text content within the <option> tag

        # Process the extracted data as per your requirements
        print("Label:", label)
        print("Value:", value)
        print("Text:", text)
        print("----------------------")