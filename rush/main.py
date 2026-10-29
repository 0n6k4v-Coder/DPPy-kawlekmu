#!/usr/bin/env python3

import os
from openai import OpenAI

HEADER = [
    "=============================",
    "=== MY PYTHON APPLICATION ===",
    "============================="
]

MENU = {
    "1.": "Add new task",
    "2.": "View all tasks",
    "3.": "Update task",
    "4.": "Remove task",
    "5.": "Summarize by LLM",
    "6.": "Exit"
}

def render(param):
    match param:
        case list():
            for item in param:
                print(item)
        case dict():
            for key, value in param.items():
                print(f'{key} {value}')

def add(records):    
    key = input('Key: ')
    value = input('Value: ')

    if key != None and value != None:
        records.update({key: value})

    return records

def view(records):
    print(records)

def update(records):
    return records

def remove(records):
    key = input('Insert Key: ')
    records.pop(key)

    return records

def llm(records):
    while True:
        prompt = input("You: ")

        if prompt == "/exit":
            print('Conversation End')
            break

        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.getenv("NVIDIA_API_KEY")
        )

        response = client.responses.create(
            model="nvidia/nemotron-3.5-super-vl-120b-a12b",
            input= (
                f'Ground truth only on data in this records: {records}'
                f'user prompt: {prompt}'
            )
        )

        print("AI:", response.output_text)

def exit_program():
    print('Goodbye!')
    exit()

def main():
    records = {}

    render(HEADER)
    render(MENU)

    while True:
        prompt = input("Select a menu: ").strip()
        if prompt == "1":
            records = add(records)
            print(records)
        elif prompt == "2":
            render(records)
        elif prompt == "3":
            records= update(records)
        elif prompt == "4":
            records = remove(records)
            print(records)
        elif prompt == "5":
            llm(records)
        elif prompt == "6":
            exit_program()
        else:
            render(MENU)

main()