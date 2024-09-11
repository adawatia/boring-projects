# Temperature Converter

## Description

This Python application allows users to convert temperatures between Celsius (`C`), Fahrenheit (`F`), and Kelvin (`K`). It takes user input for a temperature value and its unit, then converts the value into the other two units.

## Features

- **Supported Conversions**:
  - **Celsius** (`C`) to Fahrenheit (`F`) and Kelvin (`K`)
  - **Fahrenheit** (`F`) to Celsius (`C`) and Kelvin (`K`)
  - **Kelvin** (`K`) to Celsius (`C`) and Fahrenheit (`F`)
  
- **Rounding**: Conversion results are rounded to two decimal places.
- **Input Validation**: Handles invalid input for both temperature values and unit choices.

## Example Usage

1. **Input Temperature and Unit**: The user enters a temperature value and selects a unit.
2. **Output Converted Temperatures**: The program outputs equivalent temperatures in other units.

### Example

```bash
$ python temp_converter.py

Enter temperature: 100
Choose temperature unit (C for Celsius, F for Fahrenheit, K for Kelvin): F
100.0°F = 37.78°C, 310.93K
```

In this example, the user entered a temperature of `100°F`. The program provided the equivalent temperatures in Celsius and Kelvin.

## Code Structure

### `temp_converter(temperature, unit)`

This function performs the temperature conversion. It takes two arguments:
1. **`temperature`**: The numerical value of the temperature.
2. **`unit`**: The unit of the temperature (`C`, `F`, `K`).

It returns the converted values as a string, formatted with two decimal places.

#### Conversion Formulas:
- **Celsius (`C`) to Fahrenheit (`F`)**: `(C * 9/5) + 32`
- **Celsius (`C`) to Kelvin (`K`)**: `C + 273.15`
- **Fahrenheit (`F`) to Celsius (`C`)**: `(F - 32) * 5/9`
- **Fahrenheit (`F`) to Kelvin (`K`)**: `(F - 32) * 5/9 + 273.15`
- **Kelvin (`K`) to Celsius (`C`)**: `K - 273.15`
- **Kelvin (`K`) to Fahrenheit (`F`)**: `(K - 273.15) * 9/5 + 32`

### `main()`

This function handles user interaction:
- **Input**: Prompts the user to enter a temperature value and select the unit.
- **Validation**: Ensures the input values are valid.
- **Output**: Calls `temp_converter()` to calculate and display the converted temperatures.

## Installation

1. Ensure Python 3.x is installed.
2. Download or clone the script to your local machine.
3. Run the program from the terminal:

``` bash

python temp_converter.py

```
---
