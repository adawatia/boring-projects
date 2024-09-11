# Weight Conversion Application

## Description

This Python application allows users to convert weights between various units: kilograms (`kg`), pounds (`lbs`), ounces (`oz`), grams (`g`), and stones (`st`). It takes user input for weight and its unit, and then provides the equivalent weight in other units.

## Features

- Converts between the following weight units:
  - Kilograms (`kg`)
  - Pounds (`lbs`)
  - Ounces (`oz`)
  - Grams (`g`)
  - Stones (`st`)
  
- Rounds the converted values to three decimal places for clarity.
- Handles invalid numeric input and invalid unit selection.

## Example Usage

1. **Input weight and unit**: The user enters a weight and selects the unit from a predefined list.
2. **Display conversions**: The program displays the equivalent weight in all other units.

### Example

```bash
$ python weight_converter.py

Enter weight: 10

Choose unit:
Kilograms → kg
Pounds → lbs
Ounces → oz
Grams → g
Stones → st

Enter the unit (kg, lbs, oz, g, st): kg

Weight conversions from 10.0 kg:
22.046 lbs
352.74 oz
10000.0 g
1.575 st
```

In this example, the user entered a weight of 10 kilograms. The program provided conversions to pounds, ounces, grams, and stones.

## Code Structure

### `convert_weight(weight, unit)`

This function takes two arguments: `weight` (the numerical value of the weight) and `unit` (the unit in which the weight is provided). It returns a dictionary with equivalent weights in other units, rounded to three decimal places.

#### Conversion Formulas:
- **Kilograms** (`kg`) to other units:
  - Pounds (`lbs`): `weight * 2.20462`
  - Ounces (`oz`): `weight * 35.274`
  - Grams (`g`): `weight * 1000`
  - Stones (`st`): `weight * 0.157473`
  
- **Pounds** (`lbs`) to other units:
  - Kilograms (`kg`): `weight / 2.20462`
  - Ounces (`oz`): `weight * 16`
  - Grams (`g`): `weight * 453.592`
  - Stones (`st`): `weight * 0.071429`
  
- **Ounces** (`oz`) to other units:
  - Kilograms (`kg`): `weight / 35.274`
  - Pounds (`lbs`): `weight / 16`
  - Grams (`g`): `weight * 28.3495`
  - Stones (`st`): `weight * 0.004464`
  
- **Grams** (`g`) to other units:
  - Kilograms (`kg`): `weight / 1000`
  - Pounds (`lbs`): `weight / 453.592`
  - Ounces (`oz`): `weight / 28.3495`
  - Stones (`st`): `weight * 0.000157`
  
- **Stones** (`st`) to other units:
  - Kilograms (`kg`): `weight / 0.157473`
  - Pounds (`lbs`): `weight * 14`
  - Ounces (`oz`): `weight * 224`
  - Grams (`g`): `weight * 6350.29`

### `main()`

This function drives the program:
- Prompts the user for a weight and unit.
- Uses the `convert_weight()` function to calculate and display equivalent weights in other units.
- Handles invalid inputs for both weight and unit selection.

## Installation

1. Ensure you have Python 3.x installed.
2. Clone the repository or download the script to your local machine.
3. Run the program from the terminal:

```bash
python weight_converter.py
```
---
