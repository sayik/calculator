import ast


def verify_input(values: str) -> bool:
    """
    Verify if the input string contains only digits and valid operators.

    Args:
        values (str): The input string to verify.

    Returns:
        bool: True if valid, False otherwise.
    """
    valid_operators = {"+", "-", "*", "/", "%", "**"}
    for char in values:
        if not (char.isdigit() or char in valid_operators):
            return False
    return True


def evaluate_expression(expression: str) -> float | None:
    """
    Safely evaluate a mathematical expression.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        float | None: The result of the expression, or None if evaluation fails.
    """
    # try:
    #     # Safely parse and evaluate the expression
    #     result = ast.literal_eval(expression)
    #     if isinstance(result, (int, float)):
    #         return result
    # except (SyntaxError, ValueError):
    #     return None
    # return None
    return ast.literal_eval(expression)


def ui_input() -> None:
    """
    Handle user input, verify it, and evaluate the mathematical expression.
    """
    values = input("Enter the operation here (e.g., 5 + 3):\n -> ")
    if not verify_input(values):
        print(
            "Invalid input. Please use only digits and valid operators (+, -, *, /, %, **)."
        )
        return

    result = evaluate_expression(values)
    if result is None:
        print("Error evaluating the expression. Please check your syntax.")
    else:
        print(f"The result is: {result}")


if __name__ == "__main__":
    ui_input()
