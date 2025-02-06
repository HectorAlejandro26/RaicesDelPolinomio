from methods import find_roots
from pretty_functions import extract_coeficients, eq_repr, graph, sols_repr
from colorama import Fore as F
from typing import List


def main() -> int:
    """Programa principal"""
    ecStr: str = input(
        f"{F.BLUE}Ingrese una ecuación:\n\
{F.YELLOW}Ej. {F.YELLOW}\"{F.LIGHTCYAN_EX}1, 2, 3{F.YELLOW}\" -> \"{F.LIGHTCYAN_EX}x² + 2x + 3{F.YELLOW}\"\n\
{F.LIGHTGREEN_EX}>> {F.LIGHTCYAN_EX}")
    print(F.RESET)
    # ecStr: str = "1 -1 -4 4"

    coefs: List[int] = list(extract_coeficients(ecStr).values())

    roots = find_roots(coefs)
    print(f"{F.BLUE}La ecuación:\n{F.LIGHTRED_EX + eq_repr(coefs)}")
    if not roots:
        print(F.RED + "No tiene soluciones.")

    else:
        print(F.BLUE + f"Tiene {len(roots)} solución(es):\n\
{sols_repr(roots)}")
        graph(coefs, roots)

        print(F.RESET, end="")

    return 0


def __main_test__():
    a = [2, 9, 13, 6]
    b = [1, 0, -3]
    c = [1, 1, -2, -1, 1]
    print(find_roots(c))


if __name__ == "__main__":
    exit(main())
