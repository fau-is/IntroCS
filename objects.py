from mastodon import Mastodon

mastodon = Mastodon(
    client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
    client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
    access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
    api_base_url="https://mastodon.social"
)


class User:
    # list of all 'loaded' users
    users = []
    
    # Constructor
    def __init__(self, name, id, display_name, followers_count, signdate):
        self.name = name
        self.id = id
        self.display_name = display_name
        self.followers_count = followers_count
        self.signdate = signdate
        User.users.append(id)
    
    # getter-Methods
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
       
    def get_display_name(self):
        return self.display_name
       
    def get_followers_count(self):
        return self.followers_count
    
    def get_signdate(self):
        return self.signdate
    
      
class Toot:
    def __init__(self, content, account, user_id, hashtags, bookmark, no_replies, url, toot_id):
        self.content = content
        self.account = account
        self.user_id = user_id
        self.hashtag = hashtags
        self.bookmark = bookmark
        self.no_replies = no_replies
        self.url = url
        self.toot_id = toot_id
        
    def get_replies(self):
        toot_id = self.toot_id
        # toot_id = "5" 
        # Specify the ID of the toot you want to retrieve replies for 
        context = mastodon.status_context(toot_id) 
        replies = context['descendants'] 
        return replies
        
       
       
class Reply(Toot):
    def __init__(self, content, account, user_id, hashtags, bookmark, no_replies, url, reply_id, toot_id):
        super().__init__(content, account, user_id, hashtags, bookmark, no_replies, url, toot_id)
        self.reply_id = reply_id
        
    def safe_mother_toot(self):
        return 1
        # wenn toot mit der id, dann mach nichts, ansonsten erstelle toot