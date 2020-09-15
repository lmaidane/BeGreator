import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
from nltk.util import ngrams
import os
import docx2txt
from geopy.geocoders import Nominatim
from geotext import GeoText
from geopy.distance import great_circle
from datetime import datetime
from datetime import date
import json
import urllib.request as request
import requests
import sys

#Reading the job information
#response = requests.get("https://jsonplaceholder.typicode.com/todos")
#single_company_data = json.loads(response.text)

input_filename=sys.argv[1]

with open(input_filename, "r") as read_file:
    single_company_data = json.load(read_file)

job_title=single_company_data['Mission title']

job_language=single_company_data['Languages']
job_languages=list(job_language.split("; "))

job_skill=single_company_data['Hard skills']
job_skills=list(job_skill.split(" ; "))

job_skill_level=single_company_data['Level of experience']
job_skills_level=list(job_skill_level.split(" ; "))

job_date=single_company_data['Mission length']
job_dates=list(job_date.split(" to "))

current_date = date.today()

job_start_date=datetime.strptime(job_dates[0], "%Y-%m-%d")
job_end_date=datetime.strptime(job_dates[1], "%Y-%m-%d")
job_current_date=datetime.strptime(str(current_date), "%Y-%m-%d")

start_date_day=job_start_date.day
start_date_month=job_start_date.month
start_date_year=job_start_date.year

end_date_day=job_end_date.day
end_date_month=job_end_date.month
end_date_year=job_end_date.year

current_date_day=job_current_date.day
current_date_month=job_current_date.month
current_date_year=job_current_date.year

from datetime import date
d0 = date(start_date_year,start_date_month,start_date_day)
d1 = date(end_date_year,end_date_month,end_date_day)
delta = d1 - d0
job_days=delta.days

d2 = date(start_date_year,start_date_month,start_date_day)
d3 = date(current_date_year,current_date_month,current_date_day)
delta1 = d2 - d3
job_days1=delta1.days

job_location=single_company_data['Location']

job_work=single_company_data['Work regime']

job_industry=single_company_data['Industry']

job_daily_rate=single_company_data['Daily Rate']
job_daily_rate=int(job_daily_rate)

job_company_size=single_company_data['Company size']

job_tech_stack=single_company_data['Tech stack']
tech_stack=list(job_tech_stack.split(" ; "))

job_remote=single_company_data['Remote work']

mission_constraint=single_company_data['Mission constraint']

#Reading the Profiles information
job_information_data=pd.read_csv("Sample profiles & job descriptions - Profiles.csv")
job_information_dataframe=pd.DataFrame(job_information_data)
count=[]
matching_title_list=[]
not_matching_title_list=[]
matching_languages_list=[]
not_matching_languages_list=[]
matching_skills_list=[]
not_matching_skills_list=[]
matching_duration=[]
not_matching_duration=[]
not_matching_work_regime=[]
matching_work_regime=[]
matching_location=[]
not_matching_location=[]
matching_industry=[]
not_matching_industry=[]
matching_daily_rate=[]
not_matching_daily_rate=[]
matching_company_size=[]
not_matching_company_size=[]
matching_tech_objectives=[]
not_matching_tech_objectives=[]
matching_availability=[]
not_matching_availability=[]
matching_constraint=[]
not_matching_constraint=[]

#loop runs for each profile
for i in range(1,51):
    single_profile_data=job_information_dataframe['Profile {}'.format(i)]
    single_profile_data=list(single_profile_data)
    
    #title matching
    title=single_profile_data[0]
    titles = list(title.split("; "))
    counts=0
    matching_title=" "
    for j in range(len(titles)):
        if(job_title==titles[j]):
            counts=counts+1
            matching_title=job_title
            matching_title_list.append(matching_title)
            not_matching_title_list.append(" ")
    if(matching_title==' '):
        matching_title_list.append(" ")
        not_matching_title_list.append(job_title)
    count.append(counts)
    
    #languages matching
    language=single_profile_data[3]
    languages=list(language.split("; "))
    counts=0
    lang=''
    not_lan=''
    for j in range(len(job_languages)):
        lan=" "
        for k in range(len(languages)):
            if(job_languages[j]==languages[k]):
                counts=counts+3
                lan=job_languages[j]
                lang=lang+job_languages[j]+' '
        if(lan==" "):
            not_lan=not_lan+job_languages[j]
    not_matching_languages_list.append(not_lan)
    matching_languages_list.append(lang)
            
    count[i-1]=count[i-1]+counts
    
    #skills
    skill=single_profile_data[1]
    skills=list(skill.split(" ; "))
    level=single_profile_data[2]
    levels=list(level.split("; "))
    counts=0
    exp_count=0
    skill_string=''
    not_skill_string=''
    
    for j,k in zip(job_skills,job_skills_level):
        current=''
        for l,m in zip(skills,levels):
            if(j==l and k<=m):
                counts=counts+7
                exp_count=exp_count+1
                skill_string=skill_string+j+' '+k+' '
                current=j+' '+k
        if(current==''):
            not_skill_string=not_skill_string+j+' '+k+' '
    matching_skills_list.append(skill_string)
    not_matching_skills_list.append(not_skill_string)
            
    count[i-1]=count[i-1]+counts
    
    #duration
    duration=single_profile_data[11]
    counts=0
    if(duration=="< 6 months"):
        if(job_days<=210):
            counts=counts+1
            matching_duration.append(str(job_days)+" days")
            not_matching_duration.append(" ")
        else:
            not_matching_duration.append(str(job_days)+" days")
            matching_duration.append(" ")
    elif(duration=="> 12 months"):
        if(job_days>=360):
            counts=counts+1
            matching_duration.append(str(job_days)+" days")
            not_matching_duration.append(" ")
        else:
            not_matching_duration.append(str(job_days)+" days")
            matching_duration.append(" ")
    elif(duration=="6 to 12 months"):
        if(160<=job_days<=380):
            counts=counts+1
            matching_duration.append(str(job_days)+" days")
            not_matching_duration.append(" ")
        else:
            not_matching_duration.append(str(job_days)+" days")
            matching_duration.append(" ")        
    count[i-1]=count[i-1]+counts  
    
    #work regime
    work_regime=single_profile_data[8]
    counts=0
    if(job_work==work_regime):
        counts=counts+1
        matching_work_regime.append(job_work)
        not_matching_work_regime.append(" ")
    else:
        counts=0
        matching_work_regime.append(" ")
        not_matching_work_regime.append(job_work)        
        
    count[i-1]=count[i-1]+counts 
    
    #remote and location
    places=[]
    latitude=[]
    longitude=[]
    location_string=''
    location=single_profile_data[5]
    remote=single_profile_data[9]
    travel_dist=single_profile_data[13]
    travel_dist=int(travel_dist)
    counts=0
    if(job_remote=="Remote"):
        if(remote=="Yes"):
            counts=counts+1
            matching_location.append("Remote")
            not_matching_location.append(" ")
        elif(remote=="No"):
            counts=0
            matching_location.append(" ")
            not_matching_location.append("Remote")
    elif(job_remote=="On-site with some remote days"):       
        places.append(job_location)
        places.append(location)
        geolocator = Nominatim(user_agent="http")
        for q in range(len(places)):
            locate = geolocator.geocode(places[q])
            latitude.append(locate.latitude)
            longitude.append(locate.longitude)

        first = (latitude[0], longitude[0])
        second = (latitude[1], longitude[1])
        location_string=location+' '+str(great_circle(first, second).km)
        if(int(great_circle(first, second).km)<=travel_dist):
            counts=counts+1
            matching_location.append(location_string)
            not_matching_location.append(" ")
        elif(int(great_circle(first, second).km)>travel_dist):
            counts=0
            matching_location.append(" ")
            not_matching_location.append(location_string)
    count[i-1]=count[i-1]+counts
    
    #industry
    industry=single_profile_data[6]
    industries=list(industry.split("; "))
    counts=0
    for j in range(len(industries)):
        if(job_industry==industries[j]):
            counts=counts+1
            matching_industry.append(job_industry)
            not_matching_industry.append(" ")
    if(counts==0):
        matching_industry.append(" ")
        not_matching_industry.append(job_industry)
    count[i-1]=count[i-1]+counts
    
    #daily_rate
    daily_rate=single_profile_data[7]
    daily_rate=int(daily_rate)
    counts=0
    budget_count=0
    if(daily_rate<=job_daily_rate):
        counts=counts+1
        budget_count=1
        matching_daily_rate.append(daily_rate)
        not_matching_daily_rate.append(" ")
    else:
        counts=0
        budget_count=0
        matching_daily_rate.append(" ")
        not_matching_daily_rate.append(daily_rate)        
        
    count[i-1]=count[i-1]+counts     
    
    #company_size
    company_size=single_profile_data[10]
    counts=0
    if(job_company_size==company_size):
        counts=counts+1
        matching_company_size.append(company_size)
        not_matching_company_size.append(" ")
    else:
        counts=0
        matching_company_size.append(" ")
        not_matching_company_size.append(company_size)   
    
    #tech objectives
    tech_objective=single_profile_data[12]
    tech_objectives=list(tech_objective.split(" ; "))
    counts=0
    skill_string=''
    not_skill_string=''
    
    for j in tech_stack:
        current=''
        for l in tech_objectives:
            if(j==l):
                counts=counts+1
                skill_string=skill_string+j+' '
                current=j
        if(current==''):
            not_skill_string=not_skill_string+j+' '
    matching_tech_objectives.append(skill_string)
    not_matching_tech_objectives.append(not_skill_string)
            
    count[i-1]=count[i-1]+counts
    
    #availability
    availability=single_profile_data[4]
    counts=0
    time_count=0

    if(availability=="Available"):
        counts=counts+1
        time_count=1
        matching_availability.append("Availability")
        not_matching_availability.append(" ")
    elif(availability=="Available soon"):
        if(job_days1>=30):
            counts=counts+1
            time_count=1
            matching_availability.append("Availability")
            not_matching_availability.append(" ")
        elif(job_days1<30):
            counts=0
            time_count=0
            matching_availability.append(" ")
            not_matching_availability.append("Availability")   
    elif(availability=="Currently on a mission"):
        if(job_days1>=100):
            counts=counts+1
            time_count=1
            matching_availability.append("Availability")
            not_matching_availability.append(" ")
        elif(job_days1<100):
            counts=0
            time_count=0
            matching_availability.append(" ")
            not_matching_availability.append("Availability")           
    count[i-1]=count[i-1]+counts
    
    #mission constraint
    counts=0
    if(mission_constraint=="Time"):
        if(time_count==1):
            counts=counts+3
            matching_constraint.append("Time constraint")
            not_matching_constraint.append(" ")
        elif(time_count==0):
            counts=0
            matching_constraint.append(" ")
            not_matching_constraint.append("Time constraint")    
    elif(mission_constraint=="Budget"):
        if(budget_count==1):
            counts=counts+3
            matching_constraint.append("Budget constraint")
            not_matching_constraint.append(" ")
        elif(budget_count==0):
            counts=0
            matching_constraint.append(" ")
            not_matching_constraint.append("Budget constraint")        
    elif(mission_constraint=="Expertise"):
        if(exp_count==5):
            counts=counts+3
            matching_constraint.append("Expertise constraint")
            not_matching_constraint.append(" ")
        else:
            counts=0
            matching_constraint.append(" ")
            not_matching_constraint.append("Expertise constraint")     
    count[i-1]=count[i-1]+counts

profile=[]
for i in range(1,51):
    profile.append('Profile {}'.format(i))
zipped = list(zip(*sorted(zip(count,profile,matching_title_list,not_matching_title_list,matching_languages_list,not_matching_languages_list,matching_skills_list,not_matching_skills_list,matching_duration,not_matching_duration,matching_work_regime,not_matching_work_regime,matching_location,not_matching_location,matching_industry,not_matching_industry,matching_daily_rate,not_matching_daily_rate,matching_company_size,not_matching_company_size,matching_tech_objectives,not_matching_tech_objectives,matching_availability,not_matching_availability,matching_constraint,not_matching_constraint))))
count1,profile1,matching_title_list1,not_matching_title_list1,matching_languages_list1,not_matching_languages_list1,matching_skills_list1,not_matching_skills_list1,matching_duration1,not_matching_duration1,matching_work_regime1,not_matching_work_regime1,matching_location1,not_matching_location1,matching_industry1,not_matching_industry1,matching_daily_rate1,not_matching_daily_rate1,matching_company_size1,not_matching_company_size1,matching_tech_objectives1,not_matching_tech_objectives1,matching_availability1,not_matching_availability1,matching_constraint1,not_matching_constraint1 = [ list(tuple) for tuple in zipped]

count1.reverse()
profile1.reverse()
matching_title_list1.reverse()
not_matching_title_list1.reverse()
matching_languages_list1.reverse()
not_matching_languages_list1.reverse()
matching_skills_list1.reverse()
not_matching_skills_list1.reverse()
matching_duration1.reverse()
not_matching_duration1.reverse()
matching_work_regime1.reverse()
not_matching_work_regime1.reverse()
matching_location1.reverse()
not_matching_location1.reverse()
matching_industry1.reverse()
not_matching_industry1.reverse()
matching_daily_rate1.reverse()
not_matching_daily_rate1.reverse()
matching_company_size1.reverse()
not_matching_company_size1.reverse()
matching_tech_objectives1.reverse()
not_matching_tech_objectives1.reverse()
matching_availability1.reverse()
not_matching_availability1.reverse()
matching_constraint1.reverse()
not_matching_constraint1.reverse()

print(len(profile1))
for i in range(0,50):
    job_data= {'i':i,
               'Profile':profile1[i],
               'Count':count1[i],
               'Matching title':matching_title_list1[i],
               'Not matching title':not_matching_title_list1[i],
               'Matching languages':matching_languages_list1[i],
               'Not matching languages':not_matching_languages_list1[i],
               'Matching Skills':matching_skills_list1[i],
               'Not matching Skills':not_matching_skills_list1[i],
               'Matching duration':matching_duration1[i],
               'Not matching duration':not_matching_duration1[i],
               'Matching work regime':matching_work_regime1[i],
               'Not matching work regime':not_matching_work_regime1[i],
               'Matching location':matching_location1[i],
               'Not matching location':not_matching_location1[i],
               'Matching industry':matching_industry1[i],
               'Not matching industry':not_matching_industry1[i],
               'Matching daily rate':matching_daily_rate1[i],
               'Not matching daily rate':not_matching_daily_rate1[i],
               'Matching company size':matching_company_size1[i],
               'Not matching company size':not_matching_company_size1[i],
               'Matching tech objectives':matching_tech_objectives1[i],
               'Not matching tech objectives':not_matching_tech_objectives1[i],
               'Matching availability':matching_availability1[i],
               'Not matching availability':not_matching_availability1[i],
               'Matching mission constraint':matching_constraint1[i],
               'Not matching mision constraint':not_matching_constraint1[i]}
    y = json.dumps(job_data)
    print(y)  
    with open("output.json", "a") as write_file:
        json.dump(job_data, write_file)