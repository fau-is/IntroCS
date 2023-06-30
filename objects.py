import mastodon

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
    
    # getter- & setter-Methods
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
    
    def set_dollower_count(self):
        count = user_data['followers_count']
        self.followers_count = count
    
    