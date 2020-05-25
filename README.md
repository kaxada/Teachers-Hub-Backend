# Teachers Hub Backend

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8f00e10e684b43ac812feba82c89b2da)](https://app.codacy.com/gh/BuildForSDG/Team-273-Backend?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDG/Team-273-Backend&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/BuildForSDG/Teachers-Hub-Backend.svg?branch=develop)](https://travis-ci.org/BuildForSDG/Teachers-Hub-Backend)
[![Coverage Status](https://coveralls.io/repos/github/BuildForSDG/Teachers-Hub-Backend/badge.svg)](https://coveralls.io/github/BuildForSDG/Teachers-Hub-Backend)

## About

The purpose of this project is to provide inclusive, equitable and quality education for all people, globally. Its targets to span a variety of challenges related to inclusion of marginalized populations at multiple levels of education and in the workforce.

This project addresses the following SDG targets:

-   Increased supply of qualified teachers in the community
-   Increased networking among teachers
-   Training of teachers by more qualified bodies
-   Accessibility to employment opportunities

## Usage

| REQUEST | ROUTE                         | FUNCTIONALITY             |
| ------- | ----------------------------- | ------------------------- |
| GET     | api/v1/courses                | Fetches all courses       |
| GET     | api/v1/courses/&lt;course_id> | Fetches a single course   |
| POST    | api/v1/courses                | Adds a new course         |
| PUT     | api/v1/courses/&lt;course_id> | Updates a single course   |
| DELETE  | api/v1/courses/&lt;course_id> | Deletes a course          |
| POST    | api/v1/auth/login             | Logs in a user            |
| POST    | api/v1/auth/signup            | Registers a user          |
| POST    | api/v1/auth/logout            | Logs out a user           |
| POST    | api/v1/categories             | Creates a course category |

## Setup

1.  You should have **Python 3.5+** and **git** installed. 
2.  Inorder to get started, clone this repository using `git clone https://github.com/BuildForSDG/Teachers-Hub-Backend.git`
3.  Change in the repository directory `cd teachers-hub-backend`
4.  Set up a virtual environment by running `python3 -m venv <name_of_the_environment>`
5.  Install requirements by running `pip install -r requirements.txt`
6.  Start the flask server by running `python run.py`
7.  Navigate to `http://localhost:8000` in the browser to view the api.
8.  Alternatively, open [postman](https://www.postman.com/) to test the url endpoints

## Heroku deployment

View the deployed application here [Teachers Hub API](https://teachershub-backend.herokuapp.com/)

## Authors

List the team behind this project. Their names linked to their Github, LinkedIn, or Twitter accounts should siffice. Ok to signify the role they play in the project, including the TTL and mentor

## LICENSE

MIT
