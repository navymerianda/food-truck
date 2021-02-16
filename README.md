Redfin Food Truck Challenge

A command line python program to print out food truck names ordered alphabetically and locations that are open at the current execution of the program. Program is designed to display 10 food trucks at a time.

This program makes use of San Francisco government's API. 
More information on this can be found at: https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b

Installation Requirements:

1. Make sure to have Python 3 or above installed.
2. We will require 3 external libraries:
   pip install -U python-dotenv
   -> Reads the key-value pair from env file and adds them to environment variables.

   pip install tabulate
   -> Pretty-print tabular data in Python, a library and a command-line utility.

   pip install requests
   -> Helps us make HTTP requests to external APIs.

3. API usage restrictions:
   -> Although, I have given out the APP_TOKEN in this case for your testing purposes. I would recommend having your own
      APP_TOKEN for using the API heavily.


Execution steps:

1. Navigate to redfin-foodtruck folder.
2. Run the program python show-open-food-trucks.py
3. Rest of the instructions can be followed on the console.