def is_fever(temp: str) -> bool:
    # Get the last character (unit: F or C)
    unit = temp[-1].upper()
    # Convert the number part into a float
    value = float(temp[:-1])
    
    # Check based on unit
    if unit == "F":
        return value > 98.6
    elif unit == "C":
        return value > 37
    else:
        raise ValueError("Invalid temperature unit. Must be 'F' or 'C'.")

# Examples:
print(is_fever("99F"))   # True
print(is_fever("37C"))   # False
print(is_fever("98F"))   # False
