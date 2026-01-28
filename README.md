# Simple Mathematical Gradient

This project shows how to create a **linear color gradient** between two RGB colors using only basic mathematics and pure Python code.

***

## What it does

- Interpolates between two RGB colors using **linear interpolation**.
- Outputs a list of RGB values that form a smooth gradient.
- Uses no external libraries (only built‑in Python operations).

***

## Requirements

- Python 3.x (no extra packages needed).

***

## How to use

1. Save the following code into a file named `simple_math_gradient.py`:

```python
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
```

2. Run the script:

```bash
python simple_math_gradient.py
```

You will see 10 interpolated RGB values from red `(255, 0, 0)` to blue `(0, 0, 255)` printed to the console.

***

## Math behind it

The core formula is **linear interpolation**:

\[
\text{value}(t) = a(1 - t) + b t
\]

where:
- `a` is the start value,
- `b` is the end value,
- `t` runs from 0 to 1 across the steps.

This formula is applied separately to the red, green, and blue channels.

***

## Customizing

- Change the start and end colors:

  ```python
  red = (255, 0, 0)
  blue = (0, 0, 255)
  ```

- Change the number of steps:

  ```python
  n_steps = 20
  ```

You can plug the resulting RGB list into images, plots, or any other visualization code.
