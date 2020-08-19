import pandas as pd
import re
from langdetect import detect

from nltk.corpus import stopwords
from nltk.util import ngrams
import nltk

from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()

from warnings import warn

#reading csv file of job titles
data=pd.read_csv("Job_title.csv")
df=pd.DataFrame(data)
job_title=df['Job title']
location_linkedin="London, England, United Kingdom"
location_indeed="Brussels"
website = ['linkedin','indeed','ictjob']

for m in range(len(website)):
    if(website[m]=='linkedin'):
        for i in range(len(job_title)):
            url = "https://www.linkedin.com/jobs"
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(url)
            sleep(10)
            print(job_title[i])
            driver.find_element_by_xpath("/html/body/main/section[1]/section/div[2]/section[2]/form/section[1]/input").send_keys(job_title[i])
            driver.find_element_by_xpath("/html/body/main/section[1]/section/div[2]/section[2]/form/section[2]/button/icon").click()
            driver.find_element_by_xpath("/html/body/main/section[1]/section/div[2]/section[2]/form/section[2]/input").send_keys(location_linkedin)
            driver.find_element_by_xpath("/html/body/main/section[1]/section/div[2]/button[2]").click()
            sleep(3)
            driver.find_element_by_xpath("/html/body/header/section/form/ul/li[2]/div/button").click()
            #driver.find_element_by_xpath("/html/body/header/section/form/ul/li[2]/div/div/fieldset/div[1]/ul/li[1]/label").click()
            driver.find_element_by_xpath("/html/body/header/section/form/ul/li[2]/div/div/fieldset/div[1]/ul/li[2]/label").click()
            driver.find_element_by_xpath("/html/body/header/section/form/ul/li[2]/div/div/fieldset/div[2]/button").click()
            sleep(5)
            driver.execute_script("window.scrollBy(0,10000)","")
            sleep(20)
            
            # parsing the visible webpage
            pageSource = driver.page_source
            lxml_soup = BeautifulSoup(pageSource, 'lxml')
            
            # searching for all job container
            # setting up list for job information
            job_id = []
            post_title = []
            company_name = []
            post_date = []
            job_location = []
            no_of_applicants=[]
            job_desc = []
            level = []
            emp_type = []
            functions = []
            industries = []
            
            job_container = lxml_soup.find('ul', class_ = 'jobs-search__results-list')
            
            print('You are scraping information about {} jobs.'.format(len(job_container)))
            #print(job_container)
            # for loop for job title, company, id, location and date posted
            for job in job_container:
                
                # job title
                job_titles = job.find("span", class_="screen-reader-text").text
                post_title.append(job_titles)
                
                # linkedin job id
                job_ids = job.find('a', href=True)['href']
                job_ids = re.findall(r'(?!-)([0-9]*)(?=\?)',job_ids)[0]
                job_id.append(job_ids)
                
                # company name
                company_names = job.select_one('img')['alt']
                company_name.append(company_names)
                
                # job location
                job_locations = job.find("span", class_="job-result-card__location").text
                job_location.append(job_locations)
                
                # posting date
                post_dates = job.select_one('time')['datetime']
                post_date.append(post_dates)
                
            
            # for loop for job description and criterias
            for x in range(1,len(job_id)+1):
                
                # clicking on different job containers to view information about the job
                job_xpath = '/html/body/main/div/section/ul/li[{}]/img'.format(x)
                driver.find_element_by_xpath(job_xpath).click()
                sleep(3)
                
                # no of applicants
                applicants_xpath="num-applicants__caption"
                applicants=driver.find_element_by_class_name(applicants_xpath).text
                num_applicants=''.join(list(filter(lambda c: c.isdigit(), applicants)))
                no_of_applicants.append(num_applicants)
                
                # job description
                jobdesc_xpath="show-more-less-html__markup"
                try:
                    driver.find_element_by_xpath("/html/body/main/section/div[2]/section[2]/div/section/button[1]").click()
                    job_descs = driver.find_element_by_class_name(jobdesc_xpath).text
                    job_desc.append(job_descs)
                except:
                    job_descs = driver.find_element_by_class_name(jobdesc_xpath).text
                    job_desc.append(job_descs)        
                
                # job criteria container below the description
                #job_criteria_container = lxml_soup.find('ul', class_ = 'job-criteria__list')
                #all_job_criterias = job_criteria_container.find_all("span", class_='job-criteria__text job-criteria__text--criteria')
                
                # Seniority level
                try:
                    seniority_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[1]'
                    seniority = driver.find_element_by_xpath(seniority_xpath).text.splitlines(0)[1]
                    level.append(seniority)
                except:
                    level.append(" ")
                
                # Employment type
                try:
                    type_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[2]'
                    employment_type = driver.find_element_by_xpath(type_xpath).text.splitlines(0)[1]
                    emp_type.append(employment_type)
                except:
                    emp_type.append(" ")
                
                # Job function
                try:
                    function_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[3]'
                    job_function = driver.find_element_by_xpath(function_xpath).text.splitlines(0)[1]
                    functions.append(job_function)
                except:
                    functions.append(" ")
                
                # Industries
                industry_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[4]'
                try:
                    industry_type = driver.find_element_by_xpath(industry_xpath).text.splitlines(0)[1]
                    industries.append(industry_type)
                except:
                    industries.append(' ')
                #print("collected",x)
                x = x+1
            
            #elimination of other languages (only english)
            '''tect=[]
            for i in range(len(job_desc)):
                te=detect(job_desc[i])
                tect.append(te)
                #print(te)
            for i in range(len(tect)):
                if(tect[i]=="en"):
                    continue;
                elif(tect[i]!="en"):
                    job_id.remove(job_id[i])
                    post_title.remove(post_title[i])
                    company_name.remove(company_name[i])
                    post_date.remove(post_date[i])
                    job_location.remove(job_location[i])
                    no_of_applicants.remove(no_of_applicants[i])
                    job_desc.remove(job_desc[i])
                    level.remove(level[i])
                    emp_type.remove(emp_type[i])
                    functions.remove(functions[i])
                    industries.remove(industries[i])'''
            
            # creating a dataframe
            job_data = pd.DataFrame({'Job ID': job_id,
            'Date': post_date,
            'Company Name': company_name,
            'Post': post_title,
            'Location': job_location,
            'No.of Applicants': no_of_applicants,
            'Description': job_desc,
            'Level': level,
            'Type': emp_type,
            'Function': functions,
            'Industry': industries,
            'Link': ' ',
            'Review':' '
            })
            
            # cleaning description column
            job_data['Description'] = job_data['Description'].str.replace('\n',' ')
            
            #storing in csv file
            #string=str(job_title[i])+'.csv'
            job_data.to_csv("Data jobs.csv", mode='a', header=False, index=0)
            
    elif(website[m]=='indeed'):
        for i in range(len(job_title)):
            driver = webdriver.Chrome()
    
            driver.get('https://indeed.com')
            sleep(10)
            print(job_title[i])
            search_job = driver.find_element_by_xpath('/html/body/main/div[4]/div[1]/div/div/div/form/div[1]/div[1]/div/div[2]/input').send_keys(job_title[i])
            
            driver.find_element_by_xpath('/html/body/main/div[4]/div[1]/div/div/div/form/div[2]/div[1]/div/div[2]/input').send_keys(location_indeed)
            
            initial_search_button = driver.find_element_by_xpath('/html/body/main/div[4]/div[1]/div/div/div/form/div[3]/button').click()
            
            '''close_popup = driver.find_element_by_id("popover-close-link")
            close_popup.click()'''
            
            advanced_search = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[4]/div/a")
            advanced_search.click()
            
            #set display limit of 30 results per page
            display_limit = driver.find_element_by_xpath('//select[@id="limit"]//option[@value="30"]')
            display_limit.click()
            #sort by date
            sort_option = driver.find_element_by_xpath('//select[@id="sort"]//option[@value="date"]')
            sort_option.click()
            search_button = driver.find_element_by_xpath('/html/body/form/fieldset[2]/div[3]/div/div[3]/select/option[2]')
            search_button.click()
            
            driver.find_element_by_xpath('/html/body/form/button').click()
            
            #let the driver wait 3 seconds to locate the element before exiting out
            driver.implicitly_wait(3) 
            
            close_popup = driver.find_element_by_xpath("/html/body/div[3]/div[1]/a")
            close_popup.click()
            
            titles=[]
            companies=[]
            locations=[]
            links =[]
            reviews=[]
            descriptions=[]
            date_post=[]
            
            
            for j in range(0,20):
                
                job_card = driver.find_elements_by_xpath('//div[contains(@class,"clickcard")]')
                
                for job in job_card:
                   
                    #not all companies have review
                    try:
                        review = job.find_element_by_xpath('.//span[@class="ratingsContent"]').text
                    except:
                        review = " "
                    reviews.append(review)
                    
                    try:
                        location = job.find_element_by_xpath('.//span[contains(@class,"location")]').text
                    except:
                        location = " "
                    #tells only to look at the element       
                    locations.append(location)
                    
                    try:
                        date_posted=job.find_element_by_xpath('.//span[@class="date "]').text
                        
                    except:
                        date_posted=" "
                    date_post.append(date_posted)
                    
                    try:
                        title  = job.find_element_by_xpath('.//h2[@class="title"]//a').text
                    except:
                        title = job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="title")
                    titles.append(title)
                    links.append(job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="href"))
                    companies.append(job.find_element_by_xpath('.//span[@class="company"]').text)
                    
                driver.execute_script("window.scrollBy(0,10000)","")
                sleep(10)
                    
                try:
                    next_page = driver.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(j+2))
                    next_page.click()
            
                except:
                    break;               
                
                print("Page: {}".format(str(j+2)))
            
            descriptions=[]
            for link in links:
                
                driver.get(link)
                jd = driver.find_element_by_xpath('//div[@id="jobDescriptionText"]').text
                descriptions.append(jd)
            
            #collecting year of experience from job description
            jd=list(descriptions)
            year=[]
            for d in range(len(jd)):
                file1 = re.sub(r'[,.;'':@#?!&$()/]', ' ', jd[d])
                filtered_words1 = nltk.word_tokenize(file1)
                for k in range(len(filtered_words1)):
                    filtered_words1[k] = filtered_words1[k]. lower()
                years=[]
                for g in range(len(filtered_words1)):
                    if(filtered_words1[g]=='years' and filtered_words1[g-2]!='over'):
                        years.append(filtered_words1[g-1])
                if(len(years)>0):
                    year.append(str(years[0]))
                else:
                    year.append(' ')
                
            df_da=pd.DataFrame()
            df_da['Date Posted']=date_post
            df_da['Company Name']=companies
            df_da['Job Title']=titles
            df_da['Location']=location_indeed
            df_da['No.of applicants']=' '
            df_da['Description']=descriptions
            df_da['Level']=year
            df_da['Type']=' '
            df_da['Function']=' '
            df_da['Industry']=' '
            df_da['Link']=links
            df_da['Review']=reviews
            
            #string1=str(job_title[i])+'.csv'
            df_da.to_csv("Data jobs.csv", mode='a', header=False, index=0)

    elif(website[m]=='ictjob'):
        
        url = "https://www.ictjob.be/en/search-it-jobs"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        sleep(10)
        
        #job title
        #driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[1]/div/div[3]/div[2]/div[1]/div/div[1]/label/input").send_keys(job_title)
        #sleep(5)
        
        #big data expert
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/a/span").click()
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div[2]/ul/li[10]/div/label/span").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/a").click()
        
        driver.execute_script("window.scrollBy(0,300)","")
        sleep(5)
        
        #exact search
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[2]/div/div/div[2]/section/div/div[1]/div/div[2]/span[2]/a").click()
        sleep(5)
        
        #date relevance
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div/ul/li[1]/label/a").click()
        sleep(5)
        
        #english language
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/label[3]").click()
        sleep(10)
        
        driver.execute_script("window.scrollBy(0,500)","")
        sleep(10)
        
        #full-time
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/ul/li[5]/div/span/span[1]").click()
        driver.find_element_by_xpath("/html/body/section/div[1]/div/div[2]/div/div/form/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/ul/li[5]/div/ul/li[1]/label/a").click()
        
        titles=[]
        companies=[]
        locations=[]
        links =[]
        reviews=[]
        descriptions=[]
        dates=[]
        
        for i in range(0,2):
            
            job_card = driver.find_elements_by_xpath('//li[contains(@class,"search-item clearfix")]')
            sleep(2)
            for job in job_card:
                try:
                    link=job.find_element_by_xpath('.//a[@class="job-title search-item-link"]').get_attribute(name="href")
                except:
                    link=job.find_element_by_xpath('/html/body/section/div[1]/div/div[2]/div/div/form/div[2]/div/div/div[2]/section/div/div[3]/div[1]/div/ul/li[{}]/span[2]/a'.format(i+1))
                #print(link)
                links.append(link)
                
                company=job.find_element_by_xpath('.//span[@class="job-company"]').text
                #print(company)
                companies.append(company)
                
                title=job.find_element_by_xpath('.//h2[@class="job-title"]').text
                #print(title)
                titles.append(title)
                
                datee=job.find_element_by_xpath('.//span[@class="job-date"]').text     
                #print(datee)
                dates.append(datee)
                
                location=job.find_element_by_xpath('.//span[contains(@class,"job-location")]').text
                #print(location)
                locations.append(location)
            
            sleep(5)    
            driver.execute_script("window.scrollBy(0,10000)","")
            sleep(5)
                
            try:
                next_page = driver.find_element_by_xpath('//div[@class="page-list"]//a[@id="page_{}"]'.format(i+2))
                next_page.click()
                sleep(10)
        
            except:
                break;
            
            print("\nPage: {}\n".format(str(i+2)))
            
        df_da=pd.DataFrame()
        df_da['Date Posted']=dates
        df_da['Company Name']=companies
        df_da['Job Title']=titles
        df_da['Location']=locations
        df_da['No.of applicants']=' '
        df_da['Description']=' '
        df_da['Level']=' '
        df_da['Type']=' '
        df_da['Function']=' '
        df_da['Industry']=' '
        df_da['Link']=links
        df_da['Review']=' '
        
        
        df_da.to_csv("Data jobs.csv", mode='a', header=False, index=0)