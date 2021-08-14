import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "eager"
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(capabilities=caps,firefox_profile=firefox_profile)

al=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
aln=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
for one in al:
    for two in al:
        for three in al:
            for four in aln:
                for five in aln:
                    for six in aln:
                        alnum=one+two+three+four+five+six
                        fulllink="https://prnt.sc/"+one+two+three+four+five+six
                        driver.get(fulllink)
                        WebDriverWait(driver, timeout=10).until(
                            ec.visibility_of_element_located((By.XPATH, '//*[@id="screenshot-image"]'))
                        )
                        try:
                            imglink = driver.find_element_by_xpath('//*[@id="screenshot-image"]').get_attribute('src')
                            print(imglink)

                            if imglink == fulllink:
                                continue
                        except:
                            continue
                        URL = imglink
                        with open("./tmp/"+alnum+".png", "wb") as f:
                            f.write(requests.get(URL).content)

