from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from os import listdir
from time import sleep

print("Enter username: ", end='')
uname = input()
print("Enter password: ", end='')
pword = input()
print("Enter a suitable caption for all uploads: ")
CAPTION = input()
#CAPTION = "Follow me for more\n\n#memesdarkerthan2020 #dankmemes #darkmemes #darkhumor #edgymemes #memesfordays #memesforfeens #dankmemesgang #nicememes #funnytexts #memestgram #darkmemes #legendarymemes #memegod #memepage #memepages #psatmemes #memer #softmemes #memefactory #dailymeme #highschoolmemes #bossmemesquad #memepage #funnyaccount #dankdank #memeaccount #memesdaily #memes "
INTERVAL = 1
cap = 4

print("Loading webdriver...")
opts = Options()
opts.add_argument("--headless")
driver = webdriver.Firefox(options = opts)
count = 1

#logging in
driver.get("https://www.instagram.com")
print("Logging in...")
wait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys(uname)
driver.find_element(By.NAME, "password").send_keys(pword)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(3)
driver.get("https://www.instagram.com")
try:
    wait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']"))).click() #Not Now button
except:
    print("Warning: Notification popup not detected.")
files = listdir("./instagram_uploads")
print("Starting..")

while(True):
    already_uploaded = []
    with open(f"./instagram_upload.var", "r") as f:
        lines = f.readlines()
        if len(lines) >= 1:
            already_uploaded = [x.replace("\n", "") for x in lines]
    for already_uploaded_file in already_uploaded:
        if already_uploaded_file in files:
            files.remove(already_uploaded_file)
    try:
        for file in files:
            driver.find_element(By.XPATH, "//*[contains(text(), 'Create')]").click()
            if(file.endswith('.mp4')):
                wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("K:\\dev\\rip\\uploads\\"+file)
                wait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]"))).click()
            else:
                wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("K:\\dev\\rip\\uploads\\"+file)
                wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Next')]")))
            btns = driver.find_elements(By.XPATH, "//button[@class=' _acan _acao _acas _aj1- _ap30']")
            c=0
            for i in btns:
                try:
                    c=1
                    i.click()
                except:
                    c=0
                if c==1:
                    break
            sleep(1)
            btns = driver.find_elements(By.XPATH, "//span[contains(text(), 'Original')]")
            c=0
            for i in btns:
                try:
                    c=1
                    i.click()
                except:
                    c=0
                if c==1:
                    break
            sleep(0.7)
            wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Next')]"))).click()
            wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Next')]"))).click()
            sleep(1)
            for char in CAPTION:
                if (char == '\n'):
                    driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(Keys.RETURN)
                else:
                    driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(char)
                sleep(0.03)
            sleep(1)
            driver.find_element(By.XPATH, "//div[contains(text(), 'Share')]").click()
            sleep(4.5)
            already_uploaded.append(file)
            with open(f"./instagram_upload.var", "a") as f:
                f.write(f"{file}\n")
            
            btns = driver.find_elements(By.XPATH, "//div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']")
            c=0
            for i in btns:
                try:
                    c=1
                    i.click()
                except:
                    c=0
                if c==1:
                    break
            if(count>=cap):
                break
            print(f"Upload complete: {file} ({count}/{min(cap, len(files))})")
            count+=1
            sleep(INTERVAL)
        print(f"Task completed: Uploaded {count} out of {min(cap, len(files))} files.")
        break
        
    except KeyboardInterrupt:
        print(f"Task interrupted: Uploaded {count-1} out of {min(cap, len(files))} files.")
        print("Do you want to terminate the task? (y/n): ", end='')
        d = input()
        if d=="y":
            print("Task terminated.")
            break
        else:
            print("Continuing...")
            continue
    except: 
        print("Encountered an error. Retrying...")
        driver.get("https://www.instagram.com") #reload page
        try:
            wait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']"))).click() #Not Now button
        except:
            print("Warning: Notification popup not detected.")
        sleep(3)
        continue

driver.quit()
