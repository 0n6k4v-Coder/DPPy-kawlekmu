#!/usr/bin/env python3

import llm_personal_planning as lpp

def main():
    records = {}

    lpp.render(lpp.HEADER)
    lpp.render(lpp.MENU)

    while True:
        prompt = input("Select a menu: ").strip()
        if prompt == "1":
            records = lpp.add(records)
            print(records)
        elif prompt == "2":
            lpp.render(records)
        elif prompt == "3":
            records= lpp.update(records)
        elif prompt == "4":
            records = lpp.remove(records)
            print(records)
        elif prompt == "5":
            lpp.llm(records)
        elif prompt == "6":
            lpp.exit_program()
        else:
            lpp.render(menu)

main()