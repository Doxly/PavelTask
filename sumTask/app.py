import sys
import argparse
"""
Main application.
Enter two numbers:
- the number - summa
- the number of summands

Programm fill the list of all possible combinations of summands,
count them and print the result.
when summa = 50 in graph mode application work about 1 minute.
"""

class Application(object):

    def __init__(self):
        super(Application, self).__init__()
        self.is_debug = False
        self.input = raw_input

    def start(self, summa, n_factors):
        "Main cicle of application"
        # summa = args.summa
        # n_factors = args.n_factors
        interactive = summa is None or n_factors is None
        while True:
            if interactive:
                if summa is None:
                    print('Enter zero to exit from app.')
                    summa = self.input_int("Enter Summa: ")
                    if summa==0:
                        break

                if n_factors is None:
                    n_factors = self.input_int(
                        "Enter summand count: ", 
                        [2, summa]
                        )

            result = self.countCombinations(summa, n_factors)
            
            print "\nI'm count %i combinations for (%i, %i)\n" % (
                result, summa, n_factors)
            if interactive:
                summa = None
                n_factors = None
            else:
                break
        print "Thanks for using! Bye!"

    def input_int(self, prompt, limit = [0, 20]):
        """Input integer values with given prompt.
        Value range controlled over given limit.
        When range bounds is broken, print error message and repeat input.
        """
        lmin, lmax = limit
        while True:
            # either raw_input in working or mock-function in testing
            str_val = self.input(prompt)
            try:
                int_val = int(str_val)
                if int_val > lmax:
                    print """Your value (%i) is greater then the maximum limit - %i. 
                    """ % (int_val, lmax)
                    raise ValueError("Max limit exceeded.")
                elif int_val < lmin:
                    print """Your value(%i) is less then the minimum limit - %i.
                    """ % (int_val, lmin)
                    raise ValueError("Min limit exceeded.")
                return int_val
            except ValueError, e:
                print "You need to enter integer value in range(%i, %i). Please repeat." %(
                    lmin, lmax)
                if self.is_debug:
                    raise ValueError(e)
                    break

    def countCombinations(self, summa, n_factors):
        # fill array of summands and count array length
        combinations = self.fillCombinations(summa, n_factors)
        return len(combinations)

    def fillCombinations(self, summa, n_factors, max_limit = None):
        # for outer calls max_limit is equals summa
        result = []
        if max_limit is None:
            max_limit = summa
        # We will use this function in recursion
        #
        # all summands in exporession ordered from biggest to lowest
        #
        # min n_factors is 2
        # max n_factors is summa
        # min value for summand is 1
        # max value for summand is (summa - n_factors + 1) or max_limit
        #
        # summand is not good if it is bigger preceding one

        if n_factors==1:
            if summa<=max_limit:
                result.append([summa])
            return result
        
        start = summa - n_factors + 1
        if start > max_limit:
            start = max_limit

        for x in xrange(start, 0, -1):
            inner = self.fillCombinations(summa - x, n_factors-1, x)
            if inner!=[]:
                for i in inner:
                    combination = [x]
                    combination.extend(i)
                    result.append(combination)
        return result

    def help(self):
        """Print help message - how to use this programm"""
        print """
This programm written after Kuleshov Pavel talk.
Application calculate amount of unique combinations of summands
by given 'summa' and 'summand count'.
"""

    def buildGraph(self, summa):
        if summa is None:
            summa = self.input_int('Enter summa:', [1, 20])
        result = []
        print 'summa=%s' % summa
        for n_factors in xrange(2, summa):
            count = self.countCombinations(summa, n_factors)
            result.append((n_factors, count))
        for i,x in result:
            print "{0:2} ({1:2}) {2}".format(i, x, self.makeBar(x, '*'))
        return result

    def makeBar(self, count, char='*'):
        """Generate string of 'char' length 'count'"""
        result = ''
        for i in xrange(0, count):
            result = result + char
        return result

    def getArgs(self, parameters=None):
        """Pars command line parameters and return Namespace object"""
        parser = argparse.ArgumentParser(description='process parameters')
        parser.add_argument('-g', '--graph',
            dest='mode',
            action='store_const',
            const='graph',
            default='interactive',
            help='Show graph of count combinations depend of count of summands.')
        parser.add_argument('summa', 
            metavar='summa',
            type=int,
            nargs='?',
            choices=xrange(0, 21),
            default=None,
            help='an integer for summa. Maximum limit is 20.')
        parser.add_argument('n_factors',
            metavar='n_summands',
            type=int,
            nargs='?',
            choices=xrange(2, 21),
            default=None,
            help='an integer for summands count. In range(2, Summa).')
        args = parser.parse_args(parameters)
        return args

if __name__ == '__main__':
    application = Application()
    args = application.getArgs()
    print "args=%s" % args
    if args.mode =='graph':
        application.buildGraph(args.summa)
    else:
        application.start(args.summa, args.n_factors)
