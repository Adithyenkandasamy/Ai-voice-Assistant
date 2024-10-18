import google.generativeai as genai
import pathlib
import time
import take_command as tc  # Uncomment this if you're using a voice input module
import respond as rs
# Function to initialize the AI model with the API key
def configure_ai():
    genai.configure(api_key="AIzaSyBb9ONZYSIImDtFhlXccVk0pgAvlIDoc7A")
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model

# Function to generate a response using the AI model
def generate_ai_response(model, prompt):
    try:
        response = model.generate_content(prompt)
        # Extract the text response from the response object
        if response and response.candidates:
            generated_text = response.candidates[0].content.parts[0].text
            return generated_text
        else:
            return "Sorry, I didn't understand that."
    except Exception as e:
        return f"Error generating AI response: {str(e)}"

# Main loop to take input from the user and generate AI responses
def main():
    model = configure_ai()
    
    # print("AI Assistant is ready. Type something or speak (if using voice input):")
    
    while True:
        # Uncomment the line below if you have a voice command function
        my_idea = tc.takecommand()
        
        # For text input (command line or terminal)
        # my_idea = input("You: ")
        
        if my_idea.lower() in "quit":
            print("Exiting AI Assistant. Goodbye!")
            break
        
        print("Processing...")
        ai_response = generate_ai_response(model, my_idea)
        rs.say(ai_response)
        # print(f"Assistant: {ai_response}")
        
        # Optional: Add a delay to simulate processing time or to match real-world interaction
        time.sleep(1)

# Entry point for the script
if __name__ == "__main__":
    main()
