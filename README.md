#  Backend for a CRM System

## Business Logic:

1. The CRM account is associated with each employee/student-counsellor of the company with
their email id & password.

2. There is an enquiry form which is provided to every prospective client to fill their basic details
i.e. Name, Email, Course interest etc. This form can be circulated online to capture leads or
can be shared by the counsellor itself after it has connected with the student via call.

3. Inside the CRM, each employee/counsellor can see all the enquiries that prospective clients
have filled. We can say these are Public Enquiries that are visible to all the
employee/counsellor.

4. Against each public enquiry, the employee/counsellor has a choice to “Claim” it. Claiming it
will assign the enquiry to only this counsellor inside the CRM & this enquiry will no longer be
publically visible to any other employee. We can say that this is now a private enquiry.

<!-- 5. Django Admin Panel for CRUD operations of all the relevant fields, implemented
above -->

## Constraint:

- Database must be PostgreSQL/MySQL.

- The backend must be designed in DjangoRestFramework.

## Steps for Development:

1. First create a blank database as per requirements.
2. Create the .env file as per format given below.
3. Fill values of .env file as per constraints of system.
4. Run: ``` python manage.py makemigrations ```
5. Run: ``` python manage.py migrate ```
6. Run: ``` python manage.py createsuperuser```
    
    - Add superuser credentials as required.
7. Run: ``` python manage.py runserver```

## .env File Format:

```
SECRET_KEY = ' '
DATABASE = ' '
HOST = ' '
PORT =  
USER = ' '
PASSWORD = ' '
```

## Applications:

1. [FormAapp/](https://github.com/Arkiralor/crmproject/tree/master/formapp)

## Documentation:


Postman-generated documentation for backend can be found [here](https://documenter.getpostman.com/view/17779018/UVXjLbeq).

