def convert_weight(weight, unit):
    if unit == 'kg':
        return {
            'lbs': round(weight * 2.20462, 3),
            'oz': round(weight * 35.274, 3),
            'g': round(weight * 1000, 3),
            'st': round(weight * 0.157473, 3)
        }
    elif unit == 'lbs':
        return {
            'kg': round(weight / 2.20462, 3),
            'oz': round(weight * 16, 3),
            'g': round(weight * 453.592, 3),
            'st': round(weight * 0.071429, 3)
        }
    elif unit == 'oz':
        return {
            'kg': round(weight / 35.274, 3),
            'lbs': round(weight / 16, 3),
            'g': round(weight * 28.3495, 3),
            'st': round(weight * 0.004464, 3)
        }
    elif unit == 'g':
        return {
            'kg': round(weight / 1000, 3),
            'lbs': round(weight / 453.592, 3),
            'oz': round(weight / 28.3495, 3),
            'st': round(weight * 0.000157, 3)
        }
    elif unit == 'st':
        return {
            'kg': round(weight / 0.157473, 3),
            'lbs': round(weight * 14, 3),
            'oz': round(weight * 224, 3),
            'g': round(weight * 6350.29, 3)
        }
    else:
        return None

def main():
    try:
        weight = float(input("Enter weight: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    print("""
    Choose unit:
    Kilograms → kg
    Pounds → lbs
    Ounces → oz
    Grams → g
    Stones → st
    """)
    
    unit = input("Enter the unit (kg, lbs, oz, g, st): ").strip().lower()
    
    if unit not in ('kg', 'lbs', 'oz', 'g', 'st'):
        print("Invalid unit. Please enter a valid unit.")
        return
    
    converted_weights = convert_weight(weight,unit)
    
    if converted_weights:
        print(f"Weight conversions from {weight} {unit}:")
        for u, val in converted_weights.items():
            print(f"{val} {u}")
    else:
        print("Something went wrong with the conversion.")
    
if __name__ == "__main__":
    main()
