from bs4 import BeautifulSoup
import requests
import time


def scrape_jobs(unfamiliar_skills):
    print("Please Wait...")
    print(f"Filtering Out {unfamiliar_skills}")
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    job_listings = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job_listing in enumerate(job_listings):
        posted_date = job_listing.find('span', class_='sim-posted').span.text
        if 'few' in posted_date:
            company_name = job_listing.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job_listing.find('span', class_='srp-skills').text.replace(" ", "")
            more_info = job_listing.header.h2.a['href']
            if any(skill.lower() in skills.lower() for skill in unfamiliar_skills):
                continue
            with open(f'txtData/post{index}.txt', 'w') as f:
                f.write(f"Conpany Name: {company_name.strip()} \n")
                f.write(f"Skills: {skills.strip()} \n")
                f.write(f"Link to more info: {more_info} \n")
                f.write("<<---------------------------------------->>")
            print(f"Your files have been saved as post{index}.txt")


def main():
    run = True
    while run:
        print("What skills would you like to filter out??")
        unfamiliar_skills = input('>>').split()
        scrape_jobs(unfamiliar_skills)

        rerun = input("Do you want to rerun the scraper right now? (y/n)-->").lower()
        # time_wait = 10
        # print(f"waiting for {time_wait} seconds")
        # time.sleep(time_wait)
        while rerun != 'y':
            print("Crawler Dying....'dying noises'")
            run = False
            break


if __name__ == "__main__":
    main()
