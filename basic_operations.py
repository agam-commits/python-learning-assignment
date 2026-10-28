num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = int(input("Enter [base] number to calculate power? "))
num4 = int(input("Enter power of [base] number? "))
num5 = int(input("Enter number to calculate [square_root]? "))

#Add,Sub,Multiply,Divide,Floor_division,modulus, pow, square_root mathematical operations:

addition = num1+num2
print(f"Addition is = {addition}")
#rounding off addition result upto 2 digit:
print(f"Rounded off upto 2 digits is = {round(addition, 2)}")

subtraction = num1-num2
print(f"Subtraction is = {subtraction}")
#rounding off subtraction result upto 2 digit:
print(f"Rounded of upto 2 digits is = {round(subtraction, 2)}")

multiplication = num1*num2
#multiply and converted result into int literal:
print(f"Multiplication is = {multiplication}")
#rounding off multiplication result upto 2 digit:
print(f"Rounded off upto 2 digits is = {round(multiplication, 2)}")

division = num1/num2
print(f"Division is = {division}")

floor_division = num1//num2
print(f"Floor division is = {floor_division}")

modulus = num1%num2
print(f"Modulus value(remainder) is = {modulus}")

power = num3**num4
base_number = num3
superscript = num4
print(f"{base_number} to the power of {superscript} is = {power}")

square_root = num5**0.5
base_number = num5
print(f"square root of {base_number} is = {round(square_root, 2)}")