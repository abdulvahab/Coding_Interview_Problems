#!/usr/bin/env python
'''This Script takes list of email addresses as input and return list of 10 most pupolar domains
Authoured By: Abdulvahab Kharadi
Date : 20/07/2018  '''

# import python module help to sort dictionay by value
import operator
filename = 'email.txt'                 # input file which contains all email addresse
with open(filename, 'r') as f:          # create python list by reading file line by line
    email_list = f.readlines()

domains = {}
# initiate empty python dictionary for domain as key as count as value
for email in email_list:               # iterate through email list and extract domain in dictionary
    user = email.split("@")[0]
    domain = email.split("@")[1]
    if domain not in domains:          # increment count if domain alredy present in dictionary
        domains[domain] = 1
    else:
        domains[domain] += 1

i = 0                                  # initiate result counter i
for domain, count in sorted(domains.items(), key=operator.itemgetter(1), reverse=True):
    print(domain, count)
    i += 1
    if i == 10:                       # break the for loop when result counter reach 10.
        break
