import random

# Define a list of 100 random words
words = ['apple', 'banana', 'orange', 'cherry', 'grape', 'kiwi', 'lemon', 'mango', 'peach', 'pear',
         'pineapple', 'strawberry', 'watermelon', 'blueberry', 'raspberry', 'blackberry', 'apricot',
         'avocado', 'cantaloupe', 'coconut', 'fig', 'guava', 'honeydew', 'lime', 'papaya', 'plum',
         'pomegranate', 'tangerine', 'tomato', 'zucchini', 'carrot', 'potato', 'onion', 'garlic',
         'ginger', 'pepper', 'cucumber', 'eggplant', 'celery', 'broccoli', 'cauliflower', 'asparagus',
         'spinach', 'lettuce', 'kale', 'cabbage', 'radish', 'turnip', 'beet', 'corn', 'peas',
         'beans', 'chickpeas', 'lentils', 'tofu', 'tempeh', 'quinoa', 'rice', 'pasta', 'bread',
         'croissant', 'bagel', 'donut', 'pancake', 'waffle', 'frenchtoast', 'omelette', 'scrambledeggs',
         'bacon', 'sausage', 'ham', 'steak', 'chicken', 'turkey', 'fish', 'shrimp', 'lobster',
         'crab', 'clam', 'oyster', 'mussels', 'pizza', 'burger', 'hotdog', 'taco', 'burrito',
         'sushi', 'ramen', 'pho', 'padthai', 'curry', 'stirfry', 'salmon', 'trout', 'tuna']

# Shuffle the list of words
random.shuffle(words)

# Define initial score and maximum number of attempts
score = 0
max_attempts = 5

# Loop through each word in the shuffled list
for word in words:
    attempts = 0
    while attempts < max_attempts:
        # Get user input
        user_input = input(f"Type the word '{word}': ")
        # Check if user input matches the word
        if user_input == word:
            print("Correct!")
            score += 1
            break
        else:
            print("Incorrect!")
            attempts += 1
            score -= 1
    else:
        print(f"Sorry, the word was '{word}'.")
    
# Print final score
print(f"Your final score is {score}.")
