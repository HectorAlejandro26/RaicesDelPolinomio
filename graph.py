import matplotlib.pyplot as plt
import numpy as np
from typing import Sequence


def graph(coef: Sequence[int], roots: Sequence[int], ranges: int = 1) -> None:
    def f(x):
        res = 0
        for i, c in enumerate(coef):
            res += c * (x ** (len(coef) - i - 1))
        return res

    limMax = max(roots) + ranges
    limMin = min(roots) - ranges
    spacing = ((abs(limMax) + abs(limMin))//4+1) * 100
    print(f"Spacing: {spacing}")

    x = np.linspace(limMin, limMax, spacing, endpoint=True)
    plt.plot(x, f(x), "r-")
    plt.scatter(roots, np.zeros_like(roots), color="blue")
    plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
    plt.axvline(0, color="black", linewidth=0.8, linestyle=":")
    plt.show()
