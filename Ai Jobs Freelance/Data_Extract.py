# Maded By Me without AI :) My old Skill Webscraping
#----------------------------
# why am i using this ? , to help me to train my LLM model to analaying and comparing data
import csv
from itertools import zip_longest
from seleniumbase import sb_cdp
#-------------------------
# Based on real Data from mostaql website
#-------------
website = 'https://mostaql.com/projects?category=ai-machine-learning&sort=latest'
sb = sb_cdp.Chrome()
sb.goto(website)

print('Loading First Page.........')
Projects = sb.find_elements('div.card--title h2.mrg--bt-reset' , timeout=5)
links = sb.find_elements('div.card--title h2.mrg--bt-reset a', timeout=5)
oweners = sb.find_elements('li.text-muted bdi', timeout=5)
posted_date = sb.find_elements('li.text-muted time', timeout=5)

#-------------
# First Page requirements 
Titles = []
Links = []
#----
Oweners = []
Posted_Dates = []
#-------------
# Second Page requirements
Descriptions = []
Skills = []
Salarys = []
Proposals = []

print('First page --success-- !')

for p in range(len(Projects)) : 
    page = links[p].get_attribute('href')
    Links.append(page)
    Titles.append(Projects[p].text)
    Oweners.append(oweners[p].text)
    Posted_Dates.append(posted_date[p].text)

#-----------
# Second page :

print('Second Page :')

for l in range(len(Links)) :
     
    print(f'Extract Data ....({len(links)}|{l+1})')

    sb.open(Links[l])
    #---------------- 
    description = sb.find_element('div.text-wrapper-div.carda__content ', timeout=5).text
    Descriptions.append(description)

    skills = sb.find_elements('ul.skills.text-zeta.list-tags li.skills__item', timeout=5)
    Skills.append(' | '.join(s.text for s in skills))

    salary = sb.find_element("div.meta-row div.meta-value [data-original-title='الميزانية المقترحة للمشروع'] ", timeout=5)
    Salarys.append(salary.text)

    proposals = sb.find_elements('div.bid.list-group-item.pdn--vm ', timeout=5)
    Proposals.append(len(proposals))

#------------------------
#------------------------
# Save to CSV using zip_longest

columns = {
    'Titles': Titles,
    'Links': Links,
    'Owners': Oweners,
    'Posted_Dates': Posted_Dates,
    'Descriptions': Descriptions,
    'Skills': Skills,
    'Salarys': Salarys,
    'Proposals': Proposals,
}

with open('freelance_ai_jobs.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(columns.keys())                                   # column names
    writer.writerows(zip_longest(*columns.values(), fillvalue=''))    # rows