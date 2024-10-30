This project uses the web framework fastAPI to get and add sheep to a database constructed in a python file.  
Along with conducting tests to ensure each method works as expected. 

A virtual environment needs to be started before attempting to run the API. You can do this for windows in the powershell:
  In the project directory enter the command:
     python -m venv venv
     exit

In the terminal of the project once open:
  Installment needed are:
    pip install fastapi uvicorn pytest httpx
  
  To run:
    uvicorn main:app --reload
  
  To view, enter this website:
    http://127.0.0.1:8000/docs
