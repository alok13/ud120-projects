#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_changed.pkl", "rb"))
print(len(enron_data[list(enron_data)[0]]))
count=0
for person_name in enron_data: 
    if(enron_data[person_name]["poi"]==1):
        count+=1

print(count)    
print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

salary=0
for person_name in enron_data: 
    if(enron_data[person_name]["salary"]!="NaN"):
        salary+=1
print(salary)

email=0
for person_name in enron_data: 
    if(enron_data[person_name]["email_address"]!="NaN"):
        email+=1
print(email) 
