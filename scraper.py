
import requests
from bs4 import BeautifulSoup
import csv

def scrape_jobs():
  
    URL = "https://realpython.github.io/fake-jobs/"
    
   
    print("Fetching webpage...")
    response = requests.get(URL)
    

    soup = BeautifulSoup(response.content, "html.parser")
   
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    
    jobs_list = []

    print(f"Found {len(job_elements)} job postings. Extracting data...")

   
    for job in job_elements:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        
     
        links = job.find_all("a")
        apply_link = links[1]["href"]

        jobs_list.append({
            "Job Title": title,
            "Company": company,
            "Location": location,
            "Application Link": apply_link
        })

 
    save_to_file(jobs_list)

def save_to_file(data):
    filename = "job_listings.csv"
    keys = data[0].keys()
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    
    print(f"Successfully created {filename}!")

if __name__ == "__main__":
    scrape_jobs()
