value_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suit_list = ['C','H','D','S']

value = '11'
suit = 'Q'

if value in value_list:
    if suit in suit_list:
        if suit == 'C':
            print("%s of Clubs" % (value))
        elif suit == 'H':
            print("%s of Hearts" % (value))
        elif suit == 'D':
            print("%s of Diamonds" % (value))
        elif suit == 'S':
            print("%s of Spades" % (value))
    else:
        print("Error: Invalid suit")
else:
    print("Error: Invalid value")
