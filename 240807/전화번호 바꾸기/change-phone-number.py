number = input()

parts = number.split('-')

if len(parts) == 3 and parts[0] == '010':
    swapped = f"{parts[0]}-{parts[2]}-{parts[1]}"
    print(swapped)