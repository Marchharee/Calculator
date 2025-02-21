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