def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a >= b and a >= c:
        print(a)

    if b >= a and b >= c:
        print(b)

    if c >= a and c >= b:
        print(c)

    return print

print(main(3,7,1))

    
