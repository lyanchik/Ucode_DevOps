# ax^{2}+bx+c=0  D=b^{2}-4ac
import json
import math


def quad(a, b, c):  # If arguments is'nt int or float & a!=0
    if a != 0 and isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        a_str, b_str, c_str = str(a), str(b), str(c)
        d = ((b ** 2) - (4 * a * c))
        if d < 0:
            sum_x = None
        elif d == 0:
            if b == 0:
                sum_x = float(0)
            else:
                sum_x = (-b / (2 * a))
        elif d > 0:
            x1 = float(round((-b - math.sqrt(d)) / (2 * a), 3))
            x2 = float(round((-b + math.sqrt(d)) / (2 * a), 3))
            sum_x = [x1, x2]
            sum_x.sort()

        if a > 1 or a < -1:
            quad_coef = a_str + 'x^2'
        elif a == 1:
            quad_coef = 'x^2'
        elif a == -1:
            quad_coef = '-x^2'

        if b == 0:
            lin_coef = ''
        elif 0 < b < 1 or b > 1:
            lin_coef = '+' + b_str + 'x'
        elif b == 1:
            lin_coef = '+' + b_str + 'x'
        elif 0 > b > -1 or b < -1:
            lin_coef = b_str + 'x'
        elif b == -1:
            lin_coef = '-x'

        if c == 0:
            const = ''
        elif c > 0:
            const = '+' + c_str
        elif c < 0:
            const = c_str
        quad_ecuation = quad_coef + lin_coef + const + '=0'
        # The resulting object must have two fields: "equation" and "solution".
        res_obj = {'equation': quad_ecuation, 'solution': {'discriminant': round(float(d), 3), 'x': sum_x}}
        return json.dumps(res_obj, indent=3)  # JSON string with info quadratic equation with these values.
    else:
        return f'Cannot generate a quadratic equation.'
