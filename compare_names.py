first_name = input ("Enter a name: ")
second_name = input ("Enter a second name: ")
# string = string.lower()
first_name = first_name.lower()
second_name = second_name.lower() 
if len(first_name) > len(second_name):
  # second_name is smallest
  for index, value in enumerate(second_name):
    if first_name[index] < second_name[index]:
      break
    elif first_name[index] > second_name[index] or index == len(second_name)-1:
      first_name,second_name = second_name, first_name
      break
else:
  for index, value in enumerate(first_name):
    if first_name[index] > second_name[index]:
      first_name, second_name = second_name, first_name
      break
    elif first_name[index] < second_name[index] or index == len(first_name)-1:
      break
    
print(first_name, second_name)

third_name = input("Enter a third name: ")
third_name = third_name.lower()

if len(third_name) < len(first_name):
  for index, value in enumerate(third_name):
    if first_name[index] < third_name[index]:
      # compare third name to second name
      if len(third_name) < len(second_name):
        for index, value in enumerate(third_name):
          if second_name[index] < third_name[index]:
            break
          elif second_name[index] > third_name[index] or index == len(third_name)-1:
            first_name, second_name, third_name = first_name, third_name, second_name
            break
      else:
        for index, value in enumerate(second_name):
          if second_name[index] > third_name[index]:
            first_name, second_name, third_name = first_name, third_name, second_name
            break
          elif second_name[index] < third_name[index] or index == len(second_name)-1:
            break
      break
    elif first_name[index] > third_name[index] or index == len(third_name)-1:
      first_name, second_name, third_name = third_name, first_name, second_name
      break
else:
  for index, value in enumerate(first_name):
    if first_name[index] < third_name[index] or index == len(first_name)-1:
      # compare third name to second name
      if len(third_name) < len(second_name):
        for index, value in enumerate(third_name):
          if second_name[index] > third_name[index] or index == len(third_name)-1:
            first_name, second_name, third_name = first_name, third_name, second_name
            break
          elif second_name[index] < third_name[index]:
            break
      else:
        for index, value in enumerate(second_name):
          if second_name[index] > third_name[index]:
            first_name, second_name, third_name = first_name, third_name, second_name
            break
          elif second_name[index] < third_name[index] or index == len(second_name)-1:
            break
      break
    elif first_name[index] > third_name[index]:
      first_name, second_name, third_name = third_name, first_name, second_name
      break

print(first_name, second_name, third_name)