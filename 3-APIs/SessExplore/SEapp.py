
import json
from typing import List
import pandas as pd
from pandas.io.json import to_json

from apistar import App, Route, types, validators
from apistar.http import JSONResponse


def load_session_json_data(filename):
    df = pd.read_json(filename, orient='rows')
    return df


file = 'test3.json'
sessions = load_session_json_data(file)


# methods
def session_by_id(session_id: str):
    global sessions
    lookup = sessions["sessionID"] == session_id
    data = sessions[lookup].to_json()
    return data


def sessions_by_page(nodeID: int):
    global sessions
    lookup = sessions["nodeID"] == nodeID
    data = sessions[lookup].to_json()
    return data

# errors
SESSION_NOT_FOUND = 'Couldn\'t find a session with that ID.'
PAGE_NOT_FOUND = 'Couldn\'t find a session with that page.'

#

routes = [
    # Route('/', method='GET', handler=list_sessions),
    # Route('/', method='POST', handler=create_drug),
    Route('/{session_id}', method='GET', handler=session_by_id),
    Route('/{nodeID}', method='GET', handler=sessions_by_page),
    # Route('/{drug_id}', method='DELETE', handler=delete_drug)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)

