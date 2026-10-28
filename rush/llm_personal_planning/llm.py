import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def llm(records):
    while True:
        prompt = input("You: ")

        if prompt == "/exit":
            print('Conversation End')
            break

        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.environ["NVIDIA_API_KEY"]
        )

        message = {
            "role": "user",
            "content": f'Ground truth only on data in this records: {records} user prompt: {prompt}'
        }

        completion = client.chat.completions.create(
            model="nvidia/nemotron-3.5-super-vl-120b-a12b",
            messages=[message]
        )

        print("AI:", completion.choices[0].message.content)