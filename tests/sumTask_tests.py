from nose.tools import *

import sumTask.app

def str_raw_input(prompt):
    print "str_raw_input called"
    return prompt

class TestSumTask(object):

    def setup(self):
        print "SETUP!"
        self.application = sumTask.app.Application()
        self.application.is_debug = True

    def teardown(self):
        print "TEAR DOWN!"

    def test_input_int_(self):
        # Normal int
        val = self.application.input_int('12', 20, str_raw_input)
        assert_equals(val, 12)

        # Int greater max-limit
        assert_raises(ValueError, 
            self.application.input_int, 
            '12', 
            10, 
            str_raw_input)

        # Wrong Int
        assert_raises(ValueError, 
            self.application.input_int, 
            'error_int_string', 
            10, 
            str_raw_input)
