import requests
import json
import sys
import graphviz
import os
import timeit
import time
import copy


def print_graph(g):
    graph = graphviz.Graph(format='png', strict=True, filename='Mastodon_network')
    for n in g.keys():
        graph.node(n, n)

    for n in g.keys():
        for t in g[n]:
            graph.edge(n, t)
    graph.render()
    os.remove('Mastodon_network')

# define mode (fetch data/draw graph)
# 'fetch' or 'draw'
# main_user = ("65633", "dajbelshaw")
main_user = ("31622", "lpenou")
mode = "draw"

if mode == "fetch":
    # TODO: Fetching Followers
    # 2.1 With authentication fetching followers of a specified id:
    g = {}

    access_token = ""
    all_nodes = []
    followers = set()

    url = f"https://mastodon.social/api/v1/accounts/{main_user[0]}/followers?limit=80"
    while url:
        response = requests.get(url, headers={'Authorization':f'Bearer {access_token}'})
        objects = json.loads(response.text) # this converts the json to a python list of dictionary
        usernames = set([(i['id'],i['username']) for i in objects])
        followers |= usernames
        url = response.links['next']['url'] if 'next' in response.links else None


    all_nodes.extend(list(followers))
    all_ids = [i[0] for i in all_nodes]

    print(f"Iterating over {len(all_nodes)} users")
    for i, (id, username) in enumerate(all_nodes):
        url = f"https://mastodon.social/api/v1/accounts/{id}/followers?limit=80"
        followers = set()
        while url:
            response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})
            objects = json.loads(response.text)  # this converts the json to a python list of dictionary
            usernames = set([(i['id'], i['username']) for i in objects if i['id'] in all_ids])
            followers |= usernames
            url = response.links['next']['url'] if 'next' in response.links else None
            time.sleep(.5) # in order to avoid api call ban
        g[username] = [i[1] for i in followers]
        print(f"\t user {i}/{len(all_nodes)} - fetched {len(followers)} followers for user {username}({id})")

    print(g)

    # Make graph undirected
    for user, items in g.items():
        for follower in items:
            if user not in g[follower]:
                g[follower].append(user)

    with open('tests/ressources/graph_52n.json', 'w') as fp:
        json.dump(g, fp)

elif mode == "draw":
    # Create graphviz png
    with open('tests/ressources/graph_52n.json', 'r') as fr:
        data = dict(json.load(fr))
    print_graph(data)







