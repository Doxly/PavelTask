from nose.tools import *

import sumTask.app

def str_raw_input(prompt):
    return prompt

class TestSumTask(object):

    def setup(self):
        # print "SETUP!"
        self.application = sumTask.app.Application()
        self.application.is_debug = True
        self.application.input = str_raw_input

    def teardown(self):
        # print "TEAR DOWN!"
        pass

    def test_input_int_(self):
        # Normal int
        val = self.application.input_int('12', [0, 20])
        assert_equals(val, 12)

        # Int greater max-limit
        assert_raises(ValueError, 
            self.application.input_int, 
            '12', 
            [0, 10])

        # Int less min limit
        assert_raises(ValueError,
            self.application.input_int,
            '5',
            [7, 10])

        # Wrong Int
        assert_raises(ValueError, 
            self.application.input_int, 
            'error_int_string', 
            [0, 10])

    def test_countCombinations(self):
        result = self.application.countCombinations(3,2)
        assert_equals(result, 1)

        result = self.application.countCombinations(6, 2)
        assert_equals(result, 3)

        result = self.application.countCombinations(6, 3)
        assert_equals(result, 3)

        result = self.application.countCombinations(7, 3)
        assert_equals(result, 4)

    def test_fillCombinations(self):
        result = self.application.fillCombinations(3,2)
        assert_equals(result, [[2,1]])

        result = self.application.fillCombinations(6, 3)
        assert_equals(result, [[4,1,1],[3,2,1],[2,2,2]])

        result = self.application.fillCombinations(7, 3)
        assert_equals(result, [[5,1,1],[4,2,1],[3,3,1],[3,2,2]])
