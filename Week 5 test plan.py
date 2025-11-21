"""
week 5 test plan
Test Plan for celsius_to_fahrenheit:
1. Test freezing point: 0C should be 32F.
2. Test boiling point: 100C should be 212F.
3. Test room temperature: 25C should be 77F.
"""


def celsius_to_fahrenheit(Celsius_Temp):
 Fahrenheit = (Celsius_Temp * 9/5) + 32 #formula for conversion having the celsius times by 9/5 then adding 32
 return Fahrenheit

# --- Unit Tests ---
print("Running tests...")
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert celsius_to_fahrenheit(25) == 77
print("All tests passed successfully!")

Celsius_Temp = 25
f_temp = celsius_to_fahrenheit(Celsius_Temp)
print(f"{Celsius_Temp}C is equal to {f_temp}F")

