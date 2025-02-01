from re import Match, findall, fullmatch
from typing import Union, Dict, AnyStr, List, Sequence
from string import ascii_lowercase
from colorama import Fore


def toExp(n: int) -> str:
    """Numero entero a exponente"""
    digits = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(n).translate(digits)


def toSubIndex(n: int) -> str:
    """Numero entero a subindice"""
    digits = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(n).translate(digits)


def ecRepr(coef: Sequence[int]) -> str:
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
            output.append(toExp(len(coef) - i - 1) + " ")

    return "".join(output)


def solsRepr(solutions: Sequence[int]) -> str:
    """Representacion de soluciones"""
    output: str = ""
    for i in range(len(solutions)):
        output += Fore.LIGHTCYAN_EX + \
            f"x{toSubIndex(i+1)} = {Fore.LIGHTGREEN_EX + str(solutions[i])}"
        output += f"{Fore.LIGHTCYAN_EX}, " if i < len(
            solutions) - 1 else f"{Fore.RESET}"
    return output


def extractCoeficients(s: AnyStr) -> Dict[str, int]:
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
