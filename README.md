# First Python Project
# Find most suitable link between device and stations

The project can be run in 2 ways:
- Run the solution locally:  
    Before start:
    - Download python version 3.7  
        https://www.python.org/downloads/  
    - Install the additional module needed to run the project  
        pip install -r requirements.txt  
      
    Run the command "python app.py" or "python3 app.py" if you are on macOS/Linux  
    if you don't you don't have the enviroment setup to run python3 as standard  
  
    To run the unit test of the solution run  
    python -m unittest unittests.testcomputemostsuitable  
    also here if on macOS or Linux use python3 instead if you don't have configured  
    python3 as standard  
  
- Deployed version of the solution as Google Cloud Function  
    Before start:  
    - Google Cloud Function Runtime  
        https://cloud.google.com/functions/docs/concepts/python-runtime  
    - Setup the enviroment  
        https://cloud.google.com/python/setup  
        No need to install the Google Cloud Client Library for Python for this project  
    - HTTP Functions in Python  
        https://cloud.google.com/functions/docs/writing/http  
    - Deploy a function  
        https://cloud.google.com/functions/docs/deploying/  
  
    The file that contains the functions is main.py  
  
    The only function deployed is computefunction  
  
    I've deployed it using gcloud command-line tool  
    gcloud functions deploy computedevice --runtime python37 --trigger-http --region europe-west1  
  
    To access to the function via the URL  
    https://europe-west1-linkdevicetostation.cloudfunctions.net/computedevice?x=device_coordinate_x&y=device_coordinate_y  
    where device_coordinate_x is the X coordinate of the device we need to compute  
    where device_coordinate_y is the Y coordinate of the device we need to compute  
  
    if no args are passed in the query string it will process the standard points (0,0), (100, 100), (15,10) and (18, 18).  
    https://europe-west1-linkdevicetostation.cloudfunctions.net/computedevice  
  
    The result is a json array of string as described in the problem  
    “Best link station for point x,y is x,y with power z”  
    Or  
    “No link station within reach for point x,y”  