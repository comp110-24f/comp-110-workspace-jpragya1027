def get_first(input: list[str]) -> str:
    """Return first element"""
    #Return first element

    return input[0]

def remove_first(input:list[str]) -> None:
    """Remove first element"""
    # Remove first element

    input.pop(0)

def get_and_remove_first(input: list[str]) -> str:
    """Remove AND return first element"""
    #Remove AND return first element

    first_elem: str = input[0]
    input.pop(0)
    return first_elem