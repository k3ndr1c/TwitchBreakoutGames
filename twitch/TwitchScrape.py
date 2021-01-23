from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from django.conf import settings
import time


def viewToInt(viewStr):
    """ Converts viewers to string appropriately. """
    viewStr = viewStr.replace(' viewers', '')
    if 'K' in viewStr:
        viewersInt = int(float(viewStr[:-1]))
        return viewersInt * 1000
    else:
        viewersInt = int(viewStr)
    return viewersInt


def gameStats(new_soup, titlelist, viewerlimit):
    """ Gets all the games, and adds to given list """
    allGames = new_soup.findAll('div', class_='tw-card-body tw-relative')
    for game in allGames:
        title = game.find('h3', class_='tw-ellipsis tw-font-size-5 tw-line-height-body').get_text()
        viewers = game.find('p', class_='tw-c-text-alt-2 tw-ellipsis').get_text()
        viewersInt = viewToInt(viewers)
        if viewersInt < viewerlimit:
            break
        titlelist.append((title, viewersInt))


def scroll(wbdriver, timeout):
    """ Scrolls the driver 10 times to load multiple games. """
    scroll_pause_time = timeout
    card = wbdriver.find_element_by_xpath('//a[@data-a-target="card-0"]')
    i = 1
    while i < 10:
        card.send_keys(Keys.END)
        i += 1
        time.sleep(scroll_pause_time)
    bsoup = BeautifulSoup(wbdriver.page_source, 'html.parser')
    return bsoup


def scrape():
    """ Main method to start scraper and populate list of games. """
    gameList = []
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options, executable_path=settings.DRIVER_PATH)
    driver.get(settings.TWITCH_URL)
    time.sleep(10)

    soup = scroll(driver, 3)
    driver.quit()
    gameStats(soup, gameList, settings.VIEWER_LIMIT)

    return gameList

