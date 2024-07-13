from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the pre-trained StableLM model and its tokenizer
# Model: StableLM-2-Zephyr-1.6b, designed for large-scale language tasks
# Tokenizer: Converts text into numerical input for the model
tokenizer = AutoTokenizer.from_pretrained('stabilityai/stablelm-2-zephyr-1_6b')
model = AutoModelForCausalLM.from_pretrained(
    'stabilityai/stablelm-2-zephyr-1_6b',
    device_map="auto"  # Automatically utilize available hardware (GPU if present)
)

def chat_with_model():
    # Initialize an empty list to store the conversation history as a series of messages
    chat_history = []  

    while True:
        # Get user input and convert it to lowercase for case-insensitive comparison
        user_input = input("You: ")
        if user_input.lower() == "exit":  
            # Check if the user wants to end the chat and break the loop if so
            break

        # Add the user's message to the chat history
        chat_history.append({'role': 'user', 'content': user_input})

        # Prepare the input for the model using the chat template (for better context handling)
        inputs = tokenizer.apply_chat_template(
            chat_history, 
            add_generation_prompt=True,  # Add a prompt to guide the model's response
            return_tensors='pt'           # Return PyTorch tensors for model compatibility
        )

        # Generate a response from the model
        tokens = model.generate(
            inputs.to(model.device),      # Ensure inputs are on the correct device
            max_new_tokens=1024,         # Limit the response length
            temperature=0.5,             # Control randomness (0.5 is a good balance)
            do_sample=True               # Enable sampling for diverse responses
        )

        # Decode the generated tokens into text, skipping special tokens
        model_output = tokenizer.decode(tokens[0], skip_special_tokens=True)

        # Add the model's response to the chat history
        chat_history.append({'role': 'assistant', 'content': model_output})

        # Print the model's response
        print("Model:", model_output)

# This part ensures the chat function only runs when this script is executed directly
if __name__ == "__main__":
    chat_with_model()
