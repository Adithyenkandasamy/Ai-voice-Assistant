import google.generativeai as genai
import pathlib
import take_command as tc

class MyAIModel:
    def test_text_gen_text_only_prompt(self, solver):
        # [START text_gen_text_only_prompt]
        genai.configure(api_key="AIzaSyBb9ONZYSIImDtFhlXccVk0pgAvlIDoc7A")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(solver)
        return response
        

# Now create an instance of the class and call the method
my_model = MyAIModel()
while True:
    my_idea=tc.takecommand() 
    # my_model.test_text_gen_text_only_prompt(my_idea)
    print(my_model.test_text_gen_text_only_prompt)
