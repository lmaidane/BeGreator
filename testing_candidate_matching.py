import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

#Reading the job information
job_information_data=pd.read_csv("Sample JDs_data scientist - testing.csv")
job_information_dataframe=pd.DataFrame(job_information_data)

job_desc_no='Job desc 1'
single_company_data=job_information_dataframe[job_desc_no]
single_company_data=list(single_company_data)

job_title=single_company_data[0]

job_language=single_company_data[3]
job_languages=list(job_language.split("; "))

job_skill=single_company_data[1]
job_skills=list(job_skill.split(" ; "))

job_skill_level=single_company_data[2]
job_skills_level=list(job_skill_level.split(" ; "))

job_location=single_company_data[4]

job_work=single_company_data[7]

job_industry=single_company_data[5]

job_daily_rate=single_company_data[6]
job_daily_rate=int(job_daily_rate)

job_tech_stack=single_company_data[8]
tech_stack=list(job_tech_stack.split(" ; "))

years=single_company_data[9]
job_years=list(years.split(" ; "))

essential_skill=single_company_data[10]
job_essential_skills=list(essential_skill.split(" ; "))

#Reading the Profiles information
datafilename = "Sample profiles_data scientist - testing.csv"
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
profile=[]
name=[]

cond_count1=[]
profile1=[]
name1=[]
matching_title_list1=[]
not_matching_title_list1=[]
matching_languages_list1=[]
not_matching_languages_list1=[]
matching_skills_list1=[]
not_matching_skills_list1=[]
matching_work_regime1=[]
not_matching_work_regime1=[]
matching_location1=[]
not_matching_location1=[]
matching_industry1=[]
not_matching_industry1=[]
matching_daily_rate1=[]
not_matching_daily_rate1=[]
matching_tech_objectives1=[]
not_matching_tech_objectives1=[]

cond_count2=[]
profile2=[]
name2=[]
matching_title_list2=[]
not_matching_title_list2=[]
matching_languages_list2=[]
not_matching_languages_list2=[]
matching_skills_list2=[]
not_matching_skills_list2=[]
matching_work_regime2=[]
not_matching_work_regime2=[]
matching_location2=[]
not_matching_location2=[]
matching_industry2=[]
not_matching_industry2=[]
matching_daily_rate2=[]
not_matching_daily_rate2=[]
matching_tech_objectives2=[]
not_matching_tech_objectives2=[]

cond_count3=[]
profile3=[]
name3=[]
matching_title_list3=[]
not_matching_title_list3=[]
matching_languages_list3=[]
not_matching_languages_list3=[]
matching_skills_list3=[]
not_matching_skills_list3=[]
matching_work_regime3=[]
not_matching_work_regime3=[]
matching_location3=[]
not_matching_location3=[]
matching_industry3=[]
not_matching_industry3=[]
matching_daily_rate3=[]
not_matching_daily_rate3=[]
matching_tech_objectives3=[]
not_matching_tech_objectives3=[]

cond_count4=[]
profile4=[]
name4=[]
matching_title_list4=[]
not_matching_title_list4=[]
matching_languages_list4=[]
not_matching_languages_list4=[]
matching_skills_list4=[]
not_matching_skills_list4=[]
matching_work_regime4=[]
not_matching_work_regime4=[]
matching_location4=[]
not_matching_location4=[]
matching_industry4=[]
not_matching_industry4=[]
matching_daily_rate4=[]
not_matching_daily_rate4=[]
matching_tech_objectives4=[]
not_matching_tech_objectives4=[]

#loop runs for each profile
for i in range(1,ncol):

    single_profile_data=job_information_dataframe['Profile {}'.format(i)]
    print('Profile {}'.format(i))
    single_profile_data=list(single_profile_data)
    prof="Profile {}".format(i)
    profile.append(prof)
    
    #name
    candidate_name=single_profile_data[8]
    name.append(candidate_name)
    
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
    lan_score=10
    for j in range(len(job_languages)):
        lan=" "
        for k in range(len(languages)):
            if(job_languages[j]==languages[k]):
                counts=counts+3
                lan=job_languages[j]
                lang=lang+job_languages[j]+' '
        if(lan==" "):
            not_lan=not_lan+job_languages[j]+" "
    not_matching_languages_list.append(not_lan)
    matching_languages_list.append(lang)
    if(counts==(len(job_languages)*3)):
        lan_score=0
    else:
        lan_score=1
            
    count[i-1]=count[i-1]+counts
    
    #essential_skills
    skill=single_profile_data[1]
    skills=list(skill.split(" ; "))
    level=single_profile_data[2]
    levels=list(level.split("; "))
    counts=0
    ess_skill_score=20
    skill_string=''
    not_skill_string=''
    
    for j,k in zip(job_essential_skills,job_years):
        k=int(k)
        current=''
        for l,m in zip(skills,levels):
            m=int(m)
            if(j==l and k<=m):
                counts=counts+7
                skill_string=skill_string+j+' '+str(m)+' '
                current=j+' '+str(m)
        if(current==''):
            not_skill_string=not_skill_string+j+' '+str(k)+' '

    if(counts==(len(job_essential_skills)*7)):
        ess_skill_score=0
    else:
        ess_skill_score=1
    
    #skills
    skill=single_profile_data[1]
    skills=list(skill.split(" ; "))
    level=single_profile_data[2]
    levels=list(level.split("; "))
    counts=0
    skill_string=''
    not_skill_string=''
    
    for j,k in zip(job_skills,job_skills_level):
        k=int(k)
        current=''
        for l,m in zip(skills,levels):
            m=int(m)
            if(j==l and k<=m):
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
    daily_rate=single_profile_data[6]
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
    
    #tech objectives
    tech_objective=single_profile_data[1]
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
    
    if(lan_score==0 and ess_skill_score==0):
        cond_count1.append(count[i-1])
        profile1.append(profile[i-1])
        name1.append(name[i-1])
        matching_title_list1.append(matching_title_list[i-1])
        not_matching_title_list1.append(not_matching_title_list[i-1])
        matching_languages_list1.append(matching_languages_list[i-1])
        not_matching_languages_list1.append(not_matching_languages_list[i-1])
        matching_skills_list1.append(matching_skills_list[i-1])
        not_matching_skills_list1.append(not_matching_skills_list[i-1])
        matching_work_regime1.append(matching_work_regime[i-1])
        not_matching_work_regime1.append(not_matching_work_regime[i-1])
        matching_location1.append(matching_location[i-1])
        not_matching_location1.append(not_matching_location[i-1])
        matching_industry1.append(matching_industry[i-1])
        not_matching_industry1.append(not_matching_industry[i-1])
        matching_daily_rate1.append(matching_daily_rate[i-1])
        not_matching_daily_rate1.append(not_matching_daily_rate[i-1])
        matching_tech_objectives1.append(matching_tech_objectives[i-1])
        not_matching_tech_objectives1.append(not_matching_tech_objectives[i-1])
        
    elif(lan_score==0 and ess_skill_score!=0):
        cond_count2.append(count[i-1])
        profile2.append(profile[i-1])
        name2.append(name[i-1])
        matching_title_list2.append(matching_title_list[i-1])
        not_matching_title_list2.append(not_matching_title_list[i-1])
        matching_languages_list2.append(matching_languages_list[i-1])
        not_matching_languages_list2.append(not_matching_languages_list[i-1])
        matching_skills_list2.append(matching_skills_list[i-1])
        not_matching_skills_list2.append(not_matching_skills_list[i-1])
        matching_work_regime2.append(matching_work_regime[i-1])
        not_matching_work_regime2.append(not_matching_work_regime[i-1])
        matching_location2.append(matching_location[i-1])
        not_matching_location2.append(not_matching_location[i-1])
        matching_industry2.append(matching_industry[i-1])
        not_matching_industry2.append(not_matching_industry[i-1])
        matching_daily_rate2.append(matching_daily_rate[i-1])
        not_matching_daily_rate2.append(not_matching_daily_rate[i-1])
        matching_tech_objectives2.append(matching_tech_objectives[i-1])
        not_matching_tech_objectives2.append(not_matching_tech_objectives[i-1])  
        
    elif(lan_score!=0 and ess_skill_score==0):
        cond_count3.append(count[i-1])
        profile3.append(profile[i-1])
        name3.append(name[i-1])
        matching_title_list3.append(matching_title_list[i-1])
        not_matching_title_list3.append(not_matching_title_list[i-1])
        matching_languages_list3.append(matching_languages_list[i-1])
        not_matching_languages_list3.append(not_matching_languages_list[i-1])
        matching_skills_list3.append(matching_skills_list[i-1])
        not_matching_skills_list3.append(not_matching_skills_list[i-1])
        matching_work_regime3.append(matching_work_regime[i-1])
        not_matching_work_regime3.append(not_matching_work_regime[i-1])
        matching_location3.append(matching_location[i-1])
        not_matching_location3.append(not_matching_location[i-1])
        matching_industry3.append(matching_industry[i-1])
        not_matching_industry3.append(not_matching_industry[i-1])
        matching_daily_rate3.append(matching_daily_rate[i-1])
        not_matching_daily_rate3.append(not_matching_daily_rate[i-1])
        matching_tech_objectives3.append(matching_tech_objectives[i-1])
        not_matching_tech_objectives3.append(not_matching_tech_objectives[i-1])  
        
    else:          
        cond_count4.append(count[i-1])
        profile4.append(profile[i-1])
        name4.append(name[i-1])
        matching_title_list4.append(matching_title_list[i-1])
        not_matching_title_list4.append(not_matching_title_list[i-1])
        matching_languages_list4.append(matching_languages_list[i-1])
        not_matching_languages_list4.append(not_matching_languages_list[i-1])
        matching_skills_list4.append(matching_skills_list[i-1])
        not_matching_skills_list4.append(not_matching_skills_list[i-1])
        matching_work_regime4.append(matching_work_regime[i-1])
        not_matching_work_regime4.append(not_matching_work_regime[i-1])
        matching_location4.append(matching_location[i-1])
        not_matching_location4.append(not_matching_location[i-1])
        matching_industry4.append(matching_industry[i-1])
        not_matching_industry4.append(not_matching_industry[i-1])
        matching_daily_rate4.append(matching_daily_rate[i-1])
        not_matching_daily_rate4.append(not_matching_daily_rate[i-1])
        matching_tech_objectives4.append(matching_tech_objectives[i-1])
        not_matching_tech_objectives4.append(not_matching_tech_objectives[i-1])  
    
cond_count5=[]
profile5=[]
name5=[]
matching_title_list5=[]
not_matching_title_list5=[]
matching_languages_list5=[]
not_matching_languages_list5=[]
matching_skills_list5=[]
not_matching_skills_list5=[]
matching_work_regime5=[]
not_matching_work_regime5=[]
matching_location5=[]
not_matching_location5=[]
matching_industry5=[]
not_matching_industry5=[]
matching_daily_rate5=[]
not_matching_daily_rate5=[]
matching_tech_objectives5=[]
not_matching_tech_objectives5=[]
 
if(lan_score==0 and ess_skill_score==0):       
    zipped = list(zip(*sorted(zip(cond_count1,profile1,name1,matching_title_list1,not_matching_title_list1,matching_languages_list1,not_matching_languages_list1,matching_skills_list1,not_matching_skills_list1,matching_work_regime1,not_matching_work_regime1,matching_location1,not_matching_location1,matching_industry1,not_matching_industry1,matching_daily_rate1,not_matching_daily_rate1,matching_tech_objectives1,not_matching_tech_objectives1))))
    cond_count1_sort,profile1_sort,name1_sort,matching_title_list1_sort,not_matching_title_list1_sort,matching_languages_list1_sort,not_matching_languages_list1_sort,matching_skills_list1_sort,not_matching_skills_list1_sort,matching_work_regime1_sort,not_matching_work_regime1_sort,matching_location1_sort,not_matching_location1_sort,matching_industry1_sort,not_matching_industry1_sort,matching_daily_rate1_sort,not_matching_daily_rate1_sort,matching_tech_objectives1_sort,not_matching_tech_objectives1_sort = [ list(tuple) for tuple in zipped]
    
    cond_count1_sort.reverse()
    profile1_sort.reverse()
    name1_sort.reverse()
    matching_title_list1_sort.reverse()
    not_matching_title_list1_sort.reverse()
    matching_languages_list1_sort.reverse()
    not_matching_languages_list1_sort.reverse()
    matching_skills_list1_sort.reverse()
    not_matching_skills_list1_sort.reverse()
    matching_work_regime1_sort.reverse()
    not_matching_work_regime1_sort.reverse()
    matching_location1_sort.reverse()
    not_matching_location1_sort.reverse()
    matching_industry1_sort.reverse()
    not_matching_industry1_sort.reverse()
    matching_daily_rate1_sort.reverse()
    not_matching_daily_rate1_sort.reverse()
    matching_tech_objectives1_sort.reverse()
    not_matching_tech_objectives1_sort.reverse()
    
    for i in range(len(cond_count1_sort)):
        cond_count5.append(cond_count1_sort[i])
        
    for i in range(len(profile1_sort)):
        profile5.append(profile1_sort[i])
        
    for i in range(len(name1_sort)):
        name5.append(name1_sort[i])
    
    for i in range(len(matching_title_list1_sort)):
        matching_title_list5.append(matching_title_list1_sort[i])
        
    for i in range(len(not_matching_title_list1_sort)):
        not_matching_title_list5.append(not_matching_title_list1_sort[i])
    
    for i in range(len(matching_languages_list1_sort)):
        matching_languages_list5.append(matching_languages_list1_sort[i])
    
    for i in range(len(not_matching_languages_list1_sort)):
        not_matching_languages_list5.append(not_matching_languages_list1_sort[i])  
        
    for i in range(len(matching_skills_list1_sort)):
        matching_skills_list5.append(matching_skills_list1_sort[i])
        
    for i in range(len(not_matching_skills_list1_sort)):
        not_matching_skills_list5.append(not_matching_skills_list1_sort[i])
        
    for i in range(len(matching_work_regime1_sort)):
        matching_work_regime5.append(matching_work_regime1_sort[i])
    
    for i in range(len(not_matching_work_regime1_sort)):
        not_matching_work_regime5.append(not_matching_work_regime1_sort[i])
    
    for i in range(len(matching_location1_sort)):
        matching_location5.append(matching_location1_sort[i])
        
    for i in range(len(not_matching_location1_sort)):
        not_matching_location5.append(not_matching_location1_sort[i])
        
    for i in range(len(matching_industry1_sort)):
        matching_industry5.append(matching_industry1_sort[i])
    
    for i in range(len(not_matching_industry1_sort)):
        not_matching_industry5.append(not_matching_industry1_sort[i])
        
    for i in range(len(matching_daily_rate1_sort)):
        matching_daily_rate5.append(matching_daily_rate1_sort[i])
        
    for i in range(len(not_matching_daily_rate1_sort)):
        not_matching_daily_rate5.append(not_matching_daily_rate1_sort[i])
    
    for i in range(len(matching_tech_objectives1_sort)):
        matching_tech_objectives5.append(matching_tech_objectives1_sort[i])
        
    for i in range(len(not_matching_tech_objectives1_sort)):
        not_matching_tech_objectives5.append(not_matching_tech_objectives1_sort[i])

if(lan_score==0 and ess_skill_score!=0):
    zipped2 = list(zip(*sorted(zip(cond_count2,profile2,name2,matching_title_list2,not_matching_title_list2,matching_languages_list2,not_matching_languages_list2,matching_skills_list2,not_matching_skills_list2,matching_work_regime2,not_matching_work_regime2,matching_location2,not_matching_location2,matching_industry2,not_matching_industry2,matching_daily_rate2,not_matching_daily_rate2,matching_tech_objectives2,not_matching_tech_objectives2))))
    cond_count2_sort,profile2_sort,name2_sort,matching_title_list2_sort,not_matching_title_list2_sort,matching_languages_list2_sort,not_matching_languages_list2_sort,matching_skills_list2_sort,not_matching_skills_list2_sort,matching_work_regime2_sort,not_matching_work_regime2_sort,matching_location2_sort,not_matching_location2_sort,matching_industry2_sort,not_matching_industry2_sort,matching_daily_rate2_sort,not_matching_daily_rate2_sort,matching_tech_objectives2_sort,not_matching_tech_objectives2_sort = [ list(tuple) for tuple in zipped2]
    
    cond_count2_sort.reverse()
    profile2_sort.reverse()
    name2_sort.reverse()
    matching_title_list2_sort.reverse()
    not_matching_title_list2_sort.reverse()
    matching_languages_list2_sort.reverse()
    not_matching_languages_list2_sort.reverse()
    matching_skills_list2_sort.reverse()
    not_matching_skills_list2_sort.reverse()
    matching_work_regime2_sort.reverse()
    not_matching_work_regime2_sort.reverse()
    matching_location2_sort.reverse()
    not_matching_location2_sort.reverse()
    matching_industry2_sort.reverse()
    not_matching_industry2_sort.reverse()
    matching_daily_rate2_sort.reverse()
    not_matching_daily_rate2_sort.reverse()
    matching_tech_objectives2_sort.reverse()
    not_matching_tech_objectives2_sort.reverse()
    
    for i in range(len(cond_count2_sort)):
        cond_count5.append(cond_count2_sort[i])

    for i in range(len(profile2_sort)):
        profile5.append(profile2_sort[i])

    for i in range(len(name2_sort)):
        name5.append(name2_sort[i])

    for i in range(len(matching_title_list2_sort)):
        matching_title_list5.append(matching_title_list2_sort[i])

    for i in range(len(not_matching_title_list2_sort)):
        not_matching_title_list5.append(not_matching_title_list2_sort[i])

    for i in range(len(matching_languages_list2_sort)):
        matching_languages_list5.append(matching_languages_list2_sort[i])

    for i in range(len(not_matching_languages_list2_sort)):
        not_matching_languages_list5.append(not_matching_languages_list2_sort[i])

    for i in range(len(matching_skills_list2_sort)):
        matching_skills_list5.append(matching_skills_list2_sort[i])

    for i in range(len(not_matching_skills_list2_sort)):
        not_matching_skills_list5.append(not_matching_skills_list2_sort[i])

    for i in range(len(matching_work_regime2_sort)):
        matching_work_regime5.append(matching_work_regime2_sort[i])

    for i in range(len(not_matching_work_regime2_sort)):
        not_matching_work_regime5.append(not_matching_work_regime2_sort[i])

    for i in range(len(matching_location2_sort)):
        matching_location5.append(matching_location2_sort[i])

    for i in range(len(not_matching_location2_sort)):
        not_matching_location5.append(not_matching_location2_sort[i])

    for i in range(len(matching_industry2_sort)):
        matching_industry5.append(matching_industry2_sort[i])

    for i in range(len(not_matching_industry2_sort)):
        not_matching_industry5.append(not_matching_industry2_sort[i])

    for i in range(len(matching_daily_rate2_sort)):
        matching_daily_rate5.append(matching_daily_rate2_sort[i])

    for i in range(len(not_matching_daily_rate2_sort)):
        not_matching_daily_rate5.append(not_matching_daily_rate2_sort[i])

    for i in range(len(matching_tech_objectives2_sort)):
        matching_tech_objectives5.append(matching_tech_objectives2_sort[i])

    for i in range(len(not_matching_tech_objectives2_sort)):
        not_matching_tech_objectives5.append(not_matching_tech_objectives2_sort[i])

if(lan_score!=0 and ess_skill_score==0):
    zipped3 = list(zip(*sorted(zip(cond_count3,profile3,name3,matching_title_list3,not_matching_title_list3,matching_languages_list3,not_matching_languages_list3,matching_skills_list3,not_matching_skills_list3,matching_work_regime3,not_matching_work_regime3,matching_location3,not_matching_location3,matching_industry3,not_matching_industry3,matching_daily_rate3,not_matching_daily_rate3,matching_tech_objectives3,not_matching_tech_objectives3))))
    cond_count3_sort,profile3_sort,name3_sort,matching_title_list3_sort,not_matching_title_list3_sort,matching_languages_list3_sort,not_matching_languages_list3_sort,matching_skills_list3_sort,not_matching_skills_list3_sort,matching_work_regime3_sort,not_matching_work_regime3_sort,matching_location3_sort,not_matching_location3_sort,matching_industry3_sort,not_matching_industry3_sort,matching_daily_rate3_sort,not_matching_daily_rate3_sort,matching_tech_objectives3_sort,not_matching_tech_objectives3_sort = [ list(tuple) for tuple in zipped3]
    
    cond_count3_sort.reverse()
    profile3_sort.reverse()
    name3_sort.reverse()
    matching_title_list3_sort.reverse()
    not_matching_title_list3_sort.reverse()
    matching_languages_list3_sort.reverse()
    not_matching_languages_list3_sort.reverse()
    matching_skills_list3_sort.reverse()
    not_matching_skills_list3_sort.reverse()
    matching_work_regime3_sort.reverse()
    not_matching_work_regime3_sort.reverse()
    matching_location3_sort.reverse()
    not_matching_location3_sort.reverse()
    matching_industry3_sort.reverse()
    not_matching_industry3_sort.reverse()
    matching_daily_rate3_sort.reverse()
    not_matching_daily_rate3_sort.reverse()
    matching_tech_objectives3_sort.reverse()
    not_matching_tech_objectives3_sort.reverse()

    for i in range(len(cond_count3_sort)):
        cond_count5.append(cond_count3_sort[i])

    for i in range(len(profile3_sort)):
        profile5.append(profile3_sort[i])

    for i in range(len(name3_sort)):
        name5.append(name3_sort[i])

    for i in range(len(matching_title_list3_sort)):
        matching_title_list5.append(matching_title_list3_sort[i])

    for i in range(len(not_matching_title_list3_sort)):
        not_matching_title_list5.append(not_matching_title_list3_sort[i])

    for i in range(len(matching_languages_list3_sort)):
        matching_languages_list5.append(matching_languages_list3_sort[i])

    for i in range(len(not_matching_languages_list3_sort)):
        not_matching_languages_list5.append(not_matching_languages_list3_sort[i])

    for i in range(len(matching_skills_list3_sort)):
        matching_skills_list5.append(matching_skills_list3_sort[i])

    for i in range(len(not_matching_skills_list3_sort)):
        not_matching_skills_list5.append(not_matching_skills_list3_sort[i])

    for i in range(len(matching_work_regime3_sort)):
        matching_work_regime5.append(matching_work_regime3_sort[i])

    for i in range(len(not_matching_work_regime3_sort)):
        not_matching_work_regime5.append(not_matching_work_regime3_sort[i])

    for i in range(len(matching_location3_sort)):
        matching_location5.append(matching_location3_sort[i])

    for i in range(len(not_matching_location3_sort)):
        not_matching_location5.append(not_matching_location3_sort[i])

    for i in range(len(matching_industry3_sort)):
        matching_industry5.append(matching_industry3_sort[i])

    for i in range(len(not_matching_industry3_sort)):
        not_matching_industry5.append(not_matching_industry3_sort[i])

    for i in range(len(matching_daily_rate3_sort)):
        matching_daily_rate5.append(matching_daily_rate3_sort[i])

    for i in range(len(not_matching_daily_rate3_sort)):
        not_matching_daily_rate5.append(not_matching_daily_rate3_sort[i])

    for i in range(len(matching_tech_objectives3_sort)):
        matching_tech_objectives5.append(matching_tech_objectives3_sort[i])

    for i in range(len(not_matching_tech_objectives3_sort)):
        not_matching_tech_objectives5.append(not_matching_tech_objectives3_sort[i])

if(lan_score!=0 and ess_skill_score!=0):
    zipped4 = list(zip(*sorted(zip(cond_count4,profile4,name4,matching_title_list4,not_matching_title_list4,matching_languages_list4,not_matching_languages_list4,matching_skills_list4,not_matching_skills_list4,matching_work_regime4,not_matching_work_regime4,matching_location4,not_matching_location4,matching_industry4,not_matching_industry4,matching_daily_rate4,not_matching_daily_rate4,matching_tech_objectives4,not_matching_tech_objectives4))))
    cond_count4_sort,profile4_sort,name4_sort,matching_title_list4_sort,not_matching_title_list4_sort,matching_languages_list4_sort,not_matching_languages_list4_sort,matching_skills_list4_sort,not_matching_skills_list4_sort,matching_work_regime4_sort,not_matching_work_regime4_sort,matching_location4_sort,not_matching_location4_sort,matching_industry4_sort,not_matching_industry4_sort,matching_daily_rate4_sort,not_matching_daily_rate4_sort,matching_tech_objectives4_sort,not_matching_tech_objectives4_sort = [ list(tuple) for tuple in zipped4]
    
    cond_count4_sort.reverse()
    profile4_sort.reverse()
    name4_sort.reverse()
    matching_title_list4_sort.reverse()
    not_matching_title_list4_sort.reverse()
    matching_languages_list4_sort.reverse()
    not_matching_languages_list4_sort.reverse()
    matching_skills_list4_sort.reverse()
    not_matching_skills_list4_sort.reverse()
    matching_work_regime4_sort.reverse()
    not_matching_work_regime4_sort.reverse()
    matching_location4_sort.reverse()
    not_matching_location4_sort.reverse()
    matching_industry4_sort.reverse()
    not_matching_industry4_sort.reverse()
    matching_daily_rate4_sort.reverse()
    not_matching_daily_rate4_sort.reverse()
    matching_tech_objectives4_sort.reverse()
    not_matching_tech_objectives4_sort.reverse()
    
    for i in range(len(cond_count4_sort)):
        cond_count5.append(cond_count4_sort[i])

    for i in range(len(profile4_sort)):
        profile5.append(profile4_sort[i])

    for i in range(len(name4_sort)):
        name5.append(name4_sort[i])

    for i in range(len(matching_title_list4_sort)):
        matching_title_list5.append(matching_title_list4_sort[i])

    for i in range(len(not_matching_title_list4_sort)):
        not_matching_title_list5.append(not_matching_title_list4_sort[i])

    for i in range(len(matching_languages_list4_sort)):
        matching_languages_list5.append(matching_languages_list4_sort[i])

    for i in range(len(not_matching_languages_list4_sort)):
        not_matching_languages_list5.append(not_matching_languages_list4_sort[i])    

    for i in range(len(matching_skills_list4_sort)):
        matching_skills_list5.append(matching_skills_list4_sort[i])

    for i in range(len(not_matching_skills_list4_sort)):
        not_matching_skills_list5.append(not_matching_skills_list4_sort[i])
 
    for i in range(len(matching_work_regime4_sort)):
        matching_work_regime5.append(matching_work_regime4_sort[i])

    for i in range(len(not_matching_work_regime4_sort)):
        not_matching_work_regime5.append(not_matching_work_regime4_sort[i])

    for i in range(len(matching_location4_sort)):
        matching_location5.append(matching_location4_sort[i])

    for i in range(len(not_matching_location4_sort)):
        not_matching_location5.append(not_matching_location4_sort[i])

    for i in range(len(matching_industry4_sort)):
        matching_industry5.append(matching_industry4_sort[i])

    for i in range(len(not_matching_industry4_sort)):
        not_matching_industry5.append(not_matching_industry4_sort[i])

    for i in range(len(matching_daily_rate4_sort)):
        matching_daily_rate5.append(matching_daily_rate4_sort[i])
 
    for i in range(len(not_matching_daily_rate4_sort)):
        not_matching_daily_rate5.append(not_matching_daily_rate4_sort[i])

    for i in range(len(matching_tech_objectives4_sort)):
        matching_tech_objectives5.append(matching_tech_objectives4_sort[i])

    for i in range(len(not_matching_tech_objectives4_sort)):
        not_matching_tech_objectives5.append(not_matching_tech_objectives4_sort[i])
    
'''print(count1)
print(profile1)
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
print(not_matching_tech_objectives1)'''

job_desc=[]
job_desc.append(job_desc_no)
for i in range(len(profile)-1):
    job_desc.append(' ')

job_data=pd.DataFrame({'Job desc':job_desc,
           'Profile':profile5,
           'Name':name5,
           'Score':cond_count5,
           'Matching title':matching_title_list5,
           'Not matching title':not_matching_title_list5,
           'Matching languages':matching_languages_list5,
           'Not matching languages':not_matching_languages_list5,
           'Matching Skills':matching_skills_list5,
           'Not matching Skills':not_matching_skills_list5,
           'Matching work regime':matching_work_regime5,
           'Not matching work regime':not_matching_work_regime5,
           'Matching location':matching_location5,
           'Not matching location':not_matching_location5,
           'Matching industry':matching_industry5,
           'Not matching industry':not_matching_industry5,
           'Matching daily rate':matching_daily_rate5,
           'Not matching daily rate':not_matching_daily_rate5,
           'Matching tech objectives':matching_tech_objectives5,
           'Not matching tech objectives':not_matching_tech_objectives5})

#storing in csv file
job_data.to_csv("Results for data scientist job desc1 - testing.csv",index=0)