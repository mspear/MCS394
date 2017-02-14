from selenium import webdriver
import base64
import time
import graph


def find_friends(driver):
    friends = driver.find_elements_by_class_name('_39g6')
    friends[1].click()
    time.sleep(5)
    friends = driver.find_elements_by_class_name('_698')
    return friends


def main():
    driver = webdriver.Chrome('/Users/mspear/Downloads/chromedriver')

    driver.get('http://www.facebook.com')
    time.sleep(5)
    email = driver.find_element_by_id('email')
    email.send_keys('mwspear@gmail.com')
    password = driver.find_element_by_id('pass')
    with open('/Users/mspear/password.txt', 'r') as f:
        password.send_keys(f.read())

    # button = driver.find_element_by_id('loginbutton')
    # button.click()
    print('made it')

    time.sleep(10)

    profile = driver.find_element_by_class_name('_2s25')
    profile.click()
    time.sleep(10)


    friends = find_friends(driver)
    g = graph.Graph()
    queue = []
    for lv in friends:
        friend_name = lv.find_element_by_tag_name('a')
        tmp = graph.Node(friend_name)
        g.add_node(friend_name.get_attribute('href'))
        queue.append(tmp)
        time.sleep(5)


    # mutual_friends = driver.find_element_by_class_name('_3c_')

    driver.quit()

    return g

if __name__ == '__main__':
    main()
