x=[]
y=[]

def get():
    from selenium import webdriver
    import time
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    path_to_extension = '/content/drive/MyDrive/3.5.31_0'
    chrome_options.add_argument('load-extension=' + path_to_extension)
    prefs = {'download.default_directory' : '/content/drive/MyDrive/myBot/'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver =webdriver.Chrome('chromedriver',options=chrome_options)

    with open('/content/drive/MyDrive/Ben 10 OM/urls.txt') as f:
          links = [line.rstrip() for line in f]
    for link in links:
        driver.get(link)
        try:
          driver.execute_script("window.scrollTo(0, 750)")
          WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#downloadvideo"))).click()
          time.sleep(7)
          WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#downloadvideo"))).click()
        except:
          print('N/A')
        # time.sleep(5)
        # try:
        #     z=driver.find_element_by_css_selector("#fileInfoDownload")
        # x.append(z.get_attribute('href'))
        # y.append(driver.find_element_by_css_selector("#content > div > div:nth-child(1) > div.col-12.text-center.video-title > h2").text)
        # print(driver.find_element_by_css_selector("#content > div > div:nth-child(1) > div.col-12.text-center.video-title > h2").text)
        # except:
        #   print('File expired')
        import time
        import os
        path = "/content/drive/MyDrive/myBot/"
        def download_wait(path):
            t=0
            while True:
                print('Waiting....')
                time.sleep(60)
                for fname in os.listdir(path):
                    if fname.endswith('.crdownload'):
                        t=0
                        break
                    else:
                        t=1
                if t==1:
                  print('Done')
                  return
        download_wait(path)

get()
print('Link Loaded')

# import os
# os.chdir("/content/drive/MyDrive")

# for i in range(0,len(x),1):
#   import urllib.request
#   urllib.request.urlretrieve(x[i], str(y[i]))
#   print(i) 
print('Done')
