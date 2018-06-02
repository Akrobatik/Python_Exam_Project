from selenium import webdriver
from time import sleep

pagenumber = 2
link_array = []

url = 'https://www.nyse.com/listings_directory/stock#'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
driver.implicitly_wait(3)
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/button').click()

table_body = driver.find_element_by_tag_name('tbody')
tr = table_body.find_elements_by_tag_name('tr')
sleep(3)
while True:
    try:
        sleep(3)
        for i in range(len(tr)):
            href = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('a')
            link_array.append(href[i].get_attribute('href'))
            print(href[i].get_attribute('href'))
        sleep(3)
        link = driver.find_element_by_link_text(str(pagenumber))
    except NoSuchElementException:
        break
    link.click()
    pagenumber += 1
    print(pagenumber)
driver.quit()
