import json
import time
from selenium import webdriver

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome(options=chrome_options)
ids = ["7502588",
"7455393",
"7448569",
"7384324",
"7135456",
"7091374",
"7055232",
"7018690",
"6928777",
"6924559",
"6890428",
"6851747",
"6824168",
"6786111",
"6761305",
"6726661",
"6690260",
"6657202",
"6657198",
"6604986",
"6568193",
"6533088",
"6500319",
"6480097",
"6453163",
"6453150",
"6260317",
"6260309",
"6229681",
"6199270",
"6199262",
"6147841",
"6044559",
"6044553",
"6044538",
"5986025",
"5986020",
"5733493",
"5606986",
"5535086",
"5503268",
"5471329",
"5450748",
"5409897",
"5349072",
"5287045",
"5221162",
"5194898",
"5059456",
"5021682",
"4993095",
"4972419",
"4896249",
"4886556",
"4861581",
"4809966",
"4809965",
"4785182",
"4751766",
"4743617"]

#Giving 20 seconds for user log in, the session will be kept for the other accesses
driver.get('https://edh.cern.ch/Document/{id:s}'.format(id=ids[0]))
time.sleep(20)
for id in reversed(ids):
    driver.get('https://edh.cern.ch/Document/{id:s}'.format(id=id))
    driver.execute_script('window.print();')

