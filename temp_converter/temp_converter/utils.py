def validate_temperature(value):
    """Valida se o valor da temperatura é um número"""
    if not isinstance(value, (int, float)):
        raise ValueError("O valor da temperatura deve ser um número")
