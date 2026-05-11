# =========================================
#        BRASS STORE SHOPPING SYSTEM
# =========================================

print("======================================")
print("      WELCOME TO BRASS STORE")
print("======================================")

# Collect customer information
customer_name = input("Enter customer name: ")

# Collect item details
item_name = input("Enter item name: ")

# Error handling for price input
while True:
    try:
        item_price = float(input("Enter item price (₦): "))

        if item_price <= 0:
            print("Price must be greater than 0.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Error handling for quantity input
while True:
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Calculate total cost
subtotal = item_price * quantity

# Apply discount
discount = 0

if subtotal >= 10000:
    discount = subtotal * 0.10

# Calculate final amount
final_amount = subtotal - discount

# Display receipt
print("\n======================================")
print("              RECEIPT")
print("======================================")

print(f"Customer Name : {customer_name}")
print(f"Item Purchased: {item_name}")
print(f"Item Price    : ₦{item_price:,.2f}")
print(f"Quantity      : {quantity}")
print(f"Subtotal      : ₦{subtotal:,.2f}")

# Check if discount was applied
if discount > 0:
    print(f"Discount (10%): ₦{discount:,.2f}")
else:
    print("Discount      : No discount applied")

print(f"Final Amount  : ₦{final_amount:,.2f}")

print("======================================")
print("   THANK YOU FOR SHOPPING WITH US!")
print("======================================")