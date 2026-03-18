from CurrencyConverterFunction import Currency

if __name__ == "__main__":

    #---------------------------
    #--- Cas d’erreur ----------
    #---------------------------
    # Test de gestion d’une monnaie source inconnue
    try:
        invalid_currency = Currency(100, "XYZ")
        invalid_currency.convert_to("USD")
        assert False, "Erreur : une exception aurait dû être levée pour une monnaie source inconnue"
    except ValueError:
        pass # L’exception est attendue, parfait.   

    # Test de gestion d’une monnaie cible inconnue
    try:
        amount = Currency(100, "USD")
        amount.convert_to("XYZ")
        assert False, "Erreur : une exception aurait dû être levée pour une monnaie cible inconnue"
    except ValueError:
        pass # L’exception est attendue, parfait.

    #----------------------------
    #--- Cas de conversion ------
    #----------------------------   

    # Test de conversion d’une monnaie vers elle-même
    amount_same = Currency(100, "USD")
    assert amount_same.convert_to("USD") == 100.0, "Erreur de conversion d’une monnaie vers elle-même"  

    # Test de conversion de USD vers EUR
    amount_usd = Currency(100, "USD")
    converted_eur = amount_usd.convert_to("EUR")
    expected_eur = round(100 * Currency.rates["USD"] / Currency.rates["EUR"], 2)
    assert converted_eur == expected_eur, "Erreur de conversion de USD vers EUR"   

    # Test de conversion de EUR vers ALL 
    amount_eur = Currency(100, "EUR")
    converted_all = amount_eur.convert_to("ALL")
    expected_all = round(100 * Currency.rates["EUR"] / Currency.rates["ALL"], 2)
    assert converted_all == expected_all, "Erreur de conversion de EUR vers ALL"

    print("Tous les tests sont passés avec succès !")


