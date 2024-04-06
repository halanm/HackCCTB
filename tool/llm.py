from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

import os

_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

class Llm:
    def get_prompt(generator, params) -> str:
        base_str = generator.prompt

        base_str += "\n\nParameters:{context}"
        for param in params:
            base_str += f"\n{param['text']}: {param['value']}"
        return base_str
    
    def get_response(prompt) -> str:
        completion = client.chat.completions.create(
            model=os.environ['OPENAI_MODEL'],
            messages=[
                {"role": "system", "content": "You are an AI built to generate useful contents for users."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
