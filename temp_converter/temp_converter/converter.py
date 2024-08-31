def celsius_to_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Converte Celsius para Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Converte Kelvin para Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Converte Fahrenheit para Kelvin"""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Converte Kelvin para Fahrenheit"""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))
