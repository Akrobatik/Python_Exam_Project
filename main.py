from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException


# Setting up the variables
url = 'https://www.nyse.com/listings_directory/stock'
file_name = './quote1.csv'
page_number = 2
backup_list = []
# Setting the driver to Chrome
driver = webdriver.Chrome('./chromedriver')
# Sets the URL in browser to String url
driver.get(url)
# Close modal
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/button').click()
driver.implicitly_wait(3)
# Go to tbody -> Then to tr - > Then td
table_body = driver.find_element_by_tag_name('tbody')
tr = table_body.find_elements_by_tag_name('tr')
sleep(3)
# Find td and save to array list
while True:
    try:
        sleep(3)
        with open(file_name, 'a') as file_object:
            for i in range(len(tr)):
                a_tag = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('a')
                link = (a_tag[i].get_attribute('href'))
                if (link == 'https://www.nyse.com/quote/XASE:AJAX'):
                    link = 'https://www.nyse.com/quote/XNYS:AJG'
                backup_list.append(link)
                print(backup_list)
                link_symbol = a_tag[i].get_attribute('textContent')
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(link)
                sleep(4)
                name = driver.find_element_by_xpath('//*[@id="content-9d1f8b01-08a6-4db5-99fa-c40f5873615a"]/div/div[1]/header/h1').get_attribute('textContent')
                quote = driver.find_element_by_css_selector('span.d-dquote-x3').get_attribute('textContent')
                file_object.write(name + ', ' + link_symbol + ', ' + quote + '\n')
                sleep(3)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        link = driver.find_element_by_link_text(str(page_number))
    except NoSuchElementException:
        raise
    link.click()
    page_number += 1
sleep(3)

print(saved_data)
# Close the only tab, will also close the browser.
driver.close()
