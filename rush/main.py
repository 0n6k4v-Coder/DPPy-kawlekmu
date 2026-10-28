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
    1: "Add new task",
    2: "View all tasks",
    3: "Update task",
    4: "Remove task",
    5: "Using LLM",
    6: "Exit"
}

task_planning = {}

def render(param):
    match param:
        case list():
            for item in param:
                print(item)
        case dict():
            for key, value in param.items():
                print(f'{key}. {value}')

def menu1():
    print('menu 1')

def menu2():
    print('menu 2')

def menu3():
    print('menu 3')

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
            model="nvidia/nemotron-3.5-super-vl-120b-a12b",
            messages=[message]
        )

        print("AI:", completion.choices[0].message.content)

def menu6():
    print('Goodbye!')
    exit()

def main():
    prompt = ""

    while True:
        render(header)
        render(menu)
        prompt = input("Select a menu: ")
        match prompt:
            case "1": menu1()
            case "2": menu2()
            case "3": menu3()
            case "4": menu4()
            case "5": menu5()
            case "6": menu6()

main()