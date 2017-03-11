from selenium import webdriver
import time
import networkx as nx


def find_friends(driver):
    friends = driver.find_elements_by_class_name('_39g6')
    friends[1].click()
    time.sleep(5)
    try:
        driver.find_element('name', 'Mutual Friends').click()
    except:
        pass
    friends = driver.find_elements_by_class_name('_698')
    return friends


def process_friend(friend):
    friend_name = friend.find_element_by_tag_name('a')
    return friend_name.get_attribute('href')


def make_graph():
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

    g = nx.Graph()

    g.add_node('https://www.facebook.com/michael.spear.94')

    queue = []
    for lv in friends:
        lnk = process_friend(lv)
        # g.add_node(lnk)
        g.add_edge('https://www.facebook.com/michael.spear.94', lnk)
        queue.append(lnk)

    while queue:
        time.sleep(10)
        current = queue.pop()
        driver.get(current)
        friends = find_friends(driver)
        for lv in friends:
            V = process_friend(lv)
            g.add_edge(current, V)
            # if V in g:
            #     g.add_edge(current, V)
            # else:
            #     # g.add_node(V)
            #     #g.add_edges_from([('https://www.facebook.com/michael.spear.94', V), (current, V)])
            #     g.add_edge(current, V)
    driver.quit()

    return g

if __name__ == '__main__':
    import os
    import pickle
    # if os.path.isfile('/Users/mspear/graph'):
    #     with open('/Users/mspear/graph', 'rb') as f:
    #         g = pickle.load(f)
    # else:
    #     g = make_graph()
    #     with open('/Users/mspear/graph', 'wb') as f:
    #         pickle.dump(g, f)

    with open('/Users/mspear/graph2', 'wb') as f:
        g = make_graph()
        pickle.dump(g, f)
