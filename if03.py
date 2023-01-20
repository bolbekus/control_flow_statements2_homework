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
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if b > c:
            print(b)
        else: 
            print(c)
    return print

print(main(3,7,1))