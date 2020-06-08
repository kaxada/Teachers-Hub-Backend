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

### AUTHENTICATION

| REQUEST | ROUTE              | FUNCTIONALITY    |
| ------- | ------------------ | ---------------- |
| POST    | api/v1/auth/login  | Logs in a user   |
| POST    | api/v1/auth/signup | Registers a user |

### COURSES

| REQUEST | ROUTE                                                | FUNCTIONALITY                             |
| ------- | ---------------------------------------------------- | ----------------------------------------- |
| GET     | api/v1/courses                                       | Fetches all courses                       |
| GET     | api/v1/courses/&lt;course_id>                        | Fetches a single course                   |
| POST    | api/v1/courses                                       | Adds a new course                         |
| PUT     | api/v1/courses/&lt;course_id>                        | Updates a single course                   |
| DELETE  | api/v1/courses/&lt;course_id>                        | Deletes a course                          |
| POST    | api/v1/courses/&lt;course_id>/enroll                 | Enroll for a course                       |
| POST    | api/v1/courses/&lt;course_id>/modules                | Add module to course                      |
| GET     | api/v1/courses/&lt;course_id>/modules                | Fetch modules on a course                 |
| GET     | api/v1/courses/&lt;course_id>/modules/&lt;module_id> | Fetch module content for a single module  |
| POST    | api/v1/courses/&lt;course_id>/modules/&lt;module_id> | Create module content for a single module |

### USERS

| REQUEST | ROUTE               | FUNCTIONALITY            |
| ------- | ------------------- | ------------------------ |
| GET     | api/v1/auth/profile | Fetches a user's profile |

### ARTICLES

| REQUEST | ROUTE                           | FUNCTIONALITY        |
| ------- | ------------------------------- | -------------------- |
| GET     | api/v1/articles                 | Fetch all articles   |
| POST    | api/v1/articles                 | Add New Article      |
| DELETE  | api/v1/articles/&lt;article_id> | Delete an article    |
| PUT     | api/v1/articles/&lt;article_id> | Update an article    |
| GET     | api/v1/articles/&lt;article_id> | Fetch single article |

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

-   [Daisy Macharia](https://github.com/daisymacharia) - Mentor
-   [Maria Nanfuka](https://github.com/mariamiah) - TTL
-   [Akiyo Fidel](https://github.com/drfidel)
-   [Lubwama Benjamin](https://github.com/lubwamabenja)
-   [Kizza Samuel](https://github.com/skizza8)
-   [Ainembabazi Kirabo](https://github.com/AineKiraboMbabazi)
-   [Jimmy Were](https://github.com/jwere)
-   [Simon Peter Ojok](https://github.com/simonojok19)

## LICENSE

MIT
