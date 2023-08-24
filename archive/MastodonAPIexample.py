from mastodon import Mastodon

# https://mastodonpy.readthedocs.io/en/stable/index.html
# pip3 install Mastodon.py

# Create an instance of the Mastodon API
mastodon = Mastodon(
    client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
    client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
    access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
    api_base_url="https://mastodon.social"
)

# Fetch user data
user_data = mastodon.account_verify_credentials()

# Store user data in objects
username = user_data['username']
display_name = user_data['display_name']
followers_count = user_data['followers_count']
#insta = mastodon.instance()
# ?? followers = user_data.__api_request(GET /api/v1/accounts/:id/following) 

# Print the stored data
print(f"Username: {username}")
print(f"Display Name: {display_name}")
print(f"Followers Count: {followers_count}")
#print(f"{insta}")
