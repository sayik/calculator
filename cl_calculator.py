def verify_input(values: str) -> bool:
    operators: list[str] = ["+", "-", "*", "/", "%", "**", "."]
    for item in values:
        if item.isdigit() or item in operators:
            continue
        else:
            return False
    return True


def ui_input(values) -> None:
    # values: str = input("Enter the operation here \n -> ")

    if verify_input(values):
        try:
            return eval(
                str(values)  # if float needs to be calculated, it must be a string.
            )  # Here a wrong input can break program and crash it like "77/"
        except SyntaxError:
            return None
    else:
        return None


if __name__ == "__main__":
    ui_input()
