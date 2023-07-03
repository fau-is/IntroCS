import requests
import json
import pandas as pd

# 1.1 Fetching public timelines max returns 40 toots (default 20):
# response = requests.get("https://mastodon.social/api/v1/timelines/public?limit=40")
# statuses = json.loads(response.text) # this converts the json to a python list of dictionary
# assert statuses[0]["visibility"] == "public" # we are reading a public timeline
# print(statuses[0]["content"]) # this prints the status text

# 1.2 Fetching toots by hashtags:
# hashtag = 'cat'
# response = requests.get(f"https://mastodon.social/api/v1/timelines/tag/{hashtag}?limit=2")
# statuses = json.loads(response.text) # this converts the json to a python list of dictionary
# assert statuses[0]["visibility"] == "public" # we are reading a public timeline
# print(statuses[0]["content"]) # this prints the status text

# 1.3 Fetching public accounts:
# id = "110238786829709082"
# response = requests.get(f"https://mastodon.social/api/v1/accounts/{id}")
# profile = json.loads(response.text) # this converts the json to a python list of dictionary
# print(profile['note']) # this prints the status text

# 1.4 Fetching statuses of public accounts
# id = "110238786829709082"
# response = requests.get(f"https://mastodon.social/api/v1/accounts/{id}/statuses")
# statuses = json.loads(response.text) # this converts the json to a python list of dictionary
# assert statuses[0]["visibility"] == "public" # we are reading a public timeline
# print(statuses[0]["content"]) # this prints the status text

# 1.5 Fetching public statuses by id
# id = '110597114103379242'
# response = requests.get(f"https://mastodon.social/api/v1/statuses/{id}")
# status = json.loads(response.text) # this converts the json to a python list of dictionary
# assert status["visibility"] == "public" # we are reading a public timeline
# print(status["content"]) # this prints the status text

# 1.5.1
# GET /api/v1/statuses/:id/reblogged_by to view who boosted that status,
# GET /api/v1/statuses/:id/favourited_by to view who favourited that status

# 1.6 Fetching statuses context (ancestors/descendants) by id
# id = '110597114103379242'
# response = requests.get(f"https://mastodon.social/api/v1/statuses/{id}/context")
# status = json.loads(response.text) # this converts the json to a python list of dictionary
# ancestors = status['ancestors']
# descendants = status['descendants']
# assert ancestors[0]["visibility"] == "public" # we are reading a public timeline
# print(ancestors[0]["content"]) # this prints the status text


# # following request require OAuth authentification
# 2.0 Verifying OAuth token is valid
# access_token = ""
# response = requests.get(f"https://mastodon.social/api/v1/apps/verify_credentials", headers={'Authorization':f'Bearer {access_token}'})
# verification = json.loads(response.text)
# if response.status_code == 200:
#     print("Verified")
# else:
#     print("Not Verified")


# 2.1 With authentication fetching followers of a specified id:
# access_token = ""
# id = "15530"
# response = requests.get(f"https://mastodon.social/api/v1/accounts/{id}/followers", headers={'Authorization':f'Bearer {access_token}'})
# followers = json.loads(response.text) # this converts the json to a python list of dictionary
# print(len(followers)) # this prints the number of followers
# if len(followers)>0:
#     print(followers[0]['id']) # this prints the id of follower #1

# 2.2 With authentication fetching followed users of a specified id:
# access_token = ""
# id = "15530"
# response = requests.get(f"https://mastodon.social/api/v1/accounts/{id}/following?limit=80", headers={'Authorization':f'Bearer {access_token}'})
# # Pagination - response object contains a "next"- or "prev"-link for the next or previous instances of following accounts (if there are more than 80 followers)
# following = json.loads(response.text) # this converts the json to a python list of dictionary
# print(len(following)) # this prints the number of followers
# if len(following)>0:
#     print(following[0]['id']) # this prints the id of follower #1

## TODO: Issue, we can only access followers or following from users of the same server, e.g. mastodon.social, where the app is registered
