from solutions.CHK import checkout_solution


class TestChk:
    def test_empty_input(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid_input(self):
        assert checkout_solution.checkout("XAA") == -1
        assert checkout_solution.checkout("A A") == -1

    def test_pricing_for_one_item(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180

    def test_pricing_for_multiple_items(self):
        assert checkout_solution.checkout("AACAA") == 200
        assert checkout_solution.checkout("AACCAA") == 220
        assert checkout_solution.checkout("CAACCAA") == 240
        assert checkout_solution.checkout("CAABCCAA") == 270
        assert checkout_solution.checkout("CAABBCCAA") == 285
        assert checkout_solution.checkout("CAADBBCCAA") == 300
        assert checkout_solution.checkout("CAADBBBCCAA") == 330
