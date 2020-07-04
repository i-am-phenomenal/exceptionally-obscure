import csv
import os 

"""
    users.csv is the file which i generated after connecting to production database of compass application
    user_78.csv is the file from mail. 

    users.csv contains 877 records 
    user78_csv contains 979 records

"""

def get_missing_records(diff, records):
    missing = []
    diff.sort(key=take_first)
    
    for id in diff: 
       for record in records: 
            if id.lower() == record[2].lower():
                # print(record[2], " ---> ", id.lower())
                missing.append(record)
            
            else:
                pass
            
    return missing

def write_to_csv(diff): 
    global default_path, user_csv
    missing_records = get_missing_records(diff, user_csv["records"])
    with open(default_path + "missing_values_in_Users_78.csv", mode="w") as file:
        writer  = csv.writer(file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow(user_csv["headers"])
        for record in missing_records: 
            writer.writerow(record)


def take_first(ele):
    return ele[0]

def sort_by_mail(ele): 
    return ele[2]

def write_duplicates_to_csv(records):
    global default_path, user78_csv

    records.sort(key=sort_by_mail)

    with open(default_path + "duplicate_records_in_Users_78.csv", mode="w") as file:
        writer  = csv.writer(file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow(user78_csv["headers"])
        for record in records: 
            writer.writerow(record)


def write_missing_to_csv(missing_records):
    global default_path, user78_csv

    missing_records.sort(key=take_first)
    
    with open(default_path + "additional_values_in_Users_78.csv", mode="w") as file:
        writer  = csv.writer(file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow(user78_csv["headers"])
        for record in missing_records: 
            writer.writerow(record)


def check_difference(users, users_78):
    names = [x[2].lower() for x in users ]
    names_78 = [x[2].lower() for x in users_78]

    dups = list(set([x for x in names_78 if names_78.count(x) > 1]))
    
    # difference = set(users).difference(users_78) # Missing records in names_78
    # difference_2 = set(users_78).difference(users) # Additional values in names_78
    
    diff = [item for item in names_78 if item not in names] # Items which are not in production but are there in User78.csv
    
    # print(diff)
    # diff_1 = [item for item in names if item not in names_78]
    
    missing = get_missing_records(diff, user78_csv["records"])

    # missing.remove(['939', 'Elodie Morel-Bazin', 'emorel-bazin@christies.com', '', '', '', '', ''])
    # missing.remove(['940', 'Emma Bleasdale', 'emorel-bazin@christies.com', '', '', '', '', ''])
    # print(missing)
    # write_to_csv(difference)

    duplicate_records = get_missing_records(dups, user78_csv["records"]) #get_duplicate_records(dups, user78)

    print(duplicate_records)
    print(len(duplicate_records))
    write_missing_to_csv(missing)
    write_duplicates_to_csv(duplicate_records)


def find_users_diff(user_csv, user78_csv):
    users = []
    users_78 = []
    for element in user_csv["records"]: 
        users.append((element[0], element[1], element[2]))
    
    for element in user78_csv["records"]:
        users_78.append((element[0], element[1], element[2]))

    check_difference(users, users_78)

default_path = os.getcwd() + "/csv_files/"
rows = []
headers = []

user_csv = {"headers": [], "records": []}
user78_csv = {"headers": [], "records": []}

with open(default_path + "users.csv", 'rt') as users: 
    data = csv.reader(users)
    for row in data: 
        rows.append(row)

headers = rows[0]
rows = rows[1:]

user_csv["headers"] = headers 
user_csv["records"] = rows

rows = []
headers = []

with open(default_path + "user_78.csv", 'rt') as user_78: 
    data = csv.reader(user_78)
    for row in data: 
        rows.append(row)

headers = rows[0]
rows = rows[1:]
user78_csv["headers"] = headers
user78_csv["records"] = rows




find_users_diff(user_csv, user78_csv)
