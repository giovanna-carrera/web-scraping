from selenium import webdriver
import csv
import time

# You may need to add delays or wait for specific elements if the content is dynamically loaded
# For example:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a new browser session
driver = webdriver.Chrome()

# Navigate to the desired website
#driver.get('https://app.dealroom.co/dashboard')
#driver.get('https://www.custorino.it/corsi/calcio-a-5/calcio-a-5-femminile-adulti-universitari/')
#driver.get('https://www.youtube.com/')
#driver.get('https://www.crunchbase.com/discover/organization.companies')
#driver.get('https://www.youtube.com/results?search_query=annalisa')
driver.get('https://app.dealroom.co/companies.startups/f/business_models/anyof_manufacturing/employees_max/anyof_100/industries/anyof_space/launch_year_min/anyof_2019/startup_ranking_rating_min/anyof_1/total_funding_max/anyof_1000000?sort=-startup_ranking_rating')

time.sleep(120)

#element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.ID, "some_id")))

# Extract content or interact with the page
# For example, get page source:
page_source = driver.page_source

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Always close the driver after you're done
driver.close()

# Process the `page_source` with your desired parsing library (like BeautifulSoup)

from bs4 import BeautifulSoup

# Assuming `page_source` contains the HTML content you got from Selenium
soup = BeautifulSoup(page_source, 'lxml')



#for script in soup(["script", "style"]):
#    script.extract()

print(soup)

#clean_text = soup.get_text()
#print(clean_text)

#title = soup.find('title').text
#print(title)

#links = soup.find_all('a')
#divs = soup.find_all('div')
#for div in divs:
    #print(div.get('title'))


#for link in links:
#    print(link.get('href'))

# Esempio: Supponiamo di voler estrarre tutti i testi dei paragrafi <p>
paragraphs = soup.find_all('p')
data = [p.text for p in paragraphs]

# 3. Salva i dati in CSV
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Paragraph'])  # intestazione
    for item in data:
        writer.writerow([item])