import json
import pandas as pd


def load_session_json_data(filename):
    df = pd.read_json(filename, orient='rows')
    return df


sessions = load_session_json_data('test3.json')
# print(sessions.head(10))
lookup = input("Add page: ")
x = sessions["Page"] == lookup
print(sessions[x])
# data = sessions[lookup].to_json()


# lookup = sessions.sessionID == session_id

# print(len(sessions))

"""
cnt = len(csv[csv['Age'] == 22])
print(cnt)  # outputs number of rows where age is 22

cnt = len(csv[(csv['Age'] == 22) & (csv['Sex'] == 'female')])
print(cnt)  # outputs number of rows where age is 22 and sex is female

cnt = len(csv[(csv['Age'] < 10) | (csv['Age'] > 30)])
print(cnt)  # outputs number of rows where age is less than 10 or greater than 30

lookup = sessions.sessionID == session_id
data = sessions[lookup].to_json()
return data"""


