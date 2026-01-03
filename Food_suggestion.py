from textblob import TextBlob

print("Welcome to the Food Suggestion Chatbot\n")

def extract(text, options):
    text = text.lower()
    for o in options:
        if o in text:
            return o
    return options[0]

def get_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"

food = extract(
    input("What type of food do you prefer? (veg / non-veg / vegan / healthy / fast)\n"),
    ["veg", "non", "vegan", "healthy", "fast"]
)

cuisine = extract(
    input("\nWhich cuisine do you like? (south / north / chinese / italian)\n"),
    ["south", "north", "chinese", "italian"]
)

spice = extract(
    input("\nHow spicy do you want the food? (mild / medium / spicy)\n"),
    ["mild", "medium", "spicy"]
)

meal = extract(
    input("\nIs it breakfast, lunch or dinner?\n"),
    ["breakfast", "lunch", "dinner"]
)

mood = get_mood(
    input("\nHow are you feeling right now?\n")
)

def suggest_food(food, cuisine, spice, meal, mood):

    if food == "veg":
        if meal == "breakfast":
            return ["Idli", "Dosa", "Upma", "Pongal", "Poha"]
        if meal == "lunch":
            return ["Veg Meals", "Curd Rice", "Veg Biryani", "Sambar Rice"]
        return ["Chapati with Kurma", "Veg Fried Rice", "Paneer Curry"]

    if food == "non":
        if meal == "breakfast":
            return ["Egg Omelette", "Egg Dosa", "Chicken Sandwich"]
        if meal == "lunch":
            return ["Chicken Biryani", "Chicken Curry with Rice", "Fish Curry"]
        return ["Grilled Chicken", "Chicken 65", "Egg Fried Rice"]

    if food == "vegan":
        if meal == "breakfast":
            return ["Oats with Fruits", "Smoothie Bowl", "Vegan Toast"]
        if meal == "lunch":
            return ["Vegan Buddha Bowl", "Vegetable Rice", "Dal with Rice"]
        return ["Vegetable Soup", "Stir Fried Vegetables"]

    if food == "healthy":
        if meal == "breakfast":
            return ["Oats", "Fruit Salad", "Boiled Eggs"]
        if meal == "lunch":
            return ["Grilled Vegetable Salad", "Brown Rice with Dal"]
        return ["Soup", "Steamed Vegetables"]

    if food == "fast":
        if meal == "breakfast":
            return ["Veg Sandwich", "Burger", "French Toast"]
        if meal == "lunch":
            return ["Pizza", "Burger with Fries", "Fried Rice"]
        return ["Cheese Pizza", "Noodles", "Wraps"]

    return ["Simple Home Food"]

options = suggest_food(food, cuisine, spice, meal, mood)

print("\nBased on your preferences, you can try:")
for item in options:
    print("-", item)
