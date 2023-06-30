from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    print(content)

    soup= BeautifulSoup(content,'lxml')
    print(soup.prettify()) #used to print content of web page in a pretty way

    #grabbing specific tabs, say h5(h5 are sort of hidden)
    tags=soup.find('h5') #gives the first one
    print(tags)
    tags=soup.find_all('h5') #gives all

    #to find something specific
    courses_html_tags= soup.find_all('h5')
    for courses in courses_html_tags:
        print(courses.text) #prints names of courses

    #filtering to get more specific info
    soup=BeautifulSoup(content,'lxml')
    course_cards= soup.find_all('div', class_='card')
    for courses in course_cards:
        course_name=courses.h5.text #converts in text
        course_price= courses.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

#over


