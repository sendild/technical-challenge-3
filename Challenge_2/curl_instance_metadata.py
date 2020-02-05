#!/usr/bin/python3.6

"""
Challenge #2

PRE-REQUISITE:-
python3.6 -m pip install requests
https://pypi.org/project/requests/


IMDSv1 method is used to generate the instance metadata

"""


import requests
#result = requests.get('http://localhost')
result = requests.get("http://169.254.169.254/latest/meta-data/")

print(result.json())


# Print the ami_id and hostname from instance metadata
ami_id = requests.get("http://169.254.169.254/latest/meta-data/ami-id")
print(ami_id.json())

host_name = requests.get("http://169.254.169.254/latest/meta-data/hostname")
print(host_name.json())
