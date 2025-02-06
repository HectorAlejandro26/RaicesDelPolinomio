from re import Match, findall, fullmatch
from typing import Union, Dict, AnyStr, List, Sequence
from string import ascii_lowercase
from colorama import Fore
from math import floor, ceil
import matplotlib.pyplot as plt
import numpy as np


def to_exp(n: int) -> str:
    """Numero entero a exponente"""
    digits = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(n).translate(digits)


def to_subindex(n: int) -> str:
    """Numero entero a subindice"""
    digits = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(n).translate(digits)


def eq_repr(coef: Sequence[int]) -> str:
    """Representacion de ecuacion"""
    output = []

    for i in range(len(coef)):
        if coef[i] == 0:
            continue

        # Signo
        if i > 0:
            output.append("- " if coef[i] < 0 else "+ ")

        # Coeficiente
        if abs(coef[i]) != 1 or i == len(coef) - 1:
            output.append(str(abs(coef[i])))

        # Variable
        if i < len(coef) - 1:
            output.append("x")

        # Exponente
        if i < len(coef) - 2:
            output.append(to_exp(len(coef) - i - 1) + " ")
        elif i < len(coef) - 1:
            output.append(" ")

    return "".join(output)


def sols_repr(solutions: Sequence[int]) -> str:
    """Representacion de soluciones"""
    output: str = ""
    for i in range(len(solutions)):
        output += Fore.LIGHTCYAN_EX + \
            f"x{to_subindex(i+1)} = {Fore.LIGHTGREEN_EX}"
        output += f"{solutions[i]:.0f}" if solutions[i] % 1 == 0 else f"{
            solutions[i]:.5f}"
        output += f"{Fore.LIGHTCYAN_EX}, " if i < len(
            solutions) - 1 else f"{Fore.RESET}"
    return output


def extract_coeficients(s: AnyStr) -> Dict[str, int]:
    """Extrae coeficientes de la ecuacion"""
    # ? El formato es correcto.
    match: Union[Match, None] = fullmatch(
        r"^(?:-?\d+(?:\s|\,)*){2,26}$",
        s
    )

    if match is None:
        raise SyntaxError("Formato invalido")

    # ? Exctracción de: a, b, c, d, ..., z.
    nums: List[int] = list(
        map(
            int,
            findall(
                r"-?\d+",
                s
            )
        )
    )

    return {k: v for k, v in zip(ascii_lowercase, nums)}


def graph(coef: Sequence[int], roots: Sequence[Union[int, float]], ranges: int = 1) -> None:
    def f(x):
        res = 0
        for i, c in enumerate(coef):
            res += c * (x ** (len(coef) - i - 1))
        return res

    limMax = floor(max(roots)) + ranges
    limMin = ceil(min(roots)) - ranges
    spacing = ((abs(limMax) + abs(limMin))//4+1) * 100
    # print(f"Spacing: {spacing}")

    x = np.linspace(limMin, limMax, spacing, endpoint=True)
    plt.plot(x, f(x), "r-")
    plt.scatter(roots, np.zeros_like(roots), color="blue")
    plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
    plt.axvline(0, color="black", linewidth=0.8, linestyle=":")
    plt.show()
