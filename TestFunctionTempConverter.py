from TemperatureConverterFunction import Temperature

# Tests Unitaires pour la classe Temperature
if __name__ == "__main__":

    # ----------------------------
    # --- Celsius vers ... -------
    # ----------------------------

    # Test de conversion de Celsius vers Fahrenheit
    temp_c = Temperature(25, "celsius")
    assert temp_c.convert_to("fahrenheit") == 77.0, "Erreur de conversion de Celsius vers Fahrenheit"

    # Test de conversion de Celsius vers Kelvin
    temp_c2 = Temperature(0, "celsius")
    assert temp_c2.convert_to("kelvin") == 273.15, "Erreur de conversion de Celsius vers Kelvin"

    # ---------------------------
    # --- Fahrenheit vers ... ---
    # ---------------------------

    # Test de conversion de Fahrenheit vers Kelvin
    temp_f2 = Temperature(32, "fahrenheit")
    assert temp_f2.convert_to("kelvin") == 273.15, "Erreur de conversion de Fahrenheit vers Kelvin"

    # Test de conversion de Fahrenheit vers Celsius
    temp_f = Temperature(77, "fahrenheit")
    assert temp_f.convert_to("celsius") == 25.0, "Erreur de conversion de Fahrenheit vers Celsius"

    # ---------------------------
    # --- Kelvin vers ... -------
    # ---------------------------

    # Test de conversion de Kelvin vers Fahrenheit
    temp_k2 = Temperature(273.15, "kelvin")
    assert temp_k2.convert_to("fahrenheit") == 32.0, "Erreur de conversion de Kelvin vers Fahrenheit"

    # Test de conversion de Kelvin vers Celsius
    temp_k = Temperature(300, "kelvin")
    assert temp_k.convert_to("celsius") == 26.85, "Erreur de conversion de Kelvin vers Celsius"

    # ---------------------------
    # --- Cas d’erreur ----------
    # ---------------------------

    # Test de conversion d’une unité vers elle-même
    temp_c3 = Temperature(100, "celsius")
    assert temp_c3.convert_to("celsius") == 100.0, "Erreur de conversion d’une unité vers elle-même"    

    # Test de gestion d’une unité source inconnue
    try:
        temp_invalid = Temperature(100, "unknown")
        temp_invalid.convert_to("celsius")
        assert False, "Erreur : une exception aurait dû être levée pour une unité source inconnue"
    except ValueError:
        pass # L’exception est attendue, parfait.

    print("Tous les tests sont passés avec succès !")
    