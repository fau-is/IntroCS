# Week 1: Object-Oriented Programming with Mastodon API
## Objective
To familiarize students with the Mastodon API and the principles of object-oriented programming (OOP).
Students will access the API data and store users, posts, retweets, and favourites as objects.
## Tasks
1. Learning about the Mastodon API: Students will receive general instructions about OOP as well as APIs and the basics of Mastodon to understand how to interact with it.
2. Accessing Data via the API: Students will write Python code (or a language of your choice that supports OOP) to access data from the Mastodon API.
3. Creating Objects: Students will create classes for Users, Posts, Retweets, and favourites. Instances of these classes will be created using data obtained from the Mastodon API.
4. Problem-Solving Exercises: Students will work in groups to complete a problem set designed to enhance their understanding and usage of OOP concepts, including inheritance, polymorphism, and encapsulation.
5. Data Storage: Students will create methods for storing and retrieving these objects, simulating a simple database.

## API Access
### Obtaining Access to the API
1.	Register an application at the instance we want to interact with (e.g. an own website). This can be done via an API endpoint (POST /api/v1/apps). This will give us a client_id and client_secret.
2.	Obtain an access_token for the user you want to act as. This is done by directing the user to a specific URL where they can approve your app, and then they'll be redirected back to your app with an access_token in the URL.
3.	Use the access_token to make API requests on behalf of the user. This can be done by including an Authorization header with the HTTP request.
### Useful API requests
#### Timelines: 
```bash
GET /api/v1/timelines/public
``` 
allows you to retrieve public posts. 
#### Accounts: 
```bash
GET /api/v1/accounts/:id 
```
retrieves information about a given user's account, based on the account id.
#### Followers and Following: 
```bash
GET /api/v1/accounts/:id/following
```
and 
```bash
GET /api/v1/accounts/:id/followers
```
retrieves who an account is following and who is following them. This could be used for social network analysis or studying the propagation of information.
#### Statuses: 
```bash
POST /api/v1/statuses
```
allows you to post a new status (or "toot"). This could be used for unit tests (requires authentication)
#### Search: 
```bash
GET /api/v1/search
 ```
allows you to search for content. This could be used for teaching regular expressions.
