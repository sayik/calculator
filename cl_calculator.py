def verify_input(values: str) -> bool:
    operators: list[str] = ["+", "-", "*", "/", "%", "**"]
    for item in list(values):
        if item.isdigit() or item in operators:
            continue
        else:
            return False
    return True


def cli_input() -> None:
    values: str = input("Enter the operation here \n -> ")

    if verify_input(values):
        print(eval(values))
    else:
        print("Please enter digits and signs")


if __name__ == "__main__":
    cli_input()
