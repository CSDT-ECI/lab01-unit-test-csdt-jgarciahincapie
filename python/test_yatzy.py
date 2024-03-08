from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def testshouldChanceCorrectly(): 
        expected = 15
        
        actual = Yatzy.chance(1,2,3,4,5)

        assert expected == actual

def testShouldReturn50IfAllAreTheSame(): 
        expected = 50

        actual = Yatzy.yatzy([1,1,1,1,1])

        assert expected == actual

def testShouldReturn0IfAllAreNotEqual(): 
        expected = 0

        actual = Yatzy.yatzy([1,1,1,1,4])

        assert expected == actual

def testShouldSumTheOnes(): 
        expected = 2
         
        actual = Yatzy.ones(1,2,3,4,1)

        assert expected == actual

def testShouldGet0IfThersNoOnes(): 
        expected = 0 

        actual = Yatzy.ones(2,2,3,4,5)

        assert expected == actual 


def testShouldSumTheTwo(): 
        expected = 4
         
        actual = Yatzy.twos(2,2,3,4,1)

        assert expected == actual

def testShouldGet0IfThersNoTwo(): 
        expected = 0 

        actual = Yatzy.twos(1,1,3,4,5)

        assert expected == actual


def testShouldSumTheThree(): 
        expected = 6
         
        actual = Yatzy.threes(3,2,3,4,1)

        assert expected == actual

def testShouldGet0IfThersNoThree(): 
        expected = 0 

        actual = Yatzy.threes(2,2,1,4,5)

        assert expected == actual

def testShouldSumTheFour():
        yatzyObject= Yatzy(1,2,4,4,5)
        expected = 8

        actual = yatzyObject.fours()

        assert expected == actual 

def testShouldSumTheNoFour():
        yatzyObject= Yatzy(1,2,3,3,5)
        expected = 0

        actual = yatzyObject.fours()

        assert expected == actual

def testShouldSumTheFives():
        yatzyObject= Yatzy(1,2,3,5,5)
        expected = 10

        actual = yatzyObject.fives()

        assert expected == actual

def testShouldCrazyCahnge(): 
        yatzyObject= Yatzy(1,2,3,5,5)
        expected = 34

        actual = yatzyObject.crazyChance()

        assert expected == actual
