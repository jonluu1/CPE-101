def poly_add2(poly1, poly2):
    return [poly1[0] + poly2[0], poly1[1] + poly2[1], poly1[2] + poly2[2]]

def poly_mult2(poly1, poly2):
    a = poly1[0]
    b = poly1[1]
    c = poly1[2]

    d = poly2[0]
    e = poly2[1]
    f = poly2[2]

    return [a*d, a*e + b*d, a*f + b*e + c*d, b*f + c*e, c*f]