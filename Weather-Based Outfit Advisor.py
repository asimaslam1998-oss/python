temperature = None
weather_type = " "
wind_speed = None
while True:
    temp_input = input("Enter the current temperature (in Fahrenheit or celsius): ")
    try:
        temperature = float(temp_input)
        break # Exit the loop if conversion is successful
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")
Valid_weather = ['sunny', 'cloudy', 'rainy', 'snowy']

while True:
    weather_input = input("enter the weather type (sunny, rainy, snowy, etc.): ")
    weather_type = weather_input.lower()

    if weather_type in Valid_weather:
        break # Exit the loop if the input is valid
    else:
        print("Invalid weather type. Please choose from the recognized options.")
while True:
    wind_input = input("Enter the wind speed (in mph or km/h): ")
    try:
        wind_speed = float(wind_input)
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Invalid input. Please enter a number for the wind speed.")
outfit_suggestion = ""

if temperature < 40 and wind_speed >= 15:
    outfit_suggestion = "It's freezing and windy! Suggest a heavy **coat, scarf, gloves, and a hat**."
    
elif weather_type == 'rainy':
    outfit_suggestion = "It's rainy! Suggest a **waterproof jacket, rain boots, and an umbrella**."
    
elif weather_type == 'snowy':
    outfit_suggestion = "It's snowing! Suggest a **heavy parka, thermal pants, snow boots, and thick gloves**."
    
elif temperature > 70 and weather_type == 'sunny':
    outfit_suggestion = "It's hot and sunny! Suggest **shorts, a t-shirt, and sunglasses**."

elif temperature >= 40 and temperature <= 70 and weather_type == 'sunny':
    outfit_suggestion = "It's mild and sunny. Suggest a **light jacket, jeans, and sneakers**."

else:
    # Handles cloudy or any other mild, non-extreme conditions
    outfit_suggestion = "Suggest **layers**, like a sweater or light hoodie, as conditions are moderate."
print("\n--- Outfit Advisor Suggestion ---")
print("Based on the weather, we suggest: " + outfit_suggestion)