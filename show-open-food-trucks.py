'''
Command line program to display food truck names ordered alphabetically and locations 
that are open at the current execution of the program. 
Program is designed to display 10 food trucks at a time.

API used:
This program makes use of San Francisco government's API. 
More information on this can be found at: https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b
'''

import os
import requests
import config, messages
from libraries.query_builder import FoodTruckQueryBuilder
from tabulate import tabulate

'''
Parameters
----------
offset : int
    keeps track of pagination to retrieve next or previous set of data.

Function responsible for executing food truck API by passing in the built SoQL query using requests library.  
'''
def buildQuery(offset):
    baseURL = config.Config.BASE_URL
    foodTruckQuery = FoodTruckQueryBuilder(offset = offset).buildQuery()
    formattedURL = "{0}{1}".format(baseURL, foodTruckQuery)

    if config.Config.APP_TOKEN is not None:
        requestHeader = {'X-App-Token': config.Config.APP_TOKEN}
        request = requests.get(formattedURL, headers = requestHeader)
    else:
        request = requests.get(formattedURL)
    
    return request

'''
Parameters
----------
page : int
    current page of data.
nextnum : int
    increment/decrement by 1 to keep in sync with page.

Function that maintains the page status/number as and when the user requests for next or previous
page of data and invokes the API.
'''
def nextPage(page, nextnum):
    request = buildQuery(page)
    page += nextnum
    continueLookUp = True
    return page, request, continueLookUp

'''
Parameters
----------
trucksdata : list
    list of food truck data objects.
page : int
    current page of data.

Function uses tabulate to display a well formatted table of food trucks.
'''
def displayTrucks(trucksdata, page):
    allFoodTrucks = []
    for foodTruck in trucksdata:
        applicantCol, locationCol = config.Config.COLUMNS.split(',')
        allFoodTrucks.append([foodTruck[applicantCol], foodTruck[locationCol]])

    print(tabulate(allFoodTrucks, headers=config.Config.HEADERS.split(',')))
    print(messages.MSG_VIEWPAGE.format(page))

'''
Entry point of execution of the program.

Responsible for complete execution of the program. Starts by invoking the API for offset of 0; page 1.
As the long as the user continues to look through food trucks, it will continue to execute.

If no food trucks found: appropriate message will be displayed.

3 options provided at every step: next, back and exit.

If we encounter any exception while querying the API, print it out. Ideally, we would be logging it.
'''
def main():
    try:

        continueLookUp = True
        isUserInputValid = True
        page = 1
        request = buildQuery(0)

        while continueLookUp:
            if request.ok:
                trucksData = request.json()
                if len(trucksData) == 0:
                    print(messages.MSG_NOMORE)
                    break

                displayTrucks(trucksData, page)

                isUserInputValid = False
                userInput = input(messages.MSG_MOVE_NEXT).lower()

                while not isUserInputValid:
                    if userInput == messages.MSG_NEXT:
                        page, request, continueLookUp = nextPage(page, 1)
                        isUserInputValid = True
                    elif userInput == messages.MSG_BACK:
                        page, request, continueLookUp = nextPage(page, -1)
                        isUserInputValid = True
                    elif userInput == messages.MSG_EXIT:
                        isUserInputValid = True
                        continueLookUp = False
                        break
                    else:
                        userInput = input(messages.MSG_MISS).lower()

            
            else:
                print(messages.MSG_REQ_FAIL)
        
    except Exception as queryException:
        print(queryException)

if __name__ == "__main__":
    main()






