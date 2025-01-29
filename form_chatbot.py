from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.runnables import RunnablePassthrough
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"  # Replace with your actual OpenAI API key

# Initialize the LLM
llm = OpenAI(temperature=0.7)

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["form_description"],
    template="""
    You are a helpful assistant that generates form structure JSON code based on the description provided.
    The form should be structured similarly to shadcn-form.com.

    Description: {form_description}

    Please generate the JSON structure for the form.
    """
)

# Create a RunnableSequence
chain = {"form_description": RunnablePassthrough()} | prompt_template | llm

# Function to generate form JSON
def generate_form_json(form_description):
    response = chain.invoke(form_description)
    return response

# Chatbot interface
def chatbot():
    print("Welcome to the Form JSON Generator Chatbot!")
    while True:
        form_description = input("Please describe the form you want to create (or type 'exit' to quit): ")
        if form_description.lower() == 'exit':
            break
        form_json = generate_form_json(form_description)
        print("\nGenerated Form JSON:\n")
        print(form_json)
        print("\n")

if __name__ == "__main__":
    chatbot()