import json
from typing import List

from apistar import App, Route, types, validators
from apistar.http import JSONResponse

# helpers

def load_drug_data():
    with open('drug_data.json') as file:
        drugs=json.loads(file.read())
        return {drug['id']: drug for drug in drugs}


drugs = load_drug_data()
COMPANIES = set([drug['drug_co']
                for drug in drugs.values()])

DRUG_NOT_FOUND = 'Drug not found. Perhaps you typed in the wrong ID?'


# import pdb;pdb.set_trace()

class Drug(types.Type):
    id = validators.Integer(allow_null=True)
    drug_co = validators.String(enum=list(COMPANIES))
    name_generic = validators.String(max_length=2000)
    name_brand = validators.String(max_length=200)
    FDA_code = validators.String(max_length=50, default='')

# API methods


def list_drugs() -> List[Drug]:
    return [Drug(drug[1]) for drug in sorted(drugs.items())]


def create_drug(drug: Drug) -> JSONResponse:
    drug_id=len(drugs) + 1
    drug.id=drug_id
    drugs[drug_id] = drug
    return JSONResponse(Drug(drug),201)


def get_drug(drug_id: int):
    drug = drugs.get(drug_id)
    if not drug:
        error = {'error': DRUG_NOT_FOUND}
        return JSONResponse(error, 404)
    return JSONResponse(Drug(drug), 200)


def update_drug(drug_id:int, drug: Drug ) -> JSONResponse:
    if not drugs.get(drug_id):
        error = {'error': DRUG_NOT_FOUND}
        return JSONResponse(error, 404)
    drug_id = drug.id
    drugs[drug_id] = drug
    return JSONResponse(Drug(drug), 201)


def delete_drug(drug_id:int) -> JSONResponse:
    if not drugs.get(drug_id):
        error = {'error': DRUG_NOT_FOUND}
        return JSONResponse(error, 404)

    del drugs[drug_id]
    return JSONResponse({},204)

routes = [
    Route('/', method='GET', handler=list_drugs),
    Route('/', method='POST', handler=create_drug),
    Route('/{drug_id}', method='GET', handler=get_drug),
    Route('/{drug_id}', method='PUT', handler=update_drug),
    Route('/{drug_id}', method='DELETE', handler=delete_drug)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
