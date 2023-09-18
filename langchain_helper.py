from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.5)

def generate_name_and_items(wear):
    # Chain 1: Store Name
    prompt_template_name = PromptTemplate(
        input_variables=['wear'],
        template="""I want to open a fashion dress store with {wear} styles. 
                    Suggest a fancy name for this."""
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['name', 'wear'],
        template="""Suggest 10 cool dress types for {name} store where the wear types are {wear}. 
                    Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['wear'],
        output_variables=['name', "items"]
    )

    response = chain({'wear': wear})

    return response
