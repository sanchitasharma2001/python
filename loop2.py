#while loop

i = 1
while i < 6:                                     #Print i as long as i is less than 6.
    print(i)
    i += 1
print("\n")                                     #break line
i=1
while i < 6:                                     #Stop the loop if i is 3.
  if i == 3:
    break
  i += 1
print("\n")
i = 0
while i < 6:                                     #In the loop, when i is 3, jump directly to the next iteration.
  i += 1
  if i == 3:
    continue
  print(i)
print("\n")
i = 1
while i < 6:                                     #Print a message once the condition is false.
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
