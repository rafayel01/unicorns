
lst = []
while True:
    inp = input("Enter a number: ")
    if inp.isdigit():
        lst.append(int(inp))
    elif inp == 'done':
        break
    else:
        print("Invalid input")

print(sum(lst), len(lst), sum(lst) / len(lst))
