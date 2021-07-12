#for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:                                    #Loop through the items in the fruits list.
     print(x)
for x in fruits:                                #In the loop, when the item value is "banana", jump directly to the next item.
     if x == "banana":
       continue
     print(x)
for x in range(6):                                  #range function to loop through a code set 6 times.
  print(x)
for x in fruits:
  if x == "banana":                                 #Exit the loop when x is "banana".
      break
  print(x)
