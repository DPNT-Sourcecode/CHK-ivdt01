from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        assert hello_solution.hello(2) == "Hello world!"
