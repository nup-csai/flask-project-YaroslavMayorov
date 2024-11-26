###Routes

/ (GET) or /main (GET) - shows the main page with track form

/ (POST) or /main (POST) - processes data from the form and offers to register/login to save item

/register (GET) - shows the html page with the form for register new user

/register (POST) - processes data from the form and create new user

/login (GET) - shows the html page with the login form

/login (POST) - processes data from the form and compare it with data from database with existing users

/recover_password (GET) - shows the html page with the form for recovering password

/recover_password (POST) - processes data from the form, check if such user exists and send new password in email

/profile (GET) - shows the html page with menu: links to user profile, to tracked item, to bought items

/form (GET) - shows the html page with the form with information about user

/form (POST) - processes data from the form, change the data about user in database

/tracked (GET) - shows the html page with all tracked items

/tracked/<item_id> (GET) - shows the html page with more information about one current tracked item

/bought - shows the html page with all bought items


