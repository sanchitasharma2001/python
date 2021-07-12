fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:                                #to a the element is present in the set. 
     print("Yes, apple is a fruit!")
fruits.add("orange")                                 #add orange to the set.
more_fruits = ["mango", "grapes"]
fruits.update(more_fruits)                           #to add multiple items (more_fruits) to the fruits set.
fruits.remove("banana")                              #to remove item from the set.
fruits.discard("banana")                             #discard method to remove "banana" from the fruits set.
