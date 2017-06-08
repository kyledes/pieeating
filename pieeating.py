from bs4 import BeautifulSoup
import requests
import re
from Ability import Ability

proxies = {'http':'http://192.168.1.19:80'}

#page = requests.get("http://magic.wizards.com/en/articles/archive/making-magic/mechanical-color-pie-2017-2017-06-05", proxies=proxies)


def with_ul_child(tag):
    return tag.find('ul')


def parse_complex_group(node_group):
    metaAbility = node_group.pop(0)
    processed_abilities = []
    for i in range(0, len(node_group), 3):
        processed_abilities.append(Ability(node_group[i], node_group[i+1], node_group[i+2]))




def parse_abilities(node_group):
    print('Node Group: {}'.format(len(node_group)))
    if len(node_group) == 3:
        return Ability(node_group[0], node_group[1], node_group[2])
    else:
        return parse_complex_group(node_group)

with open('maro','r') as page:
    soup = BeautifulSoup(page.read(), 'html.parser')

    wrappers = soup.find_all('div', class_='collapsibleBlock')

    print(len(wrappers))

    abclist = []

    re = re.compile('[A-Z]–[A-Z]')
    # print(wrappers[0])
    for wrap in wrappers:
        print(wrap.dl.dt.h2)
        if wrap.dl.dt.h2 is not None and re.match(wrap.dl.dt.h2.get_text()):
            abclist.append(wrap)
        else:
            print('ul check')
            pass

    print('abclist: {}'.format(len(abclist)))

    abilities = []

    for wrap in abclist:
        if wrap.div.div is not None:
            p_children = wrap.div.div.findChildren(recursive=False)
        else:
            p_children = wrap.div.findChildren(recursive=False)

        # print("mod 3: {}".format(len(p_children) % 3))
        # for i in range(0, len(p_children), 3):
        #     try:
        #         ability = Ability(p_children[i], p_children[i + 1], p_children[i + 2])
        #         abilities.append(ability)
        #     except Exception as e:
        #         print('except' + str(i))
        #         print(e)
        next_node = p_children[0]
        node_group = []
        node_group.append(next_node)
        while True:
            next_node = next_node.nextSibling
            if next_node is None:
                break
            elif next_node == "\n":
                pass
            elif next_node.name != 'hr':
                node_group.append(next_node)
            elif next_node.name == 'hr':
                abilities.append(parse_abilities(list(node_group)))
                node_group = []




    print(len(abilities))