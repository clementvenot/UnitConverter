from WeightConverterFunction import weightConverter

if __name__ == "__main__":

    converter = weightConverter()

    #---------------------------
    #--- Cas d’erreur ----------
    #---------------------------
    # Test d’une unité source inconnue
    try:
        converter.convert("XYZ", 100, "g")
        assert False, "Erreur : une exception aurait dû être levée pour une unité source inconnue"
    except KeyError:
        pass  # L’exception est attendue, parfait.

    # Test d’une unité cible inconnue
    try:
        converter.convert("g", 100, "XYZ")
        assert False, "Erreur : une exception aurait dû être levée pour une unité cible inconnue"
    except KeyError:
        pass  # L’exception est attendue, parfait.

    #----------------------------
    #--- Cas de conversion ------
    #----------------------------

    # Test de conversion d’une unité vers elle-même
    same_unit = converter.convert("g", 100, "g")
    assert same_unit == 100, "Erreur de conversion d’une unité vers elle-même"

    # Test de conversion de kg vers g
    kg_to_g = converter.convert("kg", 40, "g")
    assert kg_to_g == 40000, "Erreur de conversion de kg vers g"

    # Test de conversion de g vers t (arrondi à 4 décimales)
    g_to_t = converter.convert("g", 40, "t")
    assert g_to_t == 0.0, "Erreur de conversion de g vers t"

    # Test de conversion de t vers oz
    t_to_oz = converter.convert("t", 400, "oz")
    expected_oz = round(400000000 / 28.3495, 4)
    assert t_to_oz == expected_oz, "Erreur de conversion de t vers oz"

    # Test de conversion de lb vers kg
    lb_to_kg = converter.convert("lb", 1, "kg")
    expected_kg = round(453.592 / 1000, 4)
    assert lb_to_kg == expected_kg, "Erreur de conversion de lb vers kg"

    # Test d’équivalence entre Da et u
    assert converter.tab["Da"] == converter.tab["u"], "Erreur : Da et u devraient être équivalents"

    print("Tous les tests sont passés avec succès !")
