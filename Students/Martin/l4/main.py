import miles, kilometers
validValue = True
processing = True
while processing:
  # Type checking
  try:
  	distance = float(input("Enter a distance value: "))
  except ValueError:
    print("You entered an invalid distance value")
    validValue = False
    continue
  unit = input("Enter a unit of length (M = Miles, KM = Kilometers): ")
  if unit != "M" and unit != "KM":
      print("You entered an invalid unit of length")
      validValue = False
      continue
  # Converting
  if validValue:
    if unit == "M":
      conv_answer = kilometers.convertToKilometers(distance)
      print(f"Your distance of {distance} miles is equivalent to {conv_answer} kilometers.")
    elif unit == "KM":
      conv_answer = miles.convertToMiles(distance)
      print(f"Your distance of {distance} kilometers is equivalent to {conv_answer} miles.")
  
  # Check if Continue
  cont_process = input("Press 'X' to quit, or enter to continue processing: ")
  if cont_process != '':
    processing = False