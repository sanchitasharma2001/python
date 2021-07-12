car =	{"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.get("model"))                                        #to print the value of the "model" key of the car dictionary.
car["year"]= 2020                                              #Change the "year" value from 1964 to 2020.
car["color"]="red"                                             #Add the key/value pair "color" : "red" to the car dictionary.
car.pop("model")                                               #to remove "model" from the car dictionary.
car.clear()                                                    # clear method to empty the car dictionary.
