import requests
import json
import sys
import graphviz
import os
import timeit
import time
import copy


def print_graph(g):
    graph = graphviz.Graph(format='png', strict=True, filename='network')
    for n in g.keys():
        graph.node(n, n)

    for n in g.keys():
        for t in g[n]:
            graph.edge(n, t)
    graph.render()
    os.remove('network')

# define mode (fetch data/draw graph)
mode = "draw"

if mode == "fetch":
    # TODO: Fetching Followers
    # 2.1 With authentication fetching followers of a specified id:
    g = {}

    access_token = ""
    main_user = ("65633", "dajbelshaw")
    all_nodes = [main_user]
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
    g[main_user[1]] = [i[1] for i in followers]

    print(f"Iterating over {len(all_nodes)-1} users")
    for i, (id, username) in enumerate(all_nodes[1:]):
        url = f"https://mastodon.social/api/v1/accounts/{id}/followers?limit=80"
        followers = set()
        while url:
            response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})
            objects = json.loads(response.text)  # this converts the json to a python list of dictionary
            usernames = set([(i['id'], i['username']) for i in objects if i['id'] in all_ids])
            followers |= usernames
            url = response.links['next']['url'] if 'next' in response.links else None
        g[username] = [i[1] for i in followers]
        print(f"\t user {i}/{len(all_nodes)-1} - fetched {len(followers)} followers for user {username}({id})")

    print(g)

    with open('graph_50n.json', 'w') as fp:
        json.dump(g, fp)

elif mode == "draw":
    # Create graphviz png
    with open('graph_50n.json', 'r') as fr:
        data = json.load(fr)
    data = dict(data)
    print_graph(data)







