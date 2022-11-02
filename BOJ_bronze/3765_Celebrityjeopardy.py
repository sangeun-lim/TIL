while True:
    try:
        x = input()
        print(f'{x}')
    except EOFError:
        break