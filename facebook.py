from selenium import webdriver
import time
import logging
import networkx as nx


def find_friends(driver):
    friends = driver.find_elements_by_class_name('_39g6')
    friends[1].click()
    time.sleep(5)
    try:
        driver.find_element('name', 'Mutual Friends').click()
        print('made it')
    except:
        pass
    friends = driver.find_elements_by_class_name('_698')
    return friends


# def process_friend(friend):
#     friend_name = friend.find_element_by_tag_name('a')
#     tmp = graph.Node(name=friend_name.text,link=friend_name.get_attribute('href'))
#     return tmp
def process_friend(friend):
    friend_name = friend.find_element_by_tag_name('a')
    return friend_name.get_attribute('href')


def make_graph():
    driver = webdriver.Chrome('/Users/mspear/Downloads/chromedriver')
    # driver.get('chrome://settings/advanced')
    # driver.find_element_by_id('privacyContentSettingsButton').click()
    # driver.find_element_by_name('popups').click()
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
    # g = graph.Graph()
    g = nx.Graph()

    # start = graph.Node('Michael Spear', 'https://www.facebook.com/michael.spear.94')
    g.add_node('https://www.facebook.com/michael.spear.94')


    # g.add_node(1, link='https://www.facebook.com/michael.spear.94')
    # g.add_node(start)
    queue = []
    for lv in friends:
        # V = process_friend(lv)
        # V.add_neighbor(start)
        # start.add_neighbor(V)
        # queue.append(V)
        # logging.info(V.link)
        # g.add_node(V)
        lnk = process_friend(lv)
        g.add_node(lnk)
        g.add_edge('https://www.facebook.com/michael.spear.94', lnk)
        queue.append(lnk)

    while queue:
        time.sleep(10)
        current = queue.pop()
        logging.info(f"Redirecting to {current}")
        driver.get(current)
        friends = find_friends(driver)
        for lv in friends:
            V = process_friend(lv)
            if V in g:
                # tmp = g.get(V.link)
                # tmp.add_neighbor(current)
                # current.add_neighbor(tmp)
                g.add_edge(current, V)
            else:
                g.add_node(V)
                g.add_edges_from([('https://www.facebook.com/michael.spear.94', V), (current, V)])

    driver.quit()

    return g

if __name__ == '__main__':
    import os
    import pickle
    if os.path.isfile('/Users/mspear/graph'):
        with open('/Users/mspear/graph', 'rb') as f:
            g = pickle.load(f)
    else:
        g = make_graph()
        with open('/Users/mspear/graph', 'wb') as f:
            pickle.dump(g, f)

    print(nx.clustering(g))
