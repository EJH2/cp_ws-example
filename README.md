# CP WS
This is an example project demonstrating a [modified version](https://github.com/EJH2/celery-progress) of 
[this project](https://github.com/czue/celery-progress). 

### Installing
* Download source
* Navigate to project folder
* Run `pip install -r requirements.txt`
* Download the modified celery-progress package from the link above
* Navigate to package folder
* Run `pip install .` to install http-only, or `pip install .[channels,redis]` to install http and ws
* Navigate to project folder
* Change `.env` vars to suit your needs
* Done!

### Using
* Start both the django and celery servers
* Go to index page to view various optional tests