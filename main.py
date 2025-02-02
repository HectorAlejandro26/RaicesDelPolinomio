from typing import Dict, List
from functions import extractCoeficients, ecRepr, solsRepr
from colorama import Fore
from graph import graph


def find_roots(coef: List[int]) -> List[int]:
    """Encuentra las raíces enteras de un polinomio."""
    if not coef:
        return []

    last_coef = coef[-1]
    if last_coef == 0:
        return [0]

    divisors = [div for div in range(
        1, abs(last_coef) + 1) if last_coef % div == 0]
    divisors.extend([-div for div in divisors])
    divisors.sort()

    roots = []
    for d in divisors:
        aux = coef[0]
        for c in coef[1:]:
            aux = aux * d + c
        if aux == 0:
            roots.append(d)
    return roots


def main() -> int:
    """Programa principal"""
    ecStr: str = input(
        f"{Fore.BLUE}Ingrese una ecuación:\n\
{Fore.YELLOW}Ej. {Fore.YELLOW}\"{Fore.LIGHTCYAN_EX}1, 2, 3{Fore.YELLOW}\" -> \"{Fore.LIGHTCYAN_EX}x² + 2x + 3{Fore.YELLOW}\"\n\
{Fore.LIGHTGREEN_EX}>> {Fore.LIGHTCYAN_EX}")
    print(Fore.RESET)
    # ecStr: str = "1 -1 -4 4"

    try:
        coefDict: Dict[str, int] = extractCoeficients(ecStr)
        coef: List[int] = list(coefDict.values())

        roots = find_roots(coef)

        print(f"{Fore.BLUE}La ecuación:\n{Fore.LIGHTRED_EX + ecRepr(coef)}")
        if not roots:
            print(Fore.RED + "No tiene soluciones.")

        else:
            print(Fore.BLUE + f"Tiene {len(roots)} solución(es):\n\
{solsRepr(roots)}")
            graph(coef, roots)

        print(Fore.RESET, end="")

    except Exception as e:
        print(f"Error: {Fore.RED + str(e) + Fore.RESET}.")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
