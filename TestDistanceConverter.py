from DistanceConverterFunction import Distance

if __name__ == "__main__":

    converter = Distance()

    #---------------------------
    #--- Cas d’erreur ----------
    #---------------------------

    # Test d’une unité source inconnue
    try:
        converter.convert("XYZ", 100, "m")
        assert False, "Erreur : une exception aurait dû être levée pour une unité source inconnue"
    except KeyError:
        pass  # OK

    # Test d’une unité cible inconnue
    try:
        converter.convert("m", 100, "XYZ")
        assert False, "Erreur : une exception aurait dû être levée pour une unité cible inconnue"
    except KeyError:
        pass  # OK

    #----------------------------
    #--- Cas de conversion ------
    #----------------------------

    # Conversion vers la même unité
    same_unit = converter.convert("m", 100, "m")
    assert same_unit == 100, "Erreur de conversion d’une unité vers elle-même"

    # km vers m
    km_to_m = converter.convert("km", 2, "m")
    assert km_to_m == 2000, "Erreur de conversion de km vers m"

    # m vers km
    m_to_km = converter.convert("m", 500, "km")
    assert m_to_km == 0.5, "Erreur de conversion de m vers km"

    # inch vers cm
    in_to_cm = converter.convert("in", 10, "cm")
    expected_cm = round((10 * 0.0254) / 0.01, 4)
    assert in_to_cm == expected_cm, "Erreur de conversion de inch vers cm"

    # mile vers km
    mi_to_km = converter.convert("mi", 1, "km")
    expected_km = round(1609.344 / 1000, 4)
    assert mi_to_km == expected_km, "Erreur de conversion de mile vers km"

    # année-lumière vers km (test gros nombre)
    ly_to_km = converter.convert("ly", 1, "km")
    expected_km = round((9.4607 * 10**15) / 1000, 4)
    assert ly_to_km == expected_km, "Erreur de conversion de ly vers km"

    # Vérification cohérence interne (mètre = 1)
    assert converter.tab["m"] == 1, "Erreur : le mètre doit être la référence"

    print("Tous les tests sont passés avec succès !")