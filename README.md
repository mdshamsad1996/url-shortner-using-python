## URL Shortner
URL shortening is used to create shorter aliases for long URLs
 Here is two api we have used
 1. @app.route('/', methods=['POST'])  create_shorten_url() --->creating short url via long url
 2. @app.route("/<hash>/", methods=['GET'])  long_url(hash)---->redirect long url via short url
 
Below Technologies has been used 

    Language: Python
    Database: NoSQL (MongoDb)
    Framework: Flask
 

Make sure python (preferred python3.7) is added to path.

      python --version
       or		
     python3.7 --version
     
 Install virtualenv using pip.

     pip install virtualenv 
   
 First create a virtual environment for the project.
 
    virtualenv -p python3.7 venv or virtualenv venv
       . venv/bin/activate (Linux)
       . venv/Scripts/activate (windows)

Install dependencies
    
    pip install -r requirements.txt

set up linter:

    create setup.cfg file for  pycodestyle and pep8
    generate pylintrc file using below command for pylint
      pylint --generate-rcfile > .pylintrc
      (change max_length_character to 160 (as per requiremnet))
      
    Linter Script:
       create lint.sh file inside scripts folder
        run using command sh scripts/lint.sh
        
 To run app using below command
 
     python run.py