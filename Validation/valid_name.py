def validate_name(name: str) -> bool:
    if not name:
        return False
    return name.replace(" ", "").isalpha()
