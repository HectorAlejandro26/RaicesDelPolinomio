import matplotlib.pyplot as plt
import numpy as np
from typing import Sequence


def graph(coef: Sequence[int], roots: Sequence[int]) -> None:
    def f(x):
        res = 0
        for c in range(len(coef)):
            res += coef[c] * (x ** (len(coef) - c))
        return res

    limMax = max(roots) + 1
    limMin = min(roots) - 1
    spacing = ((abs(limMax) + abs(limMin))//4+1) * 100
    print(f"Spacing: {spacing}")

    x = np.linspace(limMin, limMax, spacing, endpoint=True)
    plt.plot(x, f(x), "r-")
    plt.scatter(roots, np.zeros_like(roots), color="blue")
    plt.scatter(0, 0, color="black")
    plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
    plt.axvline(0, color="black", linewidth=0.8, linestyle=":")
    plt.show()
