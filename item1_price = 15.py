item1_price = 15.50
item2_price = 45.99
item3_price = 20.00
total_budget = 80.00
total_cost = item1_price + item2_price + item3_price
print(f"Item 1 Price: ${item1_price:.2f}")
print(f"Item 2 Price: ${item2_price:.2f}")
print(f"Item 3 Price: ${item3_price:.2f}")
print(f"Total Available Budget: ${total_budget:.2f}\n")
print(f"Calculated Total Cost of Items: ${total_cost:.2f}")
if total_cost <= total_budget:
    money_left = total_budget - total_cost
    print("\nStatus: WITHIN BUDGET.")
    print(f"Money remaining (left over): ${money_left:.2f}")
else:
    money_needed = total_cost - total_budget
    print("\nStatus: OVER BUDGET.")
    print(f"Additional money needed: ${money_needed:.2f}")