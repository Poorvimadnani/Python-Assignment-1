#STUDENT NAME: Poorvi Madnani
#STUDENT NUMBER:251178757
#DATE: 6TH OCTOBER 2023
#INSTRUCTOR NAME: CARO STRICKLAND
#DESCRIPTION: THIS PROGRAM HELPS US IDENTIFY THE MENU OPTIONS AND HELPS US GENERATE A ORDER WITH DIETARY PREFERENCES AND HENCE GENERATE A TOTAL BILL WITH THE NUMBER
# OF INVITEES AS WELL AS SUMMARIZES THE ORDER DETAILS.

# The menu options available which remain constant
MENU = {
    "Rock-N-Roll Salad Bowl": {"keto": True, "vegan": True, "gluten_free": True, "price": 19.99},
    "Zucchini Noodle Stairway to Herbs": {"keto": True, "vegan": True, "gluten_free": False, "price": 17.29},
    "Houses of the Holy Guacamole": {"keto": True, "vegan": False, "gluten_free": False, "price": 24.99},
    "Ramble On Rice Bowl": {"keto": False, "vegan": True, "gluten_free": True, "price": 15.95},
    "Codway to Heaven": {"keto": False, "vegan": False, "gluten_free": True, "price": 27.88},
    "Whole Lotta Flavors Platter": {"keto": False, "vegan": False, "gluten_free": False, "price": 19.99},
    "Zeppelin Zest Lemonade": {"keto": False, "vegan": False, "gluten_free": False, "price": 5.99}
}

# Tax rate which is to be calculated on all bills
TAX_RATE = 0.15

# Function to get user input for dietary preference
def get_dietary_preference(prompt):
    user_input = input(prompt).lower()
    return user_input == "y"

# Calculating the total cost of the dishes before tax and tip
def calculate_total_cost(order_list, menu):
    total_cost = 0
    for dish in order_list:
        if dish in menu:
            total_cost += menu[dish]["price"]
    return total_cost

# This part of the program helps generate the output for the invitees in detail
def order_details():
    tot_invitees = int(input("Please enter the number of people attending dinner: "))
    orders = []

    for invitee_num in range(1, tot_invitees + 1):
        print(f"Please enter the order details for invitee number {invitee_num}/{tot_invitees}")

        keto_friendly = get_dietary_preference("Do you want a keto-friendly meal? (y/n): ")
        vegan_friendly = get_dietary_preference("Do you want a vegan-friendly meal? (y/n): ")
        gluten_free = get_dietary_preference("Do you want a gluten-free meal? (y/n): ")
#This part of the program helps distinguish the dietary prefrences and the options available according to preferences
        dietary_preferred_dishes = []
        for dish, details in MENU.items():
            if keto_friendly and vegan_friendly and gluten_free:
                if details["keto"] and details["vegan"] and details["gluten_free"]:
                    dietary_preferred_dishes.append(dish)
            elif (keto_friendly or not details["keto"]) and \
               (vegan_friendly or not details["vegan"]) and \
               (gluten_free or not details["gluten_free"]):
                dietary_preferred_dishes.append(dish)

        if dietary_preferred_dishes:
            print(f"\n{len(dietary_preferred_dishes)} suitable dishes according to preferences of the invitee found:")
            dish_index = 1
            for dish in dietary_preferred_dishes:
                print(f"{dish_index}. {dish}")
                dish_index += 1

            choice = int(input("Choose a dish by entering the corresponding number or 0 for Zeppelin Zest Lemonade): "))
            if choice == 0:
                orders.append("Zeppelin Zest Lemonade")
            elif 1 <= choice <= len(dietary_preferred_dishes):
                orders.append(dietary_preferred_dishes[choice - 1])
        else:
            print("\nNo suitable dishes found. Ordering Zeppelin Zest Lemonade.")
            orders.append("Zeppelin Zest Lemonade")
# This part of the program helps generate a bill for the dishes ordered by the invitee
    tip_percentage = int(input("\nHow much do you want to tip your server (%)? "))
    total_cost_before_tax = calculate_total_cost(orders, MENU)
    total_tax = total_cost_before_tax * TAX_RATE
    total_cost_after_tax = total_cost_before_tax + total_tax
    total_tip = total_cost_after_tax * (tip_percentage / 100)
    total_cost_after_tip = total_cost_after_tax + total_tip
    print(f"\nYou have {tot_invitees} invitees with the following orders:")

    invitee_num = 1
    for dish in orders:
        print(f"{invitee_num} invitee(s) ordered the {dish} and the cost is: ${MENU[dish]['price']:.2f}")
        invitee_num += 1
#This part of the program prints the order output for the total bill
    print(f"The total cost before tax is: ${total_cost_before_tax:.2f}")
    print(f"The total cost after tax is: ${total_cost_after_tax:.2f}")
    print(f"The total cost after {tip_percentage}% tip is: ${total_cost_after_tip:.2f}")

if __name__ == "__main__":
    order_details()
