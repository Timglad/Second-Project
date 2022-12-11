# Second-Project
Library Project with books, loans and users apps

# First Steps for installation 

 Install virtual enviroment : 
- python -m venv venv 
- ./venv/Scripts/activate

 Install requirements.txt : 
- pip install -r requirements.txt

# Create Super-User
- python manage.py createsuperuser
- Username : admin
- Email : admin@gmail.com
- Password : admin

# BOOKS APP

Models : 
- Authors : name, age, nationality
- BookType : ten_days, five-days, two_days
- LoanStatus : avaliable, loaned
- Book : name, author, year_published, type, image, status
- BookReview : book, custemer, content, stars, date_added

Functions : 
- mains - displays all books
- single_book - displays requested book
- CRUD functions for books and authors - Avaliable only to staff members
- search_books
- authors - displays all author
- single_author - displays requested author
- search_books  
- show_reviews - Shows reviews for requested book

Pages:
- Mains - Main page
- Single book page
- Add, Edit books and authors pages
- Authors page
- single author page


# LOANS APP

Models : 
- LoanStatus : avaliable, loaned
- Loan : custID, bookID, loandate, returndate, status
- LoanTime : OVERTIME, ONTIME 

Functions : 
- loans - Loans the book - Required login
- returns - Returns the book - Required login
- late_check - Changes loan status
- loan_private_list - All the loaned books of a user - Required login
- loan_list - Table of all the loaned books - Avaliable only to staff members
- late_loan - Table with oevrtime loans - Avaliable only to staff members

Pages:
- loans - The loan page
- tables - Displays a table of all the loans


# USERS APP

Models : 
- UserProfile : user, fullname, image, city, age

Functions : 
- login_func 
- register_request - Register function
- logout_func 
- single_user - displays users profile - Required login
- user_menu - Edit user - Required login
- first_login - Creates default user profile
- customer_list - All users list - Avaliable only to staff members
- deluser - Delete user - Avaliable only to staff members

Pages:
- entry_form - login page
- register_form page
- userprofile
- all_users
-add_profile




