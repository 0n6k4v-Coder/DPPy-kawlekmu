def render(param):
    match param:
        case list():
            for item in param:
                print(item)
        case dict():
            for key, value in param.items():
                print(f'{key} {value}')