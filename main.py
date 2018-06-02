from selenium import webdriver
from time import sleep

# Setting up the variables
url = 'https://www.nyse.com/listings_directory/stock'
link_array = []
saved_data = []
page_number = 0;
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
        for i in range(len(tr)):
            href = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('a')
            link_array.append(href[i].get_attribute('href'))
        sleep(3)
        # Starts the loop which opens a new tab, scrapes Quote, closes the tab and re enters loop
        for i in range(len(link_array)):
            # Open a new window
            # This does not change focus to the new window for the driver.
            driver.execute_script("window.open('');")
            sleep(3)
            # Switch to the new window
            driver.switch_to.window(driver.window_handles[1])
            driver.get(link_array[i])
            sleep(4)
            # Do scraping
            quote = driver.find_element_by_css_selector('span.d-dquote-x3').get_attribute('textContent')
            print(quote)
            saved_data.append(quote)
            # close the active tab
            driver.close()
            sleep(3)
            # Switch back to the first tab
            driver.switch_to.window(driver.window_handles[0])
            driver.get(url)
            sleep(3)
        link = driver.find_element_by_link_text(str(page_number))
    except NoSuchElementException:
        driver.quit()
        break
    link.click()
    page_number += 1
sleep(3)

print(saved_data)
# Close the only tab, will also close the browser.
driver.close()
