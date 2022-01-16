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

5. Django Admin Panel for CRUD operations of all the relevant fields, implemented
above

## Constraint:

- Database must be postgres/Mysql.

- The backend must be designed in DjangoRestFramework.

## .env File Format:

```
SECRET_KEY = ' '
DATABASE = ' '
HOST = ' '
PORT =  
USER = ' '
PASSWORD = ' '
```

## Documentation::


Postman-generated documentation for backend can be found [here](https://documenter.getpostman.com/view/17779018/UVXjLbeq).

