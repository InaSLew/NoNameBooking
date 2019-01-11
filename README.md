# 2018 December Assignment

## The Project
It's a booking website for a fictional restaurant called NoName

## Tech Stacks Used
- Django
- Bootstrap

## Current Functionalities (rough rundown)
- Able to make a reservation
  - Date past today or beyond 4 weeks will be rejected and error messages are displayed
  - Successful booking will be redirected to the home page and a notification will be displayed
  - Inside the notification mentioned above, each user is given an unique BookingID (for rescheduling or cancelling)
- Able to cancel a reservation
  - User can cancel their reservation if a valid email and BookingID are provided
- Able to reschedule a reservation
  - User can reschedule their reservation if a valid email, BookingID, new date and time are provided.

- A polling app to collect customers' opinions towards the restaurant

## To-be-implemented Functionalities
- [x] User can `DELETE`/cancel reservation
- [x] User can `PATCH`/reschedule their reservation to another time/date
- [x] A confirmation message along with an unique BookingID should be given to user upon successful booking

## Things to be Fixed
- [ ] Everything is very cluttered and the code very unorganized.
- [ ] Pictures in the carousel get stretched/shrinked out of proportion on bigger/smaller screens.
- [ ] The beginning of the form is blocked by the navbar in mobile mode.

## Run the project
1. `pip install -r requirements.txt`
2. `python manage.py migrate` (the default sqlite db is used)
3. `python manage.py runserver`