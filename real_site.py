import requests
from bs4 import BeautifulSoup
import time

def makeitpretty(Job_Skills):
	Job_Skills = Job_Skills.strip()
	Job_Skills = Job_Skills.replace(" ","")
	Job_Skills = Job_Skills.replace("\n\n","")
	Job_Skills = Job_Skills.replace("(MoreJobs)","")
	Job_Skills = " ".join(Job_Skills.split())
	return Job_Skills

print("Enter the skills you know: ")
Skill_required = input()
print(">Filtering Out The Webs")


def Find_Job_Openings():
	website_text = requests.get('https://www.timesjobs.com/jobfunction/it-software-jobs').text
	contents = BeautifulSoup(website_text,'lxml')
	contents.prettify()
	Job_Posting = contents.find_all('li',class_='clearfix joblistli')
	for index,content in enumerate(Job_Posting):

		Job_Requirement = content.find('ul',class_='job-more-dtl clearfix')
		#print(Job_Requirements)
		Job_Requirements = Job_Requirement.find('li').text
		Job_Requirements_Years_Formatted = makeitpretty(f"{Job_Requirements[0:5]}")

		if "0-" in Job_Requirements_Years_Formatted:
			Job_Company = content.find('h3',class_="joblist-comp-name").text
			Job_Desc = content.find('ul',class_='job-dtl clearfix')
			Job_Skills = Job_Desc.find('li',class_='disc').text
			if Skill_required in Job_Skills:
				with open(f'C:/Users/shars/Desktop/Python/Web_Scraping/Posts/{index}.txt','r+') as f:
					f.write(f"Company Name: {makeitpretty(Job_Company)}\n{makeitpretty(Job_Skills)[0:9]}: {makeitpretty(Job_Skills)[10:]} \nExperience Required in Years: {Job_Requirements_Years_Formatted}\n")
					f.write(f"Link: {content.header.h2.a['href']} \n")
					print(f"File Saved {index}")

if __name__ == "__main__":
	while True:
		print("Welcome Let's Find You A Job")
		Find_Job_Openings()
		time.sleep(10)