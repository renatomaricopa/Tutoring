# Global scope

#F = (C*9/5)+32
#C = (F-32)*5/9

# temps is a list that stores our conversion temps = [32, 0]
# tempScale is the scale we are using: "F" or "C"
def convTemp(temps, tempScale):
    # local scope
    if tempScale == 'F':
        # putting the user temp at index 0 into our formula for farenheight to celcius conversion
        convTemp = (temps[1]-32)*5/9
        # storing converted Temperature inside our temps list at index 0
        temps[0] = convTemp
    elif tempScale == 'C':
        # putting the user temp at index 0 into our formula for celcius to farenheight conversion
        convTemp = (temps[0]*9/5)+32
        # storing converted Temperature inside our temps list at index 1
        temps[1] = convTemp
    

# defining/initializing the list
temps = [0, 0]
# getting user input for temperature and scale
userTemp = float(input('Enter a temperature value.'))
scale = input('Enter "F" for farenheit and "C" for celsius.')
# temps = [userTemp, 0]
if scale == "F":
	temps[1] = userTemp
elif scale == "C":
    temps[0] = userTemp
convTemp(temps, scale)
print("You entered " + str(userTemp) + "degrees" + scale)
print("The temperature in Celsius is " + str(temps[0]))
print("The temperature in Farenheit is " + str(temps[1]))