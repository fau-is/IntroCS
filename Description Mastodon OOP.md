# Mastodon OOP 
**Be sure to read this specification in its entirety before starting so you know what to do and how to do it!**

For this problem, you’ll implement a program that...

```
????
```

## Getting Started
Log into IntroCS - GitHub, click on your terminal window, and execute cd by itself. You should find that your terminal window’s prompt resembles the below:
```
  $
```
Create a new folder called 'pset7' with 
```
  mkdir pset7 
```
Direct to the newly created folder with:
```
  cd pset7
```

Next direct to the folder with 'cd pset7' and execute the following wget commands
```
  wget https://raw.githubusercontent.com/fau-is/IntroCS/Mastodon_OOP/MastodonOOP.py
```

```
  wget https://raw.githubusercontent.com/fau-is/IntroCS/Mastodon_OOP/test.py
```

Execute 'ls' by itself, and you should see a the following files:

```
  mastodon.py test.py
```
If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

**Don't change anything in ```test.py```.**

## API Access
An API access refers to the ability to interact with and make use of an Application Programming Interface (API). It is a set of rules and protocols that allows different software applications to communicate and interact with each other. It defines the methods and data formats that applications can use to request and exchange information.

APIs enable developers to access the functionality of a specific software, service, or platform, such as retrieving data, performing operations, or integrating with other systems. For example, social media platforms like Facebook, Twitter or Mastodon provide APIs that allow developers to access user data, post updates, or retrieve posts.

API access is typically provided through a combination of an API key or token and specific endpoints or URLs. The API key acts as a unique identifier that grants permission to access the API, while endpoints are URLs that specify the different actions or operations available through the API.
APIs are crucial for enabling the integration of various services and systems, allowing developers to build more powerful and complex applications by leveraging the functionality and data provided by other services.

### Mastodon API
[Mastodon](https://mastodon.social/explore) is a social networking platform that is part of the decentralized social media movement.

It was created by Eugen Rochko and launched in 2016 as an alternative to traditional, centralized social media platforms like Twitter. Mastodon is an open-source software, which means its source code is freely available for anyone to use, modify, and distribute.

Unlike traditional social media platforms, Mastodon operates on a federated model. Instead of having a single central server that hosts all user accounts and content, Mastodon instances are independently operated servers, known as "instances", which are connected to form a larger network. Each instance is its own community with its own rules and moderation policies, and users can choose which instance they want to join based on their interests or preferences.

Users on Mastodon can post messages, called "toots," which can include text, images, videos, and links. They can follow other users from their own instance or other instances, and interactions are possible across instances within the Mastodon network.

## Getting Started
### Problem 0: Get Access to the Mastodon API
1.	Create a Mastodon account at the 'Mastodon.social’ server.
2.	Generate an access token, that will allow your code to interact with the Mastodon API on your behalf.
    - Log-in into your account 
    - Go to your account settings
    - Look for “Development” or “API” in settings
    - Create a new application by providing a name, website and a brief description

3.	Use the API Library Mastodon.py to make calls from your application to the API.
4.	Authenticate your application using “Client ID”, “Client Secret” and “Access token”, as well as the server (“api_base_url”) your profile is hosted at.
5.	If you need help throughout the whole problem Set, the [documentation of Mastodon.py](mastodonpy.readthedocs.io) is your way to go. 

### Problem 1: Implement a Toot Object
#### Toot-Object
A toot in Mastodon is like a tweet on Twitter. In this problem set you are going to filter those toots, to which you got access to using the API. 
We want to store any information about an object that we can then pass around in the rest of our program. 

Your task, in this problem, is to write a class 'toot', starting with a constructor that takes (content, account, user_id, hashtags, bookmark, no_replies, url, toot_id, count_replies, pubdate, mentions, media, language, poll) as arguments and stores them appropriately. 
<details>
<summary>Hint</summary>
<br>
  Recall how to use the init method to create your constructor.
</details>


### Problem 2: Isolate the text from html
#### Get_text_content
Your task is it to implement a function called get_text_content() which takes a toot (dictionary) as its input. The dictionary contains a key called 'content', which holds an HTML content string. Write a solution that extracts the plain text content from the HTML and returns it.
<details>
<summary>Hint</summary>
<br>
  You can use the [Beautiful Soup library](https://beautiful-soup-4.readthedocs.io/en/latest/).
</details>


### Problem 3: Download the toots from mastodon
#### Load-Function
The Mastodon.py documentation includes a function, “timeline_hashtag” that takes a hashtag, and returns a JSON-like dictionary with various information about all toots which have that particular hashtag. This information should be stored in the object “toot” described above. Limit this function to 100 toots that get loaded.

It is your turn now to write a function called “load” which takes as input a hashtag. At first you need to initialize an empty list where you will store your toots in the later process. Then you access the Mastodon API to get all toots based on a hashtag you set (recall to limit this, as otherwise you potentially load a lot of toots). Now use this toots to store them as a toot object instance and load it into your toot list. At the end you should return your filled toot list.

When writing this function, make sure to save the toot context as a string and not as html script. To do so you can use the ”get_text_content()” function. We already implemented this function in the file “content_Processor_ps7.py”, so you don’t have to worry about that.

## Triggers
Triggers are rules that determine whether or not a social network post on Mastodon meets the triggers criteria. They can be based on the content of the posts, such as specific phrases or media types, or on the time when the posts were published. Triggers can be used individually or combined using composite triggers to create more sophisticated filtering rules. 

It is your task to create these filters which are using the posts (e.g. Toots) you are loading in the Load-Function. After creating all trigger classes you then need to write a function that goes through a sample of triggers and posts and checks whether or not a specific post meets all given trigger criteria.

#### Trigger-Parent
This is an abstract class representing the parent class for all triggers. It contains the evaluate method, which is used to evaluate whether an alert should be generated for a given social network post on Mastodon. All trigger classes inherit from this class. Because -as you know- if an inheriting subclass does not overwrite the methods of the super class, it uses the super class method instead of an own. Therefore you need to overwrite the evaluate method in the subclasses as otherwise the evaluate method from the super class (Trigger) will get called and return a NotImplementedError.

### Problem 4-8: Implement a Media Trigger and Subclasses of it
#### Media-Trigger
- The MediaTrigger is a trigger that fires when a toot contains any media attachments such as images, videos, gifs, or audio files.
- To implement this trigger, you need to access the media attribute of the toot object, which represents the media attachments.
- Check if the media attribute is not empty. If it's not empty, return True, indicating that the trigger should fire. Otherwise, return False.

#### Image-Trigger
- The Image-Trigger is a trigger that fires when a social network post contains one or more image attachments.
- To implement this trigger, you need to access the media attribute of the post object, which represents the media attachments.
- Check if the media attribute is not empty and contains at least one image attachment. If it does, return True, indicating that the trigger should fire. Otherwise, return False.

#### GIF-Trigger
- The GIF-Trigger is a trigger that fires when a social network post contains one or more GIF (Graphics Interchange Format) attachments.
- To implement this trigger, you need to access the media attribute of the post object, which represents the media attachments.
- Check if the media attribute is not empty and contains at least one GIF attachment. If it does, return True, indicating that the trigger should fire. Otherwise, return False.

#### Video-Trigger
- The Video-Trigger is a trigger that fires when a social network post contains one or more video attachments.
- To implement this trigger, you need to access the media attribute of the post object, which represents the media attachments.
- Check if the media attribute is not empty and contains at least one video attachment. If it does, return True, indicating that the trigger should fire. Otherwise, return False.

#### Audio-Trigger
- The Audio-Trigger is a trigger that fires when a social network post contains one or more audio attachments.
-	To implement this trigger, you need to access the media attribute of the post object, which represents the media attachments.
- Check if the media attribute is not empty and contains at least one audio attachment. If it does, return True, indicating that the trigger should fire. Otherwise, return False.
<details>
<summary>Hint</summary>
<br>
  For this task it is very helpful to check the mastodon documentation about the returning dictionaries, especially media dicts.
</details>

### Problem 9: Implement a Language Trigger
#### Language-Trigger
- The LanguageTrigger is a trigger that fires when a toot is written in a specific language.
- For this task it is important to check the specific notation Mastodon uses for the languages. In the documentation there is more information about what language codes they use and a (very short) explanation on how it looks like.
- To implement this trigger, you need to pass the desired language as an argument when creating an instance of LanguageTrigger to save the passed in argument as an attribute of the LanguageTrigger.
- In the evaluate method, access the language attribute of a toot object to check if it matches the specified language, e.g., the attribute of the trigger.
- If the language matches the specified language, return True, indicating that the trigger should fire. Otherwise, return False.

### Problem 10: Implement a Poll Trigger
#### Poll-Trigger
- The PollTrigger is a trigger that fires when a toot contains a poll, quite similar to the media trigger.
- To implement this trigger, you need to access the poll attribute of the toot object, which represents the poll details.
- Check if the poll attribute is not empty. If it's not empty, return True, indicating that the trigger should fire. Otherwise, return False.

### Problem 11: Implement a Mentions Trigger
#### Mentions-Trigger
- The MentionsTrigger is a trigger that fires when a toot mentions other users, again quite similar to the poll and the media trigger.
- To implement this trigger, you need to access the mentions attribute of the toot object, which represents the mentioned users.
- Check if the mentions attribute is not empty. If it's not empty, return True, indicating that the trigger should fire. Otherwise, return False.

### Problem 12: Implement a Trigger to check if a specific Phrase is in the Toots Text
#### Phrase-Trigger
- The PhraseTrigger is a trigger that fires when a toot contains a specific phrase in its content.
- To implement this trigger, you need to pass the desired phrase as an argument when creating an instance of PhraseTrigger.
- In the evaluate method, access the content attribute of the toot object to get the text content of the toot.
- Convert both the content and the specified phrase to lowercase (to make the comparison case-insensitive).
- After that replace all string punctuation of the content with an empty string, e.g., delete all punctuations.
- Check if the phrase is present in the content. If it is, return True, indicating that the trigger should fire. Otherwise, return False.

### Problem 13-15: Implement a Time Trigger and Subclasses for Before and After Triggers
#### Time-Trigger
- The TimeTrigger is a trigger that fires based on the publication time of a toot.
- To implement this trigger, you need to pass the trigger time as a string in the format of "YYYY-MM-DD HH:MM:SS" (in EST timezone) when creating an instance of TimeTrigger.
- Convert the trigger time from a string to a datetime object and store it as an attribute (ptime) of the TimeTrigger.
- Note that TimeTrigger should be an abstract class, and you won't directly instantiate it.
- Therefore no evaluate method needs to be constructed.

#### Before-Trigger
- The BeforeTrigger is a trigger that fires when a post was published strictly before the trigger time.
- Implement BeforeTrigger as a subclass of TimeTrigger.
- Recall that being a subclass means it inherits all methods of the super class. Therefore the __init__ function of TimeTrigger will also be inherited and you do not need to construct a new one.
- In the evaluate method, access the pubdate attribute of the post object to get the publication time of the post.
- Convert the publication time to the EST timezone and compare it with the trigger time (ptime). If the post was published before the trigger time, return True, indicating that the trigger should fire. Otherwise, return False.

#### After-Trigger
- The AfterTrigger is a trigger that fires when a post was published strictly after the trigger time.
- Implement AfterTrigger as a subclass of TimeTrigger.
- As this trigger is quite the same to the BeforeTrigger, recall what you took into consideration then.
- In the evaluate method, access the pubdate attribute of the post object to get the publication time of the post.
- Convert the publication time to the EST timezone and compare it with the trigger time (ptime). If the post was published after the trigger time, return True, indicating that the trigger should fire. Otherwise, return False.



### Problem 16-18: Implement Compositions to combine different Triggers together
### Composite Triggers
#### And-Trigger
- The AndTrigger is a trigger that fires on a toot only if both inputted triggers fire on that toot.
- To implement this trigger, you need to pass two triggers as arguments when creating an instance of AndTrigger.
- In the evaluate method, evaluate both triggers for the toot and return True only if both triggers return True.

#### Or-Trigger
- The OrTrigger is a trigger that fires on a toot if either one (or both) of the inputted triggers fires on that toot.
- To implement this trigger, you need to pass two triggers as arguments when creating an instance of OrTrigger.
- In the evaluate method, evaluate both triggers for the toot and return True if at least one trigger returns True.
#### Not-Trigger
- The NotTrigger is a trigger that inverts the output of another trigger.
- To implement this trigger, you need to pass another trigger as an argument when creating an instance of NotTrigger.
- In the evaluate method, evaluate the passed in trigger for the toot and return the inverse of the result.

### Problem 19: Implement a Function which checks for Triggers in a List of Toots
#### Filter-Toots
This function could also be referred to as the evaluation function. All the triggers you implemented, and the loading of toots come together in this function. This function returns all the toots which meet the criteria of the filters you have specified before.
- The filter_toots function takes a list of toots (posts) and a list of triggers as input.
- It returns a list of only the toots for which all trigger in the trigger list fire.
- Iterate over each toot in the toots list and then iterate over each trigger in the trigger list.
- Evaluate each trigger for the toot using the triggers evaluate method. If all triggers return True for the toot, add the toot to the triggered_toots list.
- Finally, return the triggered_toots list containing only the toots that satisfy all the specified triggers.

### Problem 19:  
#### How to make everything work:
After you managed to implement all triggers and functions of the problem set you can start filtering toots. To do so start by loading toots. Then go on and specify all your wanted triggers and trigger compositions. Make sure that your trigger arrangement is logically structured, and triggers don’t “block” each other, e.g., AND-Trigger (Before-Triger: 01.01.2024, After-Triger: 01.01.2024). 

Now make a list of all the triggers you want to check for. With this trigger list and the list of toots you can now call your filter_toots function. At the end you can decide what you want to do with your now filtered toots. Either you can create your own function to go through all of your toots contents or you can use our premade load_to_workbook function to store them in a Excel-Sheet. 

## Testing
Execute the below to evaluate the correctness of your code using check50. But be sure to compile and test it yourself as well! 
```
check50 fau-is/IntroCS/Mastodon_OOP/MastodonOOP
```

<details>
<summary>Hint</summary>
<br>
  You can always go to the tutorium with your questions or contact online support of Intro CS via Teams, if you feel like additional help would be great.
</details>

## submit50
To submit your program use this line of code.
```
submit50 fau-is/IntroCS/Mastodon_OOP/MastodonOOP
```

