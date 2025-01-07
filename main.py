print("Welcome to Classified Pizza online ordering!")
size = input("What size pizza would you like?\nSmall, Medium, or Large?\n")
add_pepperoni = input("Would you like pepperoni?\nYes or No?\n")
extra_cheese = input("Would you like extra cheese?\nYes or No?\n")
size_lower = size.lower()
add_pepperoni_lower = add_pepperoni.lower()
extra_cheese_lower = extra_cheese.lower()
price = 0
if size_lower == "small":
  price += 15
  if add_pepperoni_lower == "yes":
    price += 2
  if extra_cheese_lower == "yes":
    price += 1
elif size_lower == "medium":
  price += 20
  if add_pepperoni_lower == "yes":
    price += 3
  if extra_cheese_lower == "yes":
    price += 1
elif size_lower == "large":
  price += 25
  if add_pepperoni_lower == "yes":
    price += 3
  if extra_cheese_lower == "yes":
    price += 1
print(f"Your final bill is: ${price}.")
print("Thank you for choosing Classified Pizza!")