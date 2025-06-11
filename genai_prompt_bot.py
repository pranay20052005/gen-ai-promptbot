# Simple GenAI Prompt Bot (using OpenAI API simulation)

def generate_response(prompt):
    """
    Simulates a basic response from an AI model to a given prompt.
    In real-world usage, this would call OpenAI's API or similar.
    """
    if "hello" in prompt.lower():
        return "Hi there! How can I assist you today?"
    elif "your name" in prompt.lower():
        return "I'm a simple GenAI bot created by Pranay!"
    elif "bye" in prompt.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm still learning. Can you rephrase that?"

# Example usage
if __name__ == "__main__":
    print("Welcome to GenAI Prompt Bot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: See you soon!")
            break
        response = generate_response(user_input)
        print("Bot:", response)
