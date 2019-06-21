# firstDjangoProject
My first django demo

This app is related to - company and employee details.

You have to first run this project using : 
    python manage.py runserver
    
    
Now you can able to access APIs. So there are 2 API endpoint:

1. If you pass employee id in URL then it gives name of that particular employee.

    http://127.0.0.1:8000/firstApp/<emp_id>/
    where <emp_id> is employee id
    
2. If you pass company id in URL then it gives JOSN response about details of all employees of that particular company

    http://127.0.0.1:8000/firstApp/<company_id>/employees
    where <company_id> is company id
    
 
