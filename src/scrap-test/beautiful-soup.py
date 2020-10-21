from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1820,1150")
    DRIVER_PATH = '/Users/oliverpozo/Desktop/EVS/honey-data-lake/binary/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.set_preference("http.response.timeout", 100)
    driver.set_preference("dom.max_script_run_time", 100)
    driver.get("https://news.google.com/search?q=ivey%20kay%20alabama%20when%3A1y&hl=en-US&gl=US&ceid=US%3Aen")
    print(driver.page_source)
    driver.quit()
    for headline in driver.find_elements_by_class_name('cd__headline-text'):
        print(headline.text)
    #print(driver.page_source)

except:
    pass
f = open('file.py', 'w')
f.write('dict = ' + repr(driver.page_source) + '\n')
f.close()
for headline in driver.find_elements_by_class_name('cd__headline-text'):
    print(headline.text)
