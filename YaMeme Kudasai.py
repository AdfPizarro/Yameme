import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options





def splash():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ""
    print ""
    print ""
    print "     __   __   ___  ___                       _   __          _                 _ "
    print "     \ \ / /   |  \/  |                      | | / /         | |               (_)"
    print "      \ V /__ _| .  . | ___ _ __ ___   ___   | |/ / _   _  __| | __ _ ___  __ _ _ "
    print "       \ // _` | |\/| |/ _ \ '_ ` _ \ / _ \  |    \| | | |/ _` |/ _` / __|/ _` | |"
    print "       | | (_| | |  | |  __/ | | | | |  __/  | |\  \ |_| | (_| | (_| \__ \ (_| | |"
    print "       \_/\__,_\_|  |_/\___|_| |_| |_|\___|  \_| \_/\__,_|\__,_|\__,_|___/\__,_|_|"

    print ""
    entries = os.listdir('memes/')
    print "      ",len(entries), "Memes"


    print ""
    wt = raw_input("     Presiona una tecla para continuar con la verificacion de whatsapp ")



def openBrowser():
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.maximize_window()
    time.sleep(3)
    return driver

def login(driver):

    path=os.path.dirname(os.path.abspath(__file__))



    try:
        driver.get("https://web.whatsapp.com/")
        print "Scan the qr"
        sec = raw_input('Select the target and pres enter when you are ready .\n')

        entries = os.listdir('memes/')
        index=0
        bufferIndex=0
        buffer=[]
        for entry in entries:

            if bufferIndex < 20:
                file=path+entry
                buffer.append(file)
                bufferIndex+=1

            else:
                bufferIndex=0

                print "Sending file ",index,"/",len(entries)
                driver.find_element_by_css_selector("span[data-icon='clip']").click();

                time.sleep(1)

                image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(buffer[0],"\n",buffer[1],"\n",buffer[2],"\n",buffer[3],"\n",buffer[4],"\n",buffer[5],"\n",buffer[6],"\n",buffer[7],"\n",buffer[8],"\n",buffer[9],
                                    buffer[10],"\n",buffer[11],"\n",buffer[12],"\n",buffer[13],"\n",buffer[14],"\n",buffer[15],"\n",buffer[16],"\n",buffer[17],"\n",buffer[18],"\n",buffer[19])
                time.sleep(3)
                driver.find_element_by_css_selector("span[data-icon='send']").click();
                time.sleep(1)
                index += 10
                buffer=[]



        print "Done"


    except Exception as e:
        print(e)





def close(driver):
    driver.close()

splash()
driver=openBrowser()
login(driver)
