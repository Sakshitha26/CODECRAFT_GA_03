import random

def build_markov_model(text):
    words = text.split()
    model = {}

    # Create the transitions
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in model:
            model[current_word] = []
        model[current_word].append(next_word)
    
    return model

def generate_text(model, length=20):
    if not model:
        return "No text provided to build a model."

    # Pick a random starting word from the user's input
    current_word = random.choice(list(model.keys()))
    result = [current_word]

    for _ in range(length - 1):
        possibilities = model.get(current_word)
        if not possibilities:
            break
            
        current_word = random.choice(possibilities)
        result.append(current_word)

    return " ".join(result)

# --- INTERACTIVE USER INPUT ---
print("--- Markov Chain Text Generator ---")
user_data = input("Paste your training text here and press Enter: \n")

if len(user_data.split()) < 2:
    print("Please provide at least two words to create a chain.")
else:
    # Build and generate
    model = build_markov_model(user_data)
    output = generate_text(model, length=20)

    print("\n--- Generated Result ---")
    print(output)
    print("------------------------\n")