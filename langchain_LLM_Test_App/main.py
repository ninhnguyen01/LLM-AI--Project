from openai import OpenAI
from api import OPENAI_API_KEY
from langchain.prompts import PromptTemplate

def promp_generator():
    promp_template_name = PromptTemplate(
        template= input("Enter Prompt: \n"),
    )

    client = OpenAI(
    api_key= OPENAI_API_KEY
    )
    
    response = client.responses.create(
    model="gpt-4o-mini",
    input= promp_template_name.template,
    store=True,
    temperature=0.7,
    max_output_tokens= 100,
    )

    print("\n", response.output_text)
    print()

promp_generator()