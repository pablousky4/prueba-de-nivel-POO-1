def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(filtrados)} vehículos con {ruedas} ruedas:")
        for v in filtrados:
            print(f"{type(v).__name__}: {v}")
    else:
        for v in vehiculos:
            print(f"{type(v).__name__}: {v}")
