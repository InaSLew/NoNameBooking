# 2018 December Assignment

## The Project
It's a booking website for a fictional restaurant called NoName

## Tech Stacks Used
- Django
- Bootstrap

## Current Functionalities (rough rundown)
- Able to `CREATE` a reservation
  - Date past today or beyond 4 weeks will be rejected and error messages are displayed
  - Successful booking will be redirected to the home page and a notification will be displayed

- A polling app to collect customers' opinions towards the restaurant

## To-be-implemented Functionalities
- User can `PATCH`/reschedule their reservation to another time/date
- User can `DELETE`/cancel reservation
- A confirmation email should be sent upon successful booking

## Things to be Fixed
- Everything is very cluttered and the code very unorganized.

## Run the project
1. `pip install -r requirements.txt`
2. `python manage.py migrate` (the default sqlite db is used)
3. `python manage.py runserver`