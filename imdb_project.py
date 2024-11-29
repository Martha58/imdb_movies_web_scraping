from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

url = 'https://m.imdb.com/chart/top/'
driver = webdriver.Edge()
driver.get(url)

title = []
year = []
duration = []
review = []

wait = WebDriverWait(driver, 20)
containers = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul.ipc-metadata-list > li')))

for x in containers:
    title.append(x.find_element(By.CSS_SELECTOR, 'h3').text)
    review.append(x.find_element(By.XPATH, './/span[contains(@class, "ratingGroup")]').text)
    metadata = x.find_elements(By.CSS_SELECTOR, 'div.cli-title-metadata > span')
    year.append(metadata[0].text)
    duration.append(metadata[1].text)

    # print(x.text)

df_movie = pd.DataFrame({'title' : title, 'year' : year, 'duration' : duration, 'review' : review})
df_movie.to_csv(r'C:\Users\martha\OneDrive\Python\imbd_project.csv', index=False)

