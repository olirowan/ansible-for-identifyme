from pymongo import MongoClient


# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


def main():

    while (1):
        # chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to read.\n')

        if selection == '1':
            insert()
        if selection == '2':
            read()
        else:
            print '\n INVALID SELECTION \n'


# Function to insert data into mongo db
def insert():

    try:
        employeeId = raw_input('Enter Employee id :')
        employeeName = raw_input('Enter Name :')
        employeeAge = raw_input('Enter age :')
        employeeCountry = raw_input('Enter Country :')

        db.Employees.insert_one(
            {
                "id": employeeId,
                "name": employeeName,
                "age": employeeAge,
                "country": employeeCountry
            })

        print '\nInserted data successfully\n'

    except Exception, e:
        print str(e)


# Function to read data from mongo db
def read():

    try:
        empCol = db.Employees.find()
        print '\n All data from EmployeeData Database \n'
        for emp in empCol:
            print emp


    except Exception, e:
        print str(e)

main()




