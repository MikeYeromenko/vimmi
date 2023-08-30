from apps.common.exceptions import ValidationError
from apps.common.utils import MyList
from apps.films.handlers import films_handler

# B. Programing
my_list = MyList()
print(f"length: {my_list.length}")
print(f"average_member: {my_list.average}")
print(f"sum_of_squares: {my_list.get_sum_of_powered_elements()}")

my_new_list = MyList(start=111, end=1011, step=11)
print(f"length: {my_new_list.length}")
print(f"average_member: {my_new_list.average}")
print(f"sum_of_squares: {my_new_list.get_sum_of_powered_elements()}")

try:
    bad_list = MyList(start=98, end=207, step=0)
except ValidationError:
    ...

# C. Data management
# Task 1
print(films_handler.get_average_imb_rating_top_10())

# Task 2
print(films_handler.get_top50_films_ranges())

# Task 3 - NOTHING TO PRINT, please look at results_group_by_10.csv file
films_handler.get_top50_films_ranges()

# Task 4 - saving to the DB
films_handler.get_data_and_save()

# Tasks 5 and 6 - the queries are in the films_handler

# Task 7 - as I don't see the response - I'm not able to parse it and to insert. In our case if I have top 250 films
# in the DB - I will remove the old list of films and insert the new one.
# For other cases we can use operation UpdateOne with upsert=True. For this case Update operation is not good, because
# we need to rewrite the records from scratch

# upsert_operations = [
#     pymongo.UpdateOne(
#         filter=({"title": item["title"]}),
#         update={"$set": item},
#         upsert=True,
#     )
#     for item in new_films_list
# ]

# Task 8
# There are endpoints, e.g. GET */{lang?}/API/AdvancedSearch/{apiKey}/?parameters=values - which responds with detailed
# info about the chosen film

# Task 9 is very much alike the aggregation tasks from the above. As I don't have actors data models - I'll skip this
# task
