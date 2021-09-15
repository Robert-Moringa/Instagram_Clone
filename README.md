# Instagram_clone

This Instagram_clone web-app was created as a clone of instagram.Developed during Moringa Core. 
Date: 10th September 2021
By: Robert Maina

## Description
This web-app allows a user to create a Profile, add Post and allow users add comment that are all under his username allowing other users to vote for them.

## Setup/Installation Requirements
* Live site can be accessed from the following link 
* Pre-configured Admin details are:
Password: 12345
Username: Robert

### Known Bugs
* The comments repeat themselves on each post

### Behaviour Driven Development
* The program should return all users posts on the home page<br>
Given:All posts<br>
When: Url is changed to home page<br>
Then: All Posts are displayed<br>

* Adding a comment<br>
Given:A Post<br>
When: User cicks on the comment icon <br>
Then: A modal with the post's comments is displayed<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>

* User session should end when logout url is chosen<br>
Given:Logout option is given<br>
When: User chooses logout option<br>
Then: User session is ended<br>


### Technologies Used
* Visual Studio was the source code editor.
* Git and Github were used as my local and online repositories respectively.
* Django was used as the framework.
* Heroku was used in deploying the live site.
* Postgresql


### Support and contact details
* Contact me through my email: robertmaina.student@moringaschool.com
* The source code is also contained within the folder containing this README with comments on the code thus third-party support can be offered.

### License
Moringa School
Copyright (c)2021 **Instagram clone by Robert Maina**