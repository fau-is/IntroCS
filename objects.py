from mastodon import Mastodon
from bs4 import BeautifulSoup

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
    def __init__(self, name, id, display_name, followers_count): #signdate):
        self.name = name
        self.id = id
        self.display_name = display_name
        self.followers_count = followers_count
        #self.signdate = signdate
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

    #def get_signdate(self):
        #return self.signdate
        

class Toot:
    def __init__(self, content, account, user_id, hashtags, bookmark, no_replies, url, toot_id, count_replies, pubdate):
        self.content = content
        self.account = account
        self.user_id = user_id
        self.hashtag = hashtags
        self.bookmark = bookmark
        self.no_replies = no_replies
        self.url = url
        self.toot_id = toot_id
        self.count_replies = count_replies
        self.pubdate = pubdate
        
    def get_replies(self, x):
        toot_id = self.toot_id
        count_replies = self.count_replies
        # toot_id = "5" 
        # Specify the ID of the toot you want to retrieve replies for 
        context = mastodon.status_context(toot_id) 
        replies = context['descendants'] 
        all_replies = []
        for reply in replies: 
            content_text = get_text_content(reply)
            antwort = Reply(
                account = reply['account'],
                toot_id = reply['id'],
                from_id = reply['in_reply_to_id'],
                content = content_text,
                user_id = reply['account']['id'],
                hashtags = reply['tags'],
                bookmark = reply['bookmarked'],
                no_replies = reply['replies_count'],
                url = reply['url'],
                count_replies = reply['replies_count']               
            )
            all_replies.append(antwort)
        if x <= count_replies:
            return all_replies[x].content 
        return 0

       
       
class Reply(Toot):
    def __init__(self, content, account, user_id, hashtags, bookmark, no_replies, url, toot_id, count_replies, from_id, pubdate):
        super().__init__(content, account, user_id, hashtags, bookmark, no_replies, url, toot_id, count_replies, pubdate)
        self.from_id = from_id
        
    def get_mother_toot(self):
        mother_toot = self.from_id
        mother = mastodon.status_context(mother_toot) 
        content_text = get_text_content(mother)
        mother1 = Toot(
            account = mother['account'],
            toot_id = mother['id'],
            content = content_text,
            user_id = mother['account']['id'],
            hashtags = mother['tags'],
            bookmark = mother['bookmarked'],
            no_replies = mother['replies_count'],
            url = mother['url'],
            pubdate = mother['created_at'])
        return mother1
        # wenn toot mit der id, dann mach nichts, ansonsten erstelle toot
        
        
def get_text_content(toot):
    content_html = toot['content']
    soup = BeautifulSoup(content_html, 'html.parser')
    content_text = soup.get_text()
    return content_text
    
    