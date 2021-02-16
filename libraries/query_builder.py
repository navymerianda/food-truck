import datetime
import config

class FoodTruckQueryBuilder:
    def __init__(self, offset):
        self.dateTimeNow = datetime.datetime.now()
        self.selectedFields = config.Config.COLUMNS
        self.numResults = config.Config.NUM_RESULTS
        self.offset = offset
    
    def dayOfWeek(self):
        '''
        Returns an instance of datetime that corresponds to an integer.
        1 -> Monday; 7 -> Sunday
        '''
        numWeekDay = self.dateTimeNow.isoweekday()
        return numWeekDay
    
    def timeFormat(self):
        '''
        Returns a formatted time string from an instance of datetime that is represented in 24 hr format.
        '''
        standardTime = "\'{0}:{1}'".format(self.dateTimeNow.hour, str(self.dateTimeNow.minute).zfill(2))
        return standardTime
    
    def buildQuery(self):
        '''
        Returns a SoQL format query. This string is attached to the base_url to
        invoke the API.
        '''
        soqlDictionary = { 
            'selection_fields' : self.selectedFields,
            'time_between': "{0} BETWEEN start24 and end24".format(self.timeFormat())
        }

        soQlQuery = (
            "?$select={selection_fields}"
            "&$where={time_between} AND dayorder ={0}"
            "&$order= applicant ASC"
            "&$limit= {1}"
            "&$offset= {2}").format(self.dayOfWeek(), self.numResults, self.offset, **soqlDictionary)

        return soQlQuery