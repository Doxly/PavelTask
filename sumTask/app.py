"""
Main application.
Enter two numbers:
- the number - summa
- the number of summands
"""

class Application(object):
    
    is_debug = False

    def input_int(self, prompt, limit = 20, raw_input=raw_input):
        # raw_input parameter with default value entered for unit-testing
        while True:
            str_val = raw_input(prompt)
            try:
                int_val = int(str_val)
                if int_val > limit:
                    print """Your value (%i) greater then the maximum limit is %i. 
                    Please try again.""" % (int_val, limit)
                    raise ValueError("Max limit exceeded.")
                else:
                    return int_val
            except ValueError, e:
                print "You need to enter Integer value. Please repeat."
                if self.is_debug:
                    raise ValueError(e)
                    break

    def start(self):
        print "main application started."
        summa = self.input_int("Enter Summa: ")
        n_factors = self.input_int("Enter summand count: ")
        print "Thats all"

if __name__ == '__main__':
    application = Application()
    application.start() 