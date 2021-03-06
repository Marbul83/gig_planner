# gig_planner


Gig Planner web application

Brief

The objective of this project is to create a web application in python that has functionality 
to create, read update and delete information.

Project

I have decided to create an application that will be a Gig Planner. The user will be able to create 
a plan of upcoming gigs by adding a venue and a band

Project Tracking

I have kept track of the projects development using a trello board. 

initially I created user stories of what I would like the app to do for the user. 
From this, I created checklists inside of those user stories for how to implement each of those features. 
I then converted each of these items into cards so that the project backlog and progress of each sprint could be monitored.

The project was divided into sprints, to split up the tasks that needed to be completed in an ordered manner.

This also allowed for me to have a working application along the way.

The last sprint was to complete testing on the working application.


In order to store the data for the Gig Planner, I created an ERD diagram, showing my tables: a Venues table and a Bands table.
As they have a many to many relationship, I also had to create a table called Gigs, that took the Primary Keys from both tables.

I created the tables in mySQL and ran the databse via Google Cloud.

I created a VM through Google Cloud and a requirements.txt file that contained a list of all the essential installations needed to run the app.


Risk Assesment

I have completed the risk assessment on a separate document, in a reader friendly format. This is available in the repository, under risk assessment.


CI pipeline

The CI pipeline is available as a user friendly diagram in the repository.
