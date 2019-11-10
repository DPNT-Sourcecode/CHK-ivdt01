from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("XAA") == -1
        assert checkout_solution.checkout("A A") == -1
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AACAA") == 200
        assert checkout_solution.checkout("AACCAA") == 220
        assert checkout_solution.checkout("CAACCAA") == 240
        assert checkout_solution.checkout("CAABCCAA") == 270
        assert checkout_solution.checkout("CAABBCCAA") == 285
        assert checkout_solution.checkout("CAADBBCCAA") == 300
        assert checkout_solution.checkout("CAADBBBCCAA") == 330

