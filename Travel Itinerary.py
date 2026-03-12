import sys

def get_integer_input(prompt_text):
    """
    Prompts the user for input and ensures the value is a valid integer.

    Args:
        prompt_text (str): The text displayed to the user.

    Returns:
        int: The validated integer input.
    """
    while True:
        try:
            # Get the input from the user
            user_input = input(prompt_text).strip()

            # Check for empty input (though int() would catch non-numeric strings)
            if not user_input:
                print("Input cannot be empty. Please enter a value.")
                continue

            # Attempt to cast the input string to an integer
            # This handles the casting requirement and validates the data type
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number (integer) only.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

def get_string_input(prompt_text):
    """
    Prompts the user for input and ensures the string is not empty.

    Args:
        prompt_text (str): The text displayed to the user.

    Returns:
        str: The validated, non-empty string input.
    """
    while True:
        user_input = input(prompt_text).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please enter the required text.")

def organize_itinerary():
    """
    Collects and organizes travel destination details from the user.
    """
    # Use a list to store all destination dictionaries (Requirement: Lists)
    itinerary = []
    NUM_DESTINATIONS = 3

    print("--- Travel Itinerary Organizer ---")
    print(f"Please enter the details for {NUM_DESTINATIONS} destinations.")

    for i in range(NUM_DESTINATIONS):
        print(f"\n=====================================")
        print(f"DESTINATION {i + 1}")
        print(f"=====================================")

        # Use a dictionary to store information about the current destination (Requirement: Dictionaries)
        destination = {}

        # 1. Get City (Data Type: String)
        destination['city'] = get_string_input("Enter City Name: ")

        # 2. Get Country (Data Type: String)
        destination['country'] = get_string_input("Enter Country: ")

        # 3. Get Duration (Data Type: Integer - handled by get_integer_input)
        # Requirement: Casting (int()) is handled inside get_integer_input
        destination['duration_days'] = get_integer_input("Enter Duration of Stay (days): ")

        # 4. Get Budget (Data Type: Integer - handled by get_integer_input)
        # Requirement: Casting (int()) is handled inside get_integer_input
        destination['budget_usd'] = get_integer_input("Enter Estimated Budget (USD, whole numbers only): ")

        # Add the completed destination dictionary to the itinerary list
        itinerary.append(destination)

    # --- Display the Structured Information ---

    print("\n\n#####################################")
    print("### COMPLETE TRAVEL ITINERARY ###")
    print("#####################################")

    total_duration = 0
    total_budget = 0

    for idx, dest in enumerate(itinerary):
        print(f"\nDestination {idx + 1}:")
        print(f"  City:    {dest['city']}")
        print(f"  Country: {dest['country']}")
        # correct data types are displayed
        print(f"  Duration: {dest['duration_days']} days")
        print(f"  Budget:   ${dest['budget_usd']:,}") # Format budget

        # totals
        total_duration += dest['duration_days']
        total_budget += dest['budget_usd']

    print("\n-------------------------------------")
    print("ITINERARY SUMMARY:")
    print(f"Total Trip Duration: {total_duration} days")
    print(f"Total Estimated Budget: ${total_budget:,}")
    print("-------------------------------------")

if __name__ == "__main__":
    try:
        organize_itinerary()
    except KeyboardInterrupt:
        # Handles Ctrl+C gracefully
        print("\nProgram terminated by user.")
        sys.exit(0)