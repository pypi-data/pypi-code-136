from coda_api import hub
import pprint

access_token = hub.get_access_token({
  'username': 'louism',
  'password': 'unsafeunsafe',
  'client_id': 'test-user',
  'client_secret': '77gm8WS9YjIiK8FdUupX6x6QMucuJSQd',
  'grant_type': 'password'
    
})

query = {
    "selectors": [{
        "resource": "Patient","label":"Patient_0","filters":[],
        "fields": [{"path":"age","label":"Patient_0_age","type":"integer"}]}
    ],
    "options": {
        "measures": {"continuous": ["count","mean","stdev","ci95"],
            "categorical": ["count","mode"]
        }
    }
}

sites = ['111']
data = hub.execute_query('stats', 'summarize', sites, query, access_token)

pp = pprint.PrettyPrinter()
pp.pprint(data)