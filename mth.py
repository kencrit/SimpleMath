# simple_math_gradient.py

def lerp(a, b, t):
    """Linear interpolation: value between a and b at parameter t ∈ [0,1]."""
    return a * (1 - t) + b * t


def gradient_2colors(c1, c2, n):
    """Interpolate between two RGB tuples over n steps."""
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    gradient = []
    for i in range(n):
        t = i / (n - 1) if n > 1 else 0
        r = int(lerp(r1, r2, t))
        g = int(lerp(g1, g2, t))
        b = int(lerp(b1, b2, t))
        gradient.append((r, g, b))
    return gradient


def main():
    # Start and end colors (RGB)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    # Number of steps in the gradient
    n_steps = 10

    # Compute gradient
    grad = gradient_2colors(red, blue, n_steps)

    # Print results
    print("Linear RGB gradient (red → blue):")
    for i, rgb in enumerate(grad):
        print(f"  step {i:2d}: RGB{rgb}")


if __name__ == "__main__":
    main()
