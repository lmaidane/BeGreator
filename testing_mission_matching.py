import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

#Reading the job information
job_information_data=pd.read_csv("Sample profiles - testing.csv")
job_information_dataframe=pd.DataFrame(job_information_data)

profile_no='Profile 1'
single_company_data=job_information_dataframe[profile_no]
single_company_data=list(single_company_data)

name=single_company_data[8]

job_titles=single_company_data[0]
job_title = list(job_titles.split("; "))

job_language=single_company_data[3]
job_languages=list(job_language.split("; "))

job_skill=single_company_data[1]
job_skills=list(job_skill.split(" ; "))

job_skill_level=single_company_data[2]
job_skills_level=list(job_skill_level.split(" ; "))

job_location=single_company_data[4]

job_work=single_company_data[7]

job_industries=single_company_data[5]
job_industry=list(job_industries.split(" ; "))

job_daily_rate=single_company_data[6]
job_daily_rate=int(job_daily_rate)

#Reading the Profiles information
datafilename = "Sample job descriptions - testing.csv"
job_information_data=pd.read_csv(datafilename)
job_information_dataframe=pd.DataFrame(job_information_data)

with open(datafilename, 'r') as csv:
     first_line = csv.readline()
     your_data = csv.readlines()

ncol = first_line.count(',')+1

count=[]
matching_title_list=[]
not_matching_title_list=[]
matching_languages_list=[]
not_matching_languages_list=[]
matching_skills_list=[]
not_matching_skills_list=[]
not_matching_work_regime=[]
matching_work_regime=[]
matching_location=[]
not_matching_location=[]
matching_industry=[]
not_matching_industry=[]
matching_daily_rate=[]
not_matching_daily_rate=[]
matching_tech_objectives=[]
not_matching_tech_objectives=[]
job_desc=[]

#loop runs for each profile
for i in range(1,ncol):

    single_profile_data=job_information_dataframe['Job desc {}'.format(i)]
    single_profile_data=list(single_profile_data)
    job_desc.append("Job desc {}".format(i))
    
    #title matching
    title=single_profile_data[0]
    counts=0
    matching_title=" "
    for j in range(len(job_title)):
        if(title==job_title[j]):
            counts=counts+1
            matching_title=title
            matching_title_list.append(matching_title)
            not_matching_title_list.append(" ")
    if(matching_title==' '):
        matching_title_list.append(" ")
        not_matching_title_list.append(title)
    count.append(counts)
    
    #languages matching
    language=single_profile_data[3]
    languages=list(language.split("; "))
    counts=0
    lang=''
    not_lan=''
    for j in range(len(languages)):
        lan=" "
        for k in range(len(job_languages)):
            if(languages[j]==job_languages[k]):
                counts=counts+3
                lan=languages[j]
                lang=lang+languages[j]+' '
        if(lan==" "):
            not_lan=not_lan+languages[j]+" "
    not_matching_languages_list.append(not_lan)
    matching_languages_list.append(lang)
            
    count[i-1]=count[i-1]+counts
    
    #skills
    skill=single_profile_data[1]
    skills=list(skill.split(" ; "))
    level=single_profile_data[2]
    levels=list(level.split("; "))
    counts=0
    skill_string=''
    not_skill_string=''
    
    for j,k in zip(skills,levels):
        k=int(k)
        current=''
        for l,m in zip(job_skills,job_skills_level):
            m=int(m)
            if(j==l and (k-1)<=m):
                counts=counts+7
                skill_string=skill_string+j+' '+str(m)+' '
                current=j+' '+str(m)
        if(current==''):
            not_skill_string=not_skill_string+j+' '+str(k)+' '
    matching_skills_list.append(skill_string)
    not_matching_skills_list.append(not_skill_string)
            
    count[i-1]=count[i-1]+counts
    
    #work regime
    work_regime=single_profile_data[7]
    counts=0
    if(job_work==work_regime):
        counts=counts+1
        matching_work_regime.append(work_regime)
        not_matching_work_regime.append(" ")
    else:
        counts=0
        matching_work_regime.append(" ")
        not_matching_work_regime.append(work_regime)        
        
    count[i-1]=count[i-1]+counts 
    
    #remote and location
    places=[]
    latitude=[]
    longitude=[]
    location_string=''
    location=single_profile_data[4]
    counts=0
     
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
    if(int(great_circle(first, second).km)<=50):
        counts=counts+1
        matching_location.append(location_string)
        not_matching_location.append(" ")
    elif(int(great_circle(first, second).km)>50):
        counts=0
        matching_location.append(" ")
        not_matching_location.append(location_string)
    count[i-1]=count[i-1]+counts
    
    #industry
    industry=single_profile_data[5]
    counts=0
    for j in range(len(job_industry)):
        if(industry==job_industry[j]):
            counts=counts+1
            matching_industry.append(industry)
            not_matching_industry.append(" ")
    if(counts==0):
        matching_industry.append(" ")
        not_matching_industry.append(industry)
    count[i-1]=count[i-1]+counts
    
    #daily_rate
    daily_rate=single_profile_data[6]
    daily_rate=int(daily_rate)
    counts=0
    budget_count=0
    if(daily_rate>=job_daily_rate):
        counts=counts+1
        matching_daily_rate.append(daily_rate)
        not_matching_daily_rate.append(" ")
    else:
        counts=0
        matching_daily_rate.append(" ")
        not_matching_daily_rate.append(daily_rate)        
        
    count[i-1]=count[i-1]+counts      
    
    #tech objectives
    tech_objective=single_profile_data[8]
    tech_objectives=list(tech_objective.split(" ; "))
    counts=0
    skill_string=''
    not_skill_string=''
    
    for j in tech_objectives:
        current=''
        for l in job_skills:
            if(j==l):
                counts=counts+1
                skill_string=skill_string+j+' '
                current=j
        if(current==''):
            not_skill_string=not_skill_string+j+' '
    matching_tech_objectives.append(skill_string)
    not_matching_tech_objectives.append(not_skill_string)
            
    count[i-1]=count[i-1]+counts

zipped = list(zip(*sorted(zip(count,job_desc,matching_title_list,not_matching_title_list,matching_languages_list,not_matching_languages_list,matching_skills_list,not_matching_skills_list,matching_work_regime,not_matching_work_regime,matching_location,not_matching_location,matching_industry,not_matching_industry,matching_daily_rate,not_matching_daily_rate,matching_tech_objectives,not_matching_tech_objectives))))
count1,job_desc1,matching_title_list1,not_matching_title_list1,matching_languages_list1,not_matching_languages_list1,matching_skills_list1,not_matching_skills_list1,matching_work_regime1,not_matching_work_regime1,matching_location1,not_matching_location1,matching_industry1,not_matching_industry1,matching_daily_rate1,not_matching_daily_rate1,matching_tech_objectives1,not_matching_tech_objectives1 = [ list(tuple) for tuple in zipped]

count1.reverse()
job_desc1.reverse()
matching_title_list1.reverse()
not_matching_title_list1.reverse()
matching_languages_list1.reverse()
not_matching_languages_list1.reverse()
matching_skills_list1.reverse()
not_matching_skills_list1.reverse()
matching_work_regime1.reverse()
not_matching_work_regime1.reverse()
matching_location1.reverse()
not_matching_location1.reverse()
matching_industry1.reverse()
not_matching_industry1.reverse()
matching_daily_rate1.reverse()
not_matching_daily_rate1.reverse()
matching_tech_objectives1.reverse()
not_matching_tech_objectives1.reverse()

print(count1)
print(job_desc1)
print(matching_title_list1)
print(not_matching_title_list1)
print(matching_languages_list1)
print(not_matching_languages_list1)
print(matching_skills_list1)
print(not_matching_skills_list1)
print(matching_work_regime1)
print(not_matching_work_regime1)
print(matching_location1)
print(not_matching_location1)
print(matching_industry1)
print(not_matching_industry1)
print(matching_daily_rate1)
print(not_matching_daily_rate1)
print(matching_tech_objectives1)
print(not_matching_tech_objectives1)

profile=[]
profile.append(profile_no)
profile.append(name)
for i in range(len(job_desc)-2):
    profile.append(' ')

job_data=pd.DataFrame({'Profile':profile,
           'Job desc':job_desc1,
           'Score':count1,
           'Matching title':matching_title_list1,
           'Not matching title':not_matching_title_list1,
           'Matching languages':matching_languages_list1,
           'Not matching languages':not_matching_languages_list1,
           'Matching Skills':matching_skills_list1,
           'Not matching Skills':not_matching_skills_list1,
           'Matching work regime':matching_work_regime1,
           'Not matching work regime':not_matching_work_regime1,
           'Matching location':matching_location1,
           'Not matching location':not_matching_location1,
           'Matching industry':matching_industry1,
           'Not matching industry':not_matching_industry1,
           'Matching daily rate':matching_daily_rate1,
           'Not matching daily rate':not_matching_daily_rate1,
           'Matching tech objectives':matching_tech_objectives1,
           'Not matching tech objectives':not_matching_tech_objectives1})

#storing in csv file
job_data.to_csv("Results for data engineer profile - testing.csv",mode='a',header=False,index=0)