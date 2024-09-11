def temp_converter(temperature, unit):
    if unit == 'C':
        fahrenheit = round((temperature * 9/5) + 32, 2)
        kelvin = round(temperature + 273.15, 2)
        return f"{temperature}°C = {fahrenheit}°F, {kelvin}K"
    elif unit == 'F':
        celsius = round((temperature - 32) * 5/9, 2)
        kelvin = round((temperature - 32) * 5/9 + 273.15, 2)
        return f"{temperature}°F = {celsius}°C, {kelvin}K"
    elif unit == 'K':
        celsius = round(temperature - 273.15, 2)
        fahrenheit = round((temperature - 273.15) * 9/5 + 32, 2)
        return f"{temperature}K = {celsius}°C, {fahrenheit}°F"
    else:
        return "Enter a valid unit (C for Celsius, F for Fahrenheit, K for Kelvin)."

def main():
    try:
        temperature = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid input. Please enter numerical values only.")
        return  # Stops execution if input is invalid
    
    unit = input("Choose temperature unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
    
    result = temp_converter(temperature, unit)
    print(result)

if __name__ == "__main__":
    main()
