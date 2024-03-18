def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []
    if n <= 1:
        fibonacci_sequence = [0]
    else:
        a, b = 0, 1
        fibonacci_sequence = [a, b]
        for c in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)
            a, b = b, c
    return fibonacci_sequence


num_terms = int(input("Enter the number of terms: "))


fibonacci_sequence = fibonacci(num_terms)


print("Fibonacci Sequence:")
for term in fibonacci_sequence:
    print(term, end=" ")

