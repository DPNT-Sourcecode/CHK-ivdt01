from solutions.CHK import checkout_solution


class TestChk:
    def test_empty_input(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid_input(self):
        assert checkout_solution.checkout("XAA") == -1
        assert checkout_solution.checkout("A A") == -1

    def test_pricing_for_single_item(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10

    def test_pricing_for_one_item(self):
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBBBB") == 120
        assert checkout_solution.checkout("BBBBBB") == 135
    
    def test_pricing_for_multiple_items(self):
        assert checkout_solution.checkout("AACAA") == 200
        assert checkout_solution.checkout("AACCAA") == 220
        assert checkout_solution.checkout("CAACCAA") == 240
        assert checkout_solution.checkout("CAABCCAA") == 270
        assert checkout_solution.checkout("CAABBCCAA") == 285
        assert checkout_solution.checkout("CAADBBCCAA") == 300
        assert checkout_solution.checkout("CAADBBBCCAA") == 330

    def test_pricing_for_a_s_special_offers(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("AAAAAAAAAA") == 400

    def test_pricing_for_e_s_special_offer(self):
        assert checkout_solution.checkout("EB") == 40 + 30
        assert checkout_solution.checkout("EEB") == 40 + 40 + 0
        assert checkout_solution.checkout("EE") == 40 + 40
        assert checkout_solution.checkout("EEEEEB") == 40 * 5 + 0
        assert checkout_solution.checkout("EEEEEBB") == 40 * 5 + 0 + 0
        assert checkout_solution.checkout("EEEEEBBB") == 40 * 5 + 0 + 0 + 30
        assert checkout_solution.checkout("EEEEEBBBB") == 40 * 5 + 0 + 0 + 45

    def test_pricing_for_f_s_special_offer(self):
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
