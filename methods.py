from typing import Sequence, List, Union


def ruffini(coefs: Sequence[int], r) -> Sequence[int]:
    """Aplica la division de ruffini y retorna la expresion reducida."""
    new_c = [coefs[0]]
    for i in range(1, len(coefs)):
        new_c.append(new_c[-1] * r + coefs[i])

    if new_c[-1] == 0:
        return new_c[:-1]
    else:
        return None


def general_eq(coefs: Sequence[int], cmplx: bool = False) -> Union[List[Union[float, complex]], None]:
    """Calcula la ecuacion general para los 3 coeficientes dados."""
    assert len(coefs) == 3
    a, b, c = coefs
    sqrt = (b**2 - 4 * a * c) ** 0.5
    d = 2 * a
    r1 = (-b + sqrt) / d
    r2 = (-b - sqrt) / d

    r = []

    if not isinstance(r1, complex):
        r.append(r1)
    elif cmplx:
        r.append(r1)

    if not isinstance(r2, complex):
        r.append(r2)
    elif cmplx:
        r.append(r2)

    return r if r else None


def find_roots(coefs: Sequence[int]) -> List[Union[int, float]]:
    """Funcion que aplica los metodos vistos en clase"""
    assert len(coefs) > 1, "La ecuacion es constante."

    # * En caso de ser lineal
    if len(coefs) == 2:
        return [-coefs[1] / coefs[0]]

    last_coef = coefs[-1]

    # * Busca los divisores del ultimo coeficiente
    divisors = [d for d in range(-abs(last_coef), abs(last_coef) + 1)
                if d != 0 and last_coef % d == 0]

    roots: List[Union[int, float]] = list()
    # * Se reduce la ecuacion hasta que sea una funcion cuadratica
    while len(coefs) > 2:
        # * Control para evitar atascamientos
        finded = False
        for d in divisors:
            # * Se almacena la ecuacion reducida
            new_c = ruffini(coefs, d)
            if new_c:
                # * Guardar la raiz encontrada
                roots.append(d)

                # * Se remplaza la ecuacion anterior con la reducida
                coefs = new_c
                finded = True
                break

            # * Aplicar formula general en caso de cuadratica
        if len(coefs) == 3:
            gnrl_eq_res = general_eq(coefs, False)
            if gnrl_eq_res is not None:
                roots.extend(gnrl_eq_res)
            break

        if not finded:
            break  # ? no se encontraron mas

    roots.sort()  # ? Simple presentacion
    return list(set(roots))  # ? Conversion por si existen duplicados
