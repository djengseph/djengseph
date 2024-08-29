from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from termcolor import colored
from bs4 import BeautifulSoup
import requests
import time
import random
import pyautogui
import os
ascii_banner = 'YOUTUBE PLAYLIST V6'
byx = 'BY FAIQ ID\n'
x = byx.center(50)
z = ascii_banner.center(50)
os.system('cls' if os.name == 'nt' else 'clear')
print(colored(z, 'red'))
print(colored(x, 'green'))
license_url = 'https://raw.githubusercontent.com/faiqxid/botyt/main/lplaylist.txt'
headers = {'Authorization': 'Token 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'}
response = requests.get(license_url, headers=headers).text
license_keys = response.splitlines()

def check_license(key):
    return key in license_keys
user_key = input(colored('Masukan lisensi key Yang Sudah Terdaftar: ', 'green'))
if check_license(user_key):
    print(colored('lisensi key valid. Script dapat dijalankan.', 'green'))
    time.sleep(2)
else:  # inserted
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored('lisensi key tidak valid. \nUntuk Mendapatkan lisensi key Silahkan Hubungu Contact Di Bawah Ini \nWhatsapp 1 : +6285648758597 \nWhatsapp 2 : +6285798836607 \nEmail : Faiqid123456@gmail.com \nfacebook : https://www.facebook.com/xutoy', 'red'))
    os._exit(0)
os.system('cls' if os.name == 'nt' else 'clear')
print(colored(z, 'red'))
print(colored(x, 'green'))
mltilangu = input(colored('Aktifkan Multi Bahasa Yes Or No : ', 'blue'))
email = input(colored('Email : ', 'blue'))
pwd = input(colored('Password : ', 'blue'))
jumchnl = input(colored('Jumlah Channel : ', 'blue'))
muldr = input(colored('Mulai Dari Channel Ke Berapa : ', 'blue'))
files = input(colored('Masukan Data Excel Format .xlsx : ', 'blue'))
jumplyst = input(colored('Masukan Jumlah Playlist Yang Mau Dibuat : ', 'blue'))
if mltilangu == 'Yes' or mltilangu == 'yes':
    mtlang = 'aktif'
else:  # inserted
    mtlang = 'nonaktif'
options = webdriver.ChromeOptions()
options.add_argument('--lang=en-US')
options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
prefs = {'profile.default_content_setting_values.notifications': 2}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)
wb = load_workbook(filename=files)
sheetRange = wb['Sheet1']
driver.get('https://youtube.com/channel_switcher')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"identifierId\"]')))
emailes = driver.find_element(By.XPATH, '//*[@id=\"identifierId\"]')
emailes.send_keys(email)
next1 = driver.find_element(By.XPATH, '//*[@id=\"identifierNext\"]/div/button')
next1.click()
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"password\"]/div[1]/div/div[1]/input')))
passw = driver.find_element(By.XPATH, '//*[@id=\"password\"]/div[1]/div/div[1]/input')
passw.send_keys(pwd)
next2 = driver.find_element(By.XPATH, '//*[@id=\"passwordNext\"]/div/button')
next2.click()
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"contents\"]/ytd-account-item-renderer[2]')))
cnl = driver.find_element(By.XPATH, '//div[@id=\"contents\"]/ytd-account-item-renderer[2]')
cnl.click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"body\"]')))
gethtml = driver.find_element(By.XPATH, '//div[@id=\"body\"]').get_attribute('innerHTML')
basehtml = BeautifulSoup(gethtml, 'html.parser')
getcontents = basehtml.find('div', {'id': 'contents'}).find_all('ytd-account-item-renderer')
totch = len(getcontents)
totchnl = totch - 1
allchnlname = {}
for nmch in range(0, int(totchnl)):
    jch = nmch + 1
    getchname = getcontents[jch].find('yt-formatted-string', {'id': 'channel-title'}).text
    allchnlname['ch{0}'.format(jch)] = getchname
for zoom in range(0, 5):
    pyautogui.hotkey('ctrl', '-')
    time.sleep(1)
driver.get('https://studio.youtube.com/')
for zoom2 in range(0, 5):
    pyautogui.hotkey('ctrl', '-')
    time.sleep(1)
for i in range(int(muldr), int(jumchnl)):
    vid = i + 1
    chanelname = allchnlname['ch' + str(i)]
    driver.get('https://studio.youtube.com/')
    print(colored('Channel : ' + chanelname, 'green'), colored(i, 'red'))
    try:
        contyy = driver.find_element(By.XPATH, '//ytcp-button[@id=\"dismiss-button\"]/div')
        contyy.click()
        time.sleep(1)
    except:
        pass
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//button[@id=\"avatar-btn\"]')))
    swchnl = driver.find_element(By.XPATH, '//button[@id=\"avatar-btn\"]')
    swchnl.click()
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"items\"]/ytd-compact-link-renderer[3]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')))
    swchnls = driver.find_element(By.XPATH, '//div[@id=\"items\"]/ytd-compact-link-renderer[3]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')
    swchnls.click()
    time.sleep(4)
    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//yt-formatted-string[@id=\"channel-title\"][text()=\"' + chanelname + '\"]')))
        tochnl = driver.find_element(By.XPATH, '//yt-formatted-string[@id=\"channel-title\"][text()=\"' + chanelname + '\"]')
        tochnl.location_once_scrolled_into_view
        tochnl.click()
        time.sleep(4)
    except:
        print('Channel Habis')
        break
    if mtlang == 'aktif':
        driver.get('https://www.youtube.com/')
        time.sleep(3)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//button[@id=\"avatar-btn\"]')))
        clikavt = driver.find_element(By.XPATH, '//button[@id=\"avatar-btn\"]')
        clikavt.click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"container\"]/div[1]/yt-multi-page-menu-section-renderer[3]/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item')))
        clibhs = driver.find_element(By.XPATH, '//div[@id=\"container\"]/div[1]/yt-multi-page-menu-section-renderer[3]/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item')
        clibhs.click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//yt-formatted-string[contains(text(),\"English (US)\")]')))
        toengus = driver.find_element(By.XPATH, '//yt-formatted-string[contains(text(),\"English (US)\")]')
        toengus.location_once_scrolled_into_view
        toengus.click()
        time.sleep(3)
    else:  # inserted
        pass
    driver.get('https://studio.youtube.com/')
    try:
        conty = driver.find_element(By.XPATH, '//ytcp-button[@id=\"dismiss-button\"]/div')
        conty.click()
        time.sleep(1)
    except:
        pass
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//ul[@id=\"main-menu\"]/li[2]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')))
    konten = driver.find_element(By.XPATH, '//ul[@id=\"main-menu\"]/li[2]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')
    konten.click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')))
    playlys = driver.find_element(By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')
    playlys.click()
    tit = i * int(jumplyst)
    dsk = tit + int(jumplyst)
    for det in range(tit, dsk):
        data = det + 1 - int(jumplyst)
        linkstrm = sheetRange['A' + str(data)].value
        redirytb = sheetRange['B' + str(data)].value
        judul = sheetRange['C' + str(data)].value
        keywvid = sheetRange['D' + str(data)].value
        desc1 = sheetRange['E' + str(data)].value
        desc2 = sheetRange['F' + str(data)].value
        hastag = sheetRange['G' + str(data)].value
        des5 = sheetRange['H' + str(data)].value
        des6 = sheetRange['I' + str(data)].value
        description = f'LIVE STREAMING {judul}\n{redirytb}\n\n{desc1}\n{desc2}\n\n{des5} vs {des6}\n{des5} Vs. {des6}\n{des5} @ {des6}\n{des5} AT {des6}\n{des6} AT {des5}\n{des6} Vs {des5}\n\nTAG :\n{hastag}'
        print(colored('PLAYLIST KE : ', 'green'), colored(data, 'red'))
        try:
            contysy = driver.find_element(By.XPATH, '//ytcp-button[@id=\"dismiss-button\"]/div')
            contysy.click()
            time.sleep(1)
        except:
            pass
        time.sleep(1)
        try:
            clsntfy = driver.find_element(By.XPATH, '//body[@id=\"html-body\"]/ytcp-feature-discovery-callout/div/div[3]/ytcp-button/div')
            clsntfy.click()
            time.sleep(1)
        except:
            pass
        time.sleep(1)
        try:
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//nav[@id=\"left-nav\"]/ytcp-animatable/ul/li[1]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')))
            dasb = driver.find_element(By.XPATH, '//nav[@id=\"left-nav\"]/ytcp-animatable/ul/li[1]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')
            dasb.click()
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//ytcp-button[@id=\"create-icon\"]/tp-yt-iron-icon')))
            cret = driver.find_element(By.XPATH, '//ytcp-button[@id=\"create-icon\"]/tp-yt-iron-icon')
            cret.click()
            time.sleep(2)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-item[@test-id=\"new-playlist\"]/ytcp-ve')))
            cretply = driver.find_element(By.XPATH, '//tp-yt-paper-item[@test-id=\"new-playlist\"]/ytcp-ve')
            cretply.click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//ytcp-social-suggestions-textbox[@id=\"title-textarea\"]/ytcp-form-input-container/div[1]/div/div/ytcp-social-suggestion-input/div')))
            judlb = driver.find_element(By.XPATH, '//ytcp-social-suggestions-textbox[@id=\"title-textarea\"]/ytcp-form-input-container/div[1]/div/div/ytcp-social-suggestion-input/div')
            judlb.send_keys(judul)
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add description\"]')))
            deskrpsy = driver.find_element(By.XPATH, '//div[@aria-label=\"Add description\"]')
            deskrpsy.send_keys(description)
            time.sleep(2)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//ytcp-button[@id=\"create-button\"]')))
            creates = driver.find_element(By.XPATH, '//ytcp-button[@id=\"create-button\"]')
            creates.click()
            time.sleep(3)
        else:  # inserted
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//ul[@id=\"main-menu\"]/li[2]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')))
                kontens = driver.find_element(By.XPATH, '//ul[@id=\"main-menu\"]/li[2]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')
                kontens.click()
            except:
                print(colored('PLAYLIST LIMITED', 'red'))
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//ytcp-button[@label=\"Cancel\"]/div')))
                clslmt = driver.find_element(By.XPATH, '//ytcp-button[@label=\"Cancel\"]/div')
                clslmt.click()
                time.sleep(2)
                break
        else:  # inserted
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')))
            playlyss = driver.find_element(By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')
            playlyss.click()
        else:  # inserted
            try:
                contysys = driver.find_element(By.XPATH, '//ytcp-button[@id=\"dismiss-button\"]/div')
                contysys.click()
                time.sleep(1)
            except:
                pass
        else:  # inserted
            try:
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a')))
                linkplys = driver.find_element(By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a').get_attribute('href')
                time.sleep(1)
                if 'studio.' in linkplys:
                    removeedit = linkplys.replace('/edit', '')
                    linkplyst = removeedit.replace('studio.youtube.com/playlist/', 'youtube.com/playlist?list=')
                else:  # inserted
                    linkplyst = linkplys
                driver.execute_script('window.open(\'\');')
                driver.switch_to.window(driver.window_handles[1])
                driver.get(linkplyst)
                time.sleep(1)
            except:
                driver.refresh()
                time.sleep(1)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a')))
                linkplys = driver.find_element(By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a').get_attribute('href')
                time.sleep(1)
                driver.execute_script('window.open(\'\');')
                driver.switch_to.window(driver.window_handles[1])
                driver.get(linkplys)
                time.sleep(1)
        else:  # inserted
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label=\"Add videos\"]')))
                advidnew = driver.find_element(By.XPATH, '//button[@aria-label=\"Add videos\"]')
                advidnew.click()
            except:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')))
                seti = driver.find_element(By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')
                seti.click()
                time.sleep(1)
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')))
                advid = driver.find_element(By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')
                advid.click()
        else:  # inserted
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe'))
            except:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe'))
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[2]')))
            adevn = driver.find_element(By.XPATH, '//input[2]')
            adevn.send_keys(linkstrm)
            adevn.send_keys(Keys.ENTER)
            time.sleep(2)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div')))
            adevnvid = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div')
            adevnvid.click()
            time.sleep(1)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')))
            svadevnvid = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')
            svadevnvid.click()
            time.sleep(2)
            driver.switch_to.default_content()
        else:  # inserted
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label=\"Add videos\"]')))
                advidnew1 = driver.find_element(By.XPATH, '//button[@aria-label=\"Add videos\"]')
                advidnew1.click()
            except:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')))
                seti1 = driver.find_element(By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')
                seti1.click()
                time.sleep(1)
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')))
                advid1 = driver.find_element(By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')
                advid1.click()
        else:  # inserted
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe'))
            except:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe'))
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[2]')))
            adevn1 = driver.find_element(By.XPATH, '//input[2]')
            adevn1.send_keys(keywvid)
            adevn1.send_keys(Keys.ENTER)
            time.sleep(2)
            rand = random.randint(21, 26)
        else:  # inserted
            try:
                for advidtoply in range(0, rand):
                    selvid = advidtoply + 1
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[' + str(selvid) + ']/div')))
                    advidtopls = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[' + str(selvid) + ']/div')
                    advidtopls.location_once_scrolled_into_view
                    advidtopls.click()
            except:
                pass
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')))
            svadevnvid1 = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')
            svadevnvid1.click()
            time.sleep(5)
            driver.switch_to.default_content()
            print(str(advidtoply) + ' Video Added to Playlist')
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except:
        print('Video Not Added to Playlist')
        pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
print('Playlist Created Successfully')
driver.quit()