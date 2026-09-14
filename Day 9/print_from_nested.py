# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany":["Stutgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

# OR

# for x in travel_log.values():
#     if "Lille" in x:
#         print(x[1])

# nester list

nested_list = ["A", "B",["C", "D"]]

# print "D" from nested list

print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12,
        
    },
    "Germany":{
        "cities_visited": ["Berlin", "Hamburg", "Stutgart"],
        "total_visits": 5
               }
}

# print value from nested list inside dictionary inside another dictionary

print(travel_log["Germany"]["cities_visited"][2])