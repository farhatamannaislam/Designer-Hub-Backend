# Automated Test

## PostListViewTests 

Any user can see all post lists. Logged in user can create posts. Users that aren't logged in can't create posts.

## PostDetailViewTests

A post can be retrieved using valid ID. A post can't be retrieved using invalid ID. Logged in user can update his own post. Logged in user can not update another 
user's post.


## NotificationModelTests

Checks if the user gets notification based on likes, comments and followers. It tests string representation of notification
that includes recipients username, notification type and creation time. Notifications are also tested based on their ordering. They are ordered by
created_at.

## EventListViewTests

Any user can see all event lists. Logged in user can create events. Users that aren't logged in can't create events.

## EventDetailViewTests

An event can be retrieved using valid ID. An event can't be retrieved using invalid ID. Logged in user can update his event post. Logged in user can not update another user's event.


# Manual Tests

## Comments App

Logged out users can see comment list without the option of adding a new comment.

![Comment view for logged out users](docs/readme/images/logoutcomment.png)

Logged in user can comment on a post.

![Logged in user can comment](docs/readme/images/logincratecomment.png)

User can not post an empty comment.

![User can not post an empty comment](docs/readme/images/emptycommentnotvalid.png)

Comments can be retrived by valid id. It can be done by both logged in and logged out user.

![Retrive comment by logged in user](docs/readme/images/retrievecommentloggedin.png)

![Retrive comment by logged out user](docs/readme/images/retrievecommentlogout.png)

If user is the owner of the comment he can edit or delete it by retrieving it. If user is not the owner of the comment he can not edit or delete it.

## Followers app

 Logged-out user can see a list of all followers and all instances of a user following another user. 

 ![View list of followers as logged out user](docs/readme/images/followersloggedout.png)

 Logged-in user can see a list of all followers and all instances of a user following another user as well as has the option to follow other user.

 ![View list of followers as logged in user](docs/readme/images/followersloggedin.png)

 If a logged-in user tries to follow the same user twice, the API should return an HTTP 400 Bad request error.

 ![Follow an user twice error](docs/readme/images/duplicatefollowerror.png)

 A logged-in user should also be able to delete a follower instance retrieving by the id from Follower List.

 ![Delete Follower](docs/readme/images/deletefollower.png)

 ## Like app

Logged out user can see the list of likes.

![View list of likes as logged out user](docs/readme/images/loggedoutlikes.png)

Logged-in user can see a list of likes and  has the option to like a post.

![View list of likes as logged in user](docs/readme/images/likesloggedin.png)

Likes can be retrieved by its Id. If author is the user he can delete this.

![Like retrieved by ID](docs/readme/images/likeretrievedbyId.png)

If a logged-in user tries to like the same post twice, the API should return an HTTP 400 Bad request error.

![Like a Post twice error](docs/readme/images/likingsameposttwiceerror.png)

## Profile App