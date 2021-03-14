# Office management system  
User panel API's and service.  

## Gettings started  
Clone project:
```
git clone git@github.com:usefss/office-management.git
cd office-management
```  
Create and activate a python virtual environment:
```
python3 -m venv env
source env/bin/activate
```  
Install requirements for project:
```
pip install -r requirements.txt
```
Apply database migrations:
```
python3 manage migrate
```
Run server on local host:
```
python3 manage runserver 0.0.0.0:8001
```
Go to [swagger URL](http://127.0.0.1:8001/api/schema/swagger/), and you can see swagger UI API documantation.

