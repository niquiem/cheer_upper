import random

# List of compliments and affirmations
compliments = [
    "You're an incredible problem-solver.",
    "I love how passionate you are about your projects.",
    "Your dedication to your work is inspiring.",
    "Remember when you got into Grafana? That was amazing!",
    "Your kindness is a rare and beautiful thing.",
    # Feel free to add as many as you like
]

# Function to display a random compliment
def show_compliment():
    print(random.choice(compliments))

# Run the function to display a compliment
if __name__ == "__main__":
    print("Here's your compliment of the day:")
    show_compliment()
