from selenium import webdriver
import time
import graph
import logging


def find_friends(driver):
    friends = driver.find_elements_by_class_name('_39g6')
    friends[1].click()
    time.sleep(5)
    friends = driver.find_elements_by_class_name('_698')
    return friends


def process_friend(friend):
    friend_name = friend.find_element_by_tag_name('a')
    tmp = graph.Node(name=friend_name.text,link=friend_name.get_attribute('href'))
    time.sleep(5)
    return tmp


def main():
    driver = webdriver.Chrome('/Users/mspear/Downloads/chromedriver')

    driver.get('http://www.facebook.com')
    time.sleep(5)
    email = driver.find_element_by_id('email')
    email.send_keys('mwspear@gmail.com')
    password = driver.find_element_by_id('pass')
    with open('/Users/mspear/password.txt', 'r') as f:
        password.send_keys(f.read())

    time.sleep(10)

    profile = driver.find_element_by_class_name('_2s25')
    profile.click()
    time.sleep(10)

    friends = find_friends(driver)
    g = graph.Graph()
    queue = []
    for lv in friends:
        V = process_friend(lv)
        queue.append(V)
        logging.info(V.link)
        g.add_node(V)

    while queue:
        time.sleep(5)
        current = queue.pop()
        logging.info(f"Redirecting to {current.link}")
        driver.get(current.link)
        friends = find_friends(driver)
        for lv in friends:
            V = process_friend(lv)
            if V in g:
                print('Found duplicate', V.link)
                tmp = g.get(V)
                tmp.add_neighbor(current)
                current.add_neighbor(tmp)
            else:
                g.add_node(V)

    driver.quit()

    return g





if __name__ == '__main__':
    main()
