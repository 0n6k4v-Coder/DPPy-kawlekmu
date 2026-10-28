#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

header = [
    "=============================",
    "=== MY PYTHON APPLICATION ===",
    "============================="
]

menu = {
    1: "Add New Model",
    2: "View All Model",
    3: "Change Current Model",
    4: "Search and Summary",
    5: "Using LLM",
    6: "Exit"
}

models = {
    "Nemotron 3.5 Super": "nvidia/nemotron-3.5-super-vl-120b-a12b"
}

model_id = "nvidia/nemotron-3.5-super-vl-120b-a12b"
model_name = "Nemotron 3.5 Super"

def render(param):
    match param:
        case list():
            for item in param:
                print(item)
        case dict():
            for key, value in param.items():
                print(f'{key}. {value}')

def menu1():
    print('Add new model')

    model_name = input('Model name: ')
    model_id = input('Model ID: ')

    new_model = {model_name: model_id}
    models.update(new_model)

def menu2():
    print('Model List:')
    print(models)

def menu3():
    round = 0

    print('Available models:')
    for i in models:
        print(f'{round}.{i}')
        round += 1

    print

def menu4():
    print('menu 4')

def menu5():
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
            "content": prompt
        }

        completion = client.chat.completions.create(
            model=model_id,
            messages=[message]
        )

        print(f"{model_name}: {completion.choices[0].message.content}")

def menu6():
    print('Goodbye!')
    exit()

def main():
    render(header)
    render(menu)

    prompt = ""

    while True:
        prompt = input("Choose: ")

        match prompt:
            case "1": menu1()
            case "2": menu2()
            case "3": menu3()
            case "4": menu4()
            case "5": menu5()
            case "6": menu6()

main()