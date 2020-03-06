####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

def enum(**named_values):
    return type('Enum', (), named_values)

team_name = 'HYPEBEASTS' # Only 10 chars displayed.
strategy_name = '[retacted]\'s Algorithm'
strategy_description = 'AI guided algrorithm that uses hyperthreaded databuffers to energize character generating flux capacieors. Uses quantum coupled machine learning to do error correction.'

Style = enum(STINGY=1, FAIR=2, GULLIBLE=3, PATTERNED=4, RANDOM=0)
style = Style.RANDOM
class style():
    STINGY = 1 #always aggressive
    FAIR = 2 #copies you
    GULLIBLE = 3 #tends to pick collude more
    PATTERNED = 4 #pattern
    RANDOM = 5 #unknown/random

#test sequence
testSequence = 'cccbbbcbcb'
        
        

def move(my_history, their_history, my_score, their_score):
    global style
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    #Collude by default so there won't be an invalid move
    returnValue = 'c'
    prevMatches = len(their_history)
    matchNum = prevMatches + 1

    #Mimic by default normally
    if prevMatches > 0:
        returnValue = their_history[-1]

    #Send test sequence
    if prevMatches < len(testSequence):
        returnValue = testSequence[prevMatches]
        
    #Detect playstyle
    if prevMatches == len(testSequence):
        #Detect
        #stingy
        if(their_history[4:].upper()=='B'*(len(testSequence)-4)):
            style = Style.STINGY
        #fair
        if(their_history[1:].upper()==testSequence.upper()):
            style = Style.FAIR
        #gullible            
        if(their_history[4:].upper()=='C'*(len(testSequence)-4)):
            style = Style.GULLIBLE
        #patterned            
        if('BCBCBCBC' in their_history.upper()):
            style = Style.PATTERNED

    if prevMatches >= len(testSequence):
        if style == 1:
            returnValue = 'c'
        elif style == 2:
            returnValue = 'c'
        elif style == 3:
            returnValue = 'b'
        elif style == 4:
            None
        else:
            #Just mimic
            None

        

    # #Ending move
    # if len(my_history) == 99:
    #     returnValue = 'b'

    return returnValue

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             