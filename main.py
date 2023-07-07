from mastodon import Mastodon
from bs4 import BeautifulSoup
from objects import User, Toot

mastodon = Mastodon(
    client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
    client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
    access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
    api_base_url="https://mastodon.social"
)

# Fetch user data
user_data = mastodon.account_verify_credentials()

######################################################################## Create User-Instance of own profile ################################################################
user = User(
    name=user_data['username'],
    id=user_data['id'],
    display_name=user_data['display_name'],
    followers_count=user_data['followers_count'],
    #signdate=None
)

# Print the stored data
print(f"Username: {user.get_name()}")
print(f"Display Name: {user.get_display_name()}")
print(f"Followers Count: {user.get_followers_count()}")
print("")


query = "Johny"
limit = 10

######################################################################## Get all followed Persons ################################################################
def get_followed(user_id):
    followedPersons = []
    followed = mastodon.account_following(id = user_id, limit=None)
    for account in followed:
        user = User(
            name=account['username'],
            id=account['id'],
            display_name=account['display_name'],
            followers_count=account['followers_count'],
            #signdate=None 
        )
        followedPersons.append(user)

    print("Follows: ")

    # Print the stored user data
    for user in followedPersons:
        print(f"Username: {user.get_name()}")
        print(f"Display Name: {user.get_display_name()}")
        print(f"Followers Count: {user.get_followers_count()}")
        print()


    print("End")
    print("")

######################################################################## Search Accounts by Name ################################################################
def search_account():
    results = mastodon.account_search(q=query, limit=limit)

    users = []
    for account in results:
        user = User(
            name=account['username'],
            id=account['id'],
            display_name=account['display_name'],
            followers_count=account['followers_count'],
            signdate=None
        )
        users.append(user)

    # Print the stored user data
    for user in users:
        print(f"Username: {user.get_name()}")
        print(f"Display Name: {user.get_display_name()}")
        print(f"Followers Count: {user.get_followers_count()}")
        print()
    
hashtag = "Moin" 

toots = mastodon.timeline_hashtag(hashtag, limit=limit)
toots_dict = []
# Process and print the retrieved toots
for toot in toots:
    content_html = toot['content']
    soup = BeautifulSoup(content_html, 'html.parser')
    content_text = soup.get_text()
    toot = Toot(
        account = toot['account'],
        toot_id = toot['id'],
        content = content_text,
        user_id = toot['account']['id'],
        hashtags = toot['tags'],
        bookmark = toot['bookmarked'],
        no_replies = toot['replies_count'],
        url = toot['url'],
        count_replies = toot['replies_count']    
    )
    toots_dict.append(toot)
    
toot_replies = []
    
for toot in toots_dict:
    print('Og-Toot: {}'.format(toot.content))
    for x in range(toot.count_replies):
        print('Reply-Toot: {}'.format(toot.get_replies(x)))
    # anzahl an antworten/ mehrer antworten printen
    
    