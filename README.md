# DESIGNER HUB

Designer Hub is a website created as a social media app for Designers. Here designers can interact with each other, posts there designes, get in touch with each other. They can share their opinios and create events related to desiging issues. The API is the backend of the platfrm which gives  create, view, edit and delete posts, events, new profiles, getting notification, choosing category, follow/unfollow users. 

The live API can be found [here](https://designerhubbackend-ebd8c03488fb.herokuapp.com/)

# Agile Development

The project was created based on user stories . The user stories are given here:

* As a user I can create my own profile so that I can create my post, edit/delete it
* As a user I can create posts so that I can update my contents
* As a user I can create edit/delete my comments so that I can keep my opinion uptodate
* As a user I can like/unlike posts so that I can express my preference
* As a user I can follow/unfollow other users so that I keep in touch with the profiles I am interested in
* As a user I can search or post in different categories so that it is easier to sort out my choice
* As a user I can get notified so that I know my posts have new like, comment or I have a new follower
* As a user I can create/see events so that I can know what is happening


The detais about user stories can be found [here](https://github.com/users/farhatamannaislam/projects/6/views/1)

# Database Design

I have the following models:

* Post - My post model is customized which includes a catagory parameter. 
* Category - User can post into a specific category.
* Comments - User can comment on a post
* Like - User can like/unlike a post
* Follow - User can follow/unfollow each other.
* Notification - User gets notification if another user like, comments on their posts or follow them.
* Profiles - Created automatically with every user.

# Data model Diagram

I drew my data model schema using [DrawSQL](https://drawsql.app/)



