#--------------------------------------------------------------------------------------------
print("Lab 04\n")
#--------------------------------------------------------------------------------------------
# As this part of the code is repeated multiple times, the best practice is to make a function of it

def complement_str(length, bin, bit): # This function converts binary to 2's Complement System
    while len(bin) < length:
        bin = bit + bin
    return bin

# NOT USED, as bitwise operations are prohibited in the lab
def reverse_bit(bin): # This function reverses 0 into 1 from the string array
    for i in range(len(bin)):
        if(bin[i] == '0'):
            bin = bin[0:i] + '1' + bin[i+1:]
        else:
            bin = bin[0:i] + '0' + bin[i+1:]
    return bin

#--------------------------------------------------------------------------------------------

print("From decimal to 2's complement system")
print("-------------------------------------")

# Inputs from the user needed for the program
n = int(input("How many bits to use in the 2's complement system? ")) # Number of bits
num = int(input("Give an integer in decimal representation: ")) # The number to be converted

# Algorithm for converting decimal into 2's complement system
s = '' # Accumulator for bits
if(num >= 0): # Positive (+) number
    temp = num
    while temp > 0:
        s = str(temp % 2) + s
        temp = temp // 2
    s = complement_str(n, s, '0') # Filling empty bits with 0's
else: # Negative (-) number
    temp = 2**n + num
    while temp > 0:
        s = str(temp % 2) + s
        temp = temp // 2
    s = complement_str(n, s, '1')  # Filling empty bits with 0's


print("The 2's complement representation of", num, "is", s)

#--------------------------------------------------------------------------------------------

print("\nFrom 2's complement system to decimal")
print("-------------------------------------")

# User inputs the Binary string
s = str(input("Give an integer in 2's complement representation ({} bits): ".format(n)))
num = 0 # Accumulator for the decimal value

# Algorithm for converting 2's complement system into decimal
temp = complement_str(n, s, '0') # Makes sure that the user input is in the correct format
for i in range(len(temp)):
    if i == n-1 and temp[0] == '1': # Negative (-) binary
        num += int(temp[-1]) * 2**i * -1
    else: # Positive (+) binary
        num += int(temp[-1]) * 2**i
    temp = temp[:-1]

# Printing the value in the correct format
print("The decimal representation of", complement_str(n, s, '0'), "is", num)

print("\nThanks for using this program.")
input("Press Enter to continue ...") # Hold the screen display

#--------------------------------------------------------------------------------------------