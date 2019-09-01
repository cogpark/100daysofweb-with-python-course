from apistar import test

from test_app import app, drugs

client = test.TestClient(app)


def test_list_drugs():
    response = client.get('/')
    assert response.status_code == 200
    drugs = response.json()
    assert len(drugs) == 1000
    assert type(drugs) == list
    drug = drugs[0]
    expected = {'id': 1,
              'drug_co': 'A-S Medication Solutions LLC',
              'name_generic': 'Amoxicillin and Clavulanate Potassium',
              'name_brand': 'Amoxicillin and Clavulanate Potassium',
              'FDA_code': '54569-6043'}
    assert drug == expected
    last_id = drugs[-1]["id"]
    assert last_id == 1000


def test_create_drug():
    new_drug = dict(drug_co='A-S Medication Solutions LLC',
                    name_generic='This is a fun new drug',
                    name_brand='This has a fun new name',
                    FDA_code='54569-6043-03494')
    response = client.post('/', data=new_drug)
    assert response.status_code == 201
    assert len(drugs) == 1001

    response = client.get('/1001')
    assert response.status_code == 200
    expected = {'id': 1001,
                  'drug_co': 'A-S Medication Solutions LLC',
                  'name_generic': 'This is a fun new drug',
                  'name_brand': 'This has a fun new name',
                  'FDA_code': '54569-6043-03494'}

    assert response.json() == expected






