x = "Hello World"
print(len(x))
fruits = ["apple", "banana", "cherry","lichi"]
fruits[0] = "kiwi"                             #Change the value from "apple" to "kiwi", in the fruits list.
fruits.append("orange")                        #add orange to the list.
fruits.insert(1, "lemon")                      #insert method to add "lemon" as the second item in the fruits list.
fruits.remove("banana")                        #remove banana from the list.
print(fruits[-1])                              #negative indexing to print the last item in the list
print(fruits[2:5])                             #to print the third, fourth, and fifth item in the list.
print(len(fruits))                             #to print the number of items in the list.
