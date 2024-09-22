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

Profile list can be viewed by both logged in and logged out users.

![Profiles logged in view](docs/readme/images/profilesloggedin.png)

![Profiles logged out view](docs/readme/images/profilesloggedout.png)

If user is the owner he can edit his profile by retrieving the profile by ID.

![Retrieve Profile by ID](docs/readme/images/retrieveprofilebyId.png)

An invalid ID will show 404 error message.

![Invalid Profile ID](docs/readme/images/InvalidIdprofile.png)

## Category App

Logged in user can make a post with selecting the catagory.

![Select Category](docs/readme/images/selectcategory.png)

## Notifications App

Logged in user can see his notifications.

![Logged in Notification View](docs/readme/images/loggedinNotificationview.png)

Logged out user can not see any notification.

![Logged out Notification View](docs/readme/images/loggedoutnotificationview.png)

## Events App

Logged out users can see event list without the option of adding a new event.

![Event view for logged out users](docs/readme/images/loggedouteventview.png)

Logged-in user can see a list of events and  has the option to create an event.

![Event view for logged in users](docs/readme/images/loggedineventview.png)


Event can be retrieved by its ID and if the user is the author he can edit or delete it.

![Retrieve Event by ID](docs/readme/images/eventretrievedbyID.png)

But if user is not the author he can not edit or delete it.

![Retrieve Event by not the owner](docs/readme/images/eventtretrievedbynotowner.png)

If user try to retrieve an event by wrong ID it will show HTTP 404 Not Found error.

![Retrieve Event by wrong ID error](docs/readme/images/wrongIdeventerror.png)

If user tries to create an event without title, date and tag it will show error.

![Event error without mandatory fields](docs/readme/images/eventerrorwithoutmandatoryfields.png)


## Post App

Logged out users can see post list without the option of adding a new event.

![Post view for logged out users](docs/readme/images/loggedoutpostview.png)

Logged-in user can see a list of posts and  has the option to create a post.

![Post view for logged in users](docs/readme/images/loggedinpostview.png)

Post can be retrieved by its ID and if the user is the author he can edit or delete it.

![Retrieve Post by ID](docs/readme/images/retrievepostbyID.png)

But if user is not the author he can not edit or delete it.

![Retrieve Post by not the owner](docs/readme/images/retrievepostbynotauthor.png)

If user try to retrieve a post by wrong ID it will show HTTP 404 Not Found error.

![Retrieve Post by wrong ID error](docs/readme/images/wrongIdPosterror.png)

If user tries to create a post without title it will show HTTP 400 Bad Request error.

![Create Post without title error](docs/readme/images/postwithouttitleerror.png)