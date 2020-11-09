# FastAPI

Knowledge graph api using fastapi and neo4j 

TODO : add visualization 

## preparation

install Docker 
run neo4j 
load the data via data_extraction for sample data
## Start Api
````
$ python ./api/main.py
````

If there is an error :

Kill running app and restart.

```
$ ps aux | grep knowledge_graph_api.py
kill -9 <process id>
```

## Visit Browser 

by default it would run with swagger 

![alt text](https://raw.githubusercontent.com/sgmoorthy/Knowledge_Graph_API/master/gitImages/fastapi_knowledge_api.png)

