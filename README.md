# Introduction
## Purpose
The purpose of this Independent Project is to demonstrate your level of understanding of the various concepts that you have covered in the content throughout the week. The project will be graded by your peers and will determine if you are eligible to move on to the next module. All the requirements provided below should be met in a high quality manner.

# Additional Information
Before you start building the project, create an empty Github Repository and submit the link of the repository in the LMS. All Independent Projects must be submitted by 6pm.

# References
If you get stuck during the development of your project you can contact me on Github


# Project prompt
At Moringa school you create a lot of projects (IPs, Mid-week projects) but you never know how those projects rate with your peers. Your objective is to create an application like Awwards (Links to an external site.)Links to an external site. (It doesn't necessarily have to be exactly the same). The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

A project can be rated based on 3 different criteria

Design
Usability
Content
These criteria can be reviewed on a scale of 1-10 and the average score is taken.

# User stories
As a user, you can:

View posted projects and their details.
Post a project to be rated/reviewed
Rate/ review other users' projects
Search for projects 
View projects overall score
View my profile page.

3. System Features/Objectives
Feature A: Projects
Projects should have a Title, an image of the project's landing page, a detailed description of the project, a link to the live site.

Feature B: Profile
Your project should have a user profile that at least the following information:

Profile picture of the user.
User Bio
Projects the user has posted
A contact information of the user. 
Feature C: An Authentication System 
Your application should have a solid authentication system that allows users to sign up or log in to the application before posting or rating a project.

Feature D: Rating/ Review
Projects will be rated/reviewed based on the following criteria:

Design - This is the overall appearance of the project
Usability - This can be translated to the user experience and how responsive the project is.
Content - This includes the technologies used, the font used(is it uniform throughout the project) and grammar
These criteria will each be rated/review on a scale of 1-10 and the overall score will be their average.

Feature E: API Endpoints
You should create an API so that users can access data from your application. You can create two API endpoints:

Profile - This endpoint should return all the user profiles with information such as the username, bio, projects of the user and profile picture
Projects- This endpoint should return information pertaining to all the projects posted in your application.
Feature I: Deployment
Your project should be deployed to Heroku when you have finished with the set features. You should provide the link to your project in the description part of your project repository.


#Software quality attributes
Your code should be written following the Python pep 8 guidelines (Links to an external site.)Links to an external site.. Make sure you document major sections of your code using docstrings. Also, ensure you commit regularly and your commit messages are clear and well written.

# Getting Started.

These instructions will get you a copy of the project up and running on a local host.

Step 1: git clone
Step 2: Enter the Project root folder

cd gallery/
install virtual environment (venv) without pip

python3.6 -m venv --without-pip virtual
Step 3: Activate virtual environment

source virtual/bin/activate
install pip using curl

curl https://bootstrap.pypa.io/get-pip.py | python
run the application

python3.6 manage.py runserver

## Prerequisites

None, follow this link to get run the application.

## Deployment

Deploying the Django Apps to Heroku to view.

## Built With

Python3.6 - Python is a programming language that lets you work quickly and integrate systems more effectively
Django - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design
postgresql - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
Versioning
version 1.0.0

## Bugs

If you encounter any bugs, email me on melissamalala@gmail.com. If you would like to add some changes, please feel free to
fork the project and make a pull request.

## Authors

MELISSA MALALA

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Moringa School
