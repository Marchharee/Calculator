import math
def calculate(expression):
    
    expression = expression.replace('π', str(math.pi))
    
    # add scientific functions
    if 'sin' in expression:
        value = float(expression.replace('sin', '').strip('() '))
        return round(math.sin(math.radians(value)), 4)
    elif 'cos' in expression:
        value = float(expression.replace('cos', '').strip('() '))
        return round(math.cos(math.radians(value)), 4)
    elif 'tan' in expression:
        value = float(expression.replace('tan', '').strip('() '))
        return round(math.tan(math.radians(value)), 4)
    elif 'arcsin' in expression:
        value = float(expression.replace('arcsin', '').strip('() '))
        return round(math.degrees(math.asin(value)), 4)
    elif 'arccos' in expression:
        value = float(expression.replace('arccos', '').strip('() '))
        return round(math.degrees(math.acos(value)), 4)
    elif 'arctan' in expression:
        value = float(expression.replace('arctan', '').strip('() '))
        return round(math.degrees(math.atan(value)), 4)
    elif '^' in expression:
        base, exponent = expression.split('^')
        return round(float(base.strip()) ** float(exponent.strip()), 4)
    elif 'sqrt' in expression:
        value = float(expression.replace('sqrt', '').strip('() '))
        return round(math.sqrt(value), 4)
    elif 'x^2' in expression:
        value = float(expression.replace('x^2', '').strip('() '))
        return round(value ** 2, 4)
    elif 'inv' in expression:
        value = float(expression.replace('inv', '').strip('() '))
        return round(1 / value, 4)
    elif 'fact' in expression:
        value = int(expression.replace('fact', '').strip('() '))
        return round(math.factorial(value), 4)