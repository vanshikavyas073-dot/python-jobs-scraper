
import requests
from bs4 import BeautifulSoup
import csv

def scrape_jobs():
    # The target URL for learning web scraping
    URL = "https://realpython.github.io/fake-jobs/"
    
    # 1. Fetch the webpage
    print("Fetching webpage...")
    response = requests.get(URL)
    
    # 2. Parse the HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 3. Target the main container
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    
    jobs_list = []

    print(f"Found {len(job_elements)} job postings. Extracting data...")

    # 4. Loop and Extract
    for job in job_elements:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        
        # Get the 'Apply' link (the second link in the footer)
        links = job.find_all("a")
        apply_link = links[1]["href"]

        jobs_list.append({
            "Job Title": title,
            "Company": company,
            "Location": location,
            "Application Link": apply_link
        })

    # 5. Save to CSV
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
