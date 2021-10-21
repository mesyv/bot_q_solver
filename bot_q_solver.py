from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import namedtuple
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time 
import random
import ujson as json
import re
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument(r"--user-data-dir=C:\Users\kamil\AppData\Local\Google\Chrome\User Data")
bot = webdriver.Chrome(executable_path=r"C:\Projekty\chromedriver.exe", chrome_options=chrome_options)
with open(r'C:\Projekty\Coding\bot_heinz_json.json', encoding='utf-8') as json_file:
    data3 = json.load(json_file, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

bot.get('https://heinzloween.pl/')
time.sleep(random.uniform(0.1, 0.9))

quizButton = bot.find_element_by_xpath('//button[@class="contest-quiz"]')  
quizButton.click()
time.sleep(random.uniform(0.1, 0.9))
mailInput = bot.find_element_by_xpath('//input[@id="email"]')
billInput = bot.find_element_by_xpath('//input[@id="bill_number"]')
dateInput = bot.find_element_by_xpath('//input[@name="bill_date"]')
mailInput.send_keys("jarkow163@gmail.com")
time.sleep(0.6531)
rdm = random.randrange(78912301, 99978912301)
billInput.send_keys(rdm)

#Tu wstawić jedną pętle json, zeby pozniej szybciej sie ladowal https://pythonspeed.com/articles/faster-json-library/


#Waiting for the date to be inserted
i = 0
while (i < 100):
    if (not dateInput.get_attribute('value')):
        time.sleep(4)
    else:
        startButton = bot.find_element_by_xpath('//div[@id="startQuiz"]')
        startButton.click()
        time.sleep(0.6)
        break
    i += 1
#Quiz Starts
print("------------------------Quiz starts------------------------")
i = 1
j = 1
while (i <= 10):
    time.sleep(0.1)
    try:
        print(f"--------------------------------New loop:{i}-------------------------------")
        question = bot.find_element_by_xpath(f'//div[contains(@id,"question_{i}")]').text.split("\n")[0]
        answer1 = bot.find_element_by_xpath(f'//div[contains(@id,"question_{i}")]').text.split("\n")[1]
        answer2 = bot.find_element_by_xpath(f'//div[contains(@id,"question_{i}")]').text.split("\n")[2]
        answer3 = bot.find_element_by_xpath(f'//div[contains(@id,"question_{i}")]').text.split("\n")[3]
        answer4 = bot.find_element_by_xpath(f'//div[contains(@id,"question_{i}")]').text.split("\n")[4]
        print(f"Question:{question}")
        print(f"{answer1} | {answer2} | {answer3} | {answer4}")
        
        for obj in data3:
            if obj.question.lower() in question.lower():
                print("Question found!")
                if obj.answer.replace(" ", "") == answer1.replace(" ", ""):
                    j = 1
                    answer = bot.find_element_by_xpath(f"/html/body/main/section[4]/div/div[2]/form/div[{i}]/div/div/div[{j}]/label")
                    print("obj.answer:", obj.answer, " #:", j)
                    break
                elif obj.answer.replace(" ", "") == answer2.replace(" ", ""):
                    j = 2
                    answer = bot.find_element_by_xpath(f"/html/body/main/section[4]/div/div[2]/form/div[{i}]/div/div/div[{j}]/label")
                    print("obj.answer:", obj.answer, " #:", j)
                    break
                elif obj.answer.replace(" ", "") == answer3.replace(" ", ""):
                    j = 3
                    answer = bot.find_element_by_xpath(f"/html/body/main/section[4]/div/div[2]/form/div[{i}]/div/div/div[{j}]/label")
                    print("obj.answer:", obj.answer, " #:", j)
                    break
                elif obj.answer.replace(" ", "") == answer4.replace(" ", ""):
                    j = 4
                    answer = bot.find_element_by_xpath(f"/html/body/main/section[4]/div/div[2]/form/div[{i}]/div/div/div[{j}]/label")
                    print("obj.answer:", obj.answer, " #:", j)
                    break
            else: #answer = A
                answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer1[:len(answer1)//2]+"')]")
        try:
            print(f"Click to:{answer.text}")
            answer.click()
            print("OK!")
        except:
            try:
                print(f"FAIL! Trying 2nd click... j={j}")
                if (j == 1):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer1[:len(answer1)//2]+"')]")
                if (j == 2):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer2[:len(answer2)//2]+"')]")
                if (j == 3):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer3[:len(answer3)//2]+"')]")
                if (j == 4):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer4[:len(answer4)//2]+"')]")
                answer.click()
                print(f"OK! Click to:{answer.text}")
            except:
                print(f"FAIL! Trying 3nd click... j={j}")
                if (j == 1):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer1[len(answer1)//2:]+"')]")
                if (j == 2):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer2[len(answer2)//2:]+"')]")
                if (j == 3):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer3[len(answer3)//2:]+"')]")
                if (j == 4):
                    answer = bot.find_element_by_xpath("//label[contains(text(),'"+answer4[len(answer4)//2:]+"')]")
                answer.click()
                print(f"OK! Click to:{answer.text}")
            pass
        # try:
        #     clock = bot.find_element_by_xpath("//div[@id='timer']")
        #     print("Time left:",clock.text)
        # except:
        #     pass
    except:
        pass
    time.sleep(4.2)
    i += 1
