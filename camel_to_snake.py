def camel_to_snake(name):
    snake = ""
    for char in name:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

def main():
    camel_case = input("Enter something in camel case: ")
    snake_case = camel_to_snake(camel_case)
    print("converted to snake case: ", snake_case)

if __name__ == "__main__":
    main()