## B. Programing
## C. Data management

## Look all the results please run:
```
poetry install
poetry shell
```

### Please start the DB instance with
```docker-compose up```

### Upload to the db the list with films

### When DB ready run from the terminal:
```python run.py```

#### Task 1 - results will be printed in the command line

#### Task 2 - results will be printed in the command line

#### Task 3
- NOTHING TO PRINT, please look at results_group_by_10.csv file

#### Task 4 - saving to the DB

#### Tasks 5 and 6 - the queries are in the films_handler

#### Task 7 
as I don't see the response - I'm not able to parse it and to insert. In our case if I have top 250 films
in the DB - I will remove the old list of films and insert the new one.
For other cases we can use operation UpdateOne with upsert=True. For this case Update operation is not good, because
we need to rewrite the records from scratch
```
upsert_operations = [
    pymongo.UpdateOne(
        filter=({"title": item["title"]}),
        update={"$set": item},
        upsert=True,
    )
    for item in new_films_list
]
```

#### Task 8
There are endpoints, e.g. GET */{lang?}/API/AdvancedSearch/{apiKey}/?parameters=values - which responds with detailed
 info about the chosen film

#### Task 9 
is very much alike the aggregation tasks from the above. As I don't have actors data models - I'll skip this task
