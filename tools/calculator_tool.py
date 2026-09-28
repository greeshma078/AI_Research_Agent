from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Use this tool when the user asks for arithmetic calculations.
    """

    try:
        result = eval(expression)

        return str(result)

    except Exception:
        return "Unable to calculate the expression."

if __name__ == "__main__":

    result = calculator.invoke("250 * 18")

    print("Calculation Result:")
    print(result)