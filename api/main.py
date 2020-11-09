import query_graph as graphapi
import traceback
#from flask import request

from typing import Optional

from fastapi import FastAPI,Request

import uvicorn




#####################################################################
# Configs
#####################################################################

app = FastAPI()

#####################################################################
# API Endpoints
#####################################################################
# 'supported_endpoints': ['%s' % rule for rule in app.url_map.iter_rules()]



@app.get('/')
def hello():
    try:
        return {
            'status': 'successful',
            'message': 'Welcome to the knowledge graph api.'                        
        }
    except Exception as ex:
        traceback.print_exc()
        return {'status': 'failed', 'error': str(ex)}


# Passing p_id via Url. Parameter p_id
# will be passed to the function
@app.get('/person_details_with_relationships/{p_id}')
def person_relation_by_id(p_id:int, request: Request):
    try:
        #p_id = request.get()
        print (graphapi.relation_of_person_by_id(p_id))
        return graphapi.relation_of_person_by_id(p_id)
    except Exception as ex:
        traceback.print_exc()
        return {'status': 'failed', 'error': str(ex)}


# Same as last endpoint,
# but serving data via POST this time
@app.post('/person_details')
def call_get_person_by_id(p_id:int, request: Request):
    try :
        # Use request.data for fetching
        # json passed to request
        #p_id = request.client_host
        #p_id = Request.data.get('p_id')
        return graphapi.get_person_by_id(p_id)
    except Exception as ex:
        traceback.print_exc()
        return {'status': 'failed', 'error': str(ex)}



@app.get('/graph_size')
def count_all_node():
    try :
        return graphapi.get_all_count()
    except Exception as ex:
        traceback.print_exc()
        return {'status': 'failed', 'error': str(ex)}


#####################################################################
# Entry point
#####################################################################

if __name__ == "__main__":

    uvicorn.run("main:app")

