#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def render(content):
    match content:
        case list():
            for line in content:
                print(line)
        case dict():
            for name, status in content.items():
                print(f'{name}: {status}')
        case str():
            print(f'\n============ {content} ===========\n')


def get_input(message):
    user_input = input(f'{message} (/cancel to return): ').strip()

    if user_input == '/cancel':
        return None

    return user_input


def add(records):
    render('1. Add new task')

    task_name = get_input('Task name')
    if task_name is None:
        return

    task_status = get_input('Task status')
    if task_status is None:
        return

    if not task_name:
        print('Task name cannot be empty.')
    elif task_name in records:
        print('Task already exists.')
    elif not task_status:
        print('Task status cannot be empty.')
    else:
        records[task_name] = task_status
        print('Task added.')


def view(records):
    render('2. View all tasks')

    if not records:
        print('No tasks found.')
    else:
        render(records)


def update(records):
    render('3. Update task')

    task_name = get_input('Task name')
    if task_name is None:
        return

    if task_name not in records:
        print('Task not found.')
    else:
        task_status = get_input('New status')
        if task_status is None:
            return

        if task_status:
            records[task_name] = task_status
            print('Task updated.')
        else:
            print('Status cannot be empty.')


def remove(records):
    render('4. Remove task')

    task_name = get_input('Task name')
    if task_name is None:
        return

    if task_name in records:
        records.pop(task_name)
        print('Task removed.')
    else:
        print('Task not found.')


def search(records):
    render('5. Search tasks')

    keyword = get_input('Search task')
    if keyword is None:
        return

    keyword = keyword.lower()
    found_task = False

    for task_name, task_status in records.items():
        if keyword and keyword in task_name.lower():
            print(f'{task_name}: {task_status}')
            found_task = True

    if not found_task:
        print('No matching tasks found.')


def summary(records):
    render('6. Summarize tasks')

    print(f'Total tasks: {len(records)}')

    for task_status in set(records.values()):
        print(
            f'{task_status}: '
            f'{list(records.values()).count(task_status)}'
        )


def llm(records):
    render('7. Summarize by LLM')

    client = OpenAI(
        base_url='https://integrate.api.nvidia.com/v1',
        api_key=os.getenv('NVIDIA_API_KEY')
    )

    while True:
        user_prompt = get_input('You')

        if user_prompt is None:
            break

        if not user_prompt:
            print('Please enter a question.')
            continue

        response = client.responses.create(
            model='nvidia/nemotron-3.5-super-vl-120b-a12b',
            input=(
                f'Use only these task records: {records}\n'
                f'User prompt: {user_prompt}'
            )
        )

        print('AI:', response.output_text)


def exit_program():
    goodbye_art = [
        r"                                            ",
        r"                                            ",
        r"     ██████╗  ██████╗  ██████╗ ██████╗      ",
        r"    ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗     ",
        r"    ██║  ███╗██║   ██║██║   ██║██║  ██║     ",
        r"    ██║   ██║██║   ██║██║   ██║██║  ██║     ",
        r"    ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝     ",
        r"     ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝      ",
        r"                                            ",
        r"           THANKS FOR PLAYING!              ",
        r"            SEE YOU NEXT TIME!              ",
        r"                                            ",
        r"                                            "
    ]

    render(goodbye_art)


def main():
    records = {}

    header_art = [
        r"╔══════════════════════════════════════════╗",
        r"║                                          ║",
        r"║    ██████╗ ██╗   ██╗███████╗██╗  ██╗     ║",
        r"║    ██╔══██╗██║   ██║██╔════╝██║  ██║     ║",
        r"║    ██████╔╝██║   ██║███████╗███████║     ║",
        r"║    ██╔══██║██║   ██║╚════██║██╔══██║     ║",
        r"║    ██║  ██║╚██████╔╝███████║██║  ██║     ║",
        r"║    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     ║",
        r"║            R U S H   H O U R             ║",
        r"║                                          ║",
        r"╚══════════════════════════════════════════╝"
    ]

    menu_items = {
        '1': 'Add new task',
        '2': 'View all tasks',
        '3': 'Update task',
        '4': 'Remove task',
        '5': 'Search tasks',
        '6': 'Summarize tasks',
        '7': 'Summarize by LLM',
        '8': 'Exit'
    }

    render(header_art)

    while True:
        render('MENU')
        render(menu_items)

        choice = input('\nSelect a menu: ').strip()

        if choice == '1':
            add(records)
        elif choice == '2':
            view(records)
        elif choice == '3':
            update(records)
        elif choice == '4':
            remove(records)
        elif choice == '5':
            search(records)
        elif choice == '6':
            summary(records)
        elif choice == '7':
            llm(records)
        elif choice == '8':
            exit_program()
            break
        else:
            print('Invalid menu choice.')


if __name__ == '__main__':
    main()
