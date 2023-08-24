from mastodon import Mastodon
from objects import User, Toot, get_text_content

mastodon = Mastodon(
    client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
    client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
    access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
    api_base_url="https://mastodon.social"
)

# Fetch user data
user_data = mastodon.account_verify_credentials()
toots_dict = []
def load(hashtag):
    # load all toots with a specififc hashtag into a dictionary 
    hashtag = hashtag 
    toots = mastodon.timeline_hashtag(hashtag, limit=100)
    # Process and print the retrieved toots
    for toot in toots:
        content_text = get_text_content(toot)
        toot = Toot(
            account = toot['account'],
            toot_id = toot['id'],
            content = content_text,
            user_id = toot['account']['id'],
            hashtags = toot['tags'],
            bookmark = toot['bookmarked'],
            no_replies = toot['replies_count'],
            url = toot['url'],
            count_replies = toot['replies_count'],
            pubdate = toot['created_at']   
        )
        toots_dict.append(toot)
        
load("ChatGPT")

for toot in toots_dict:
    print('Date ({})'.format(toot.pubdate))