def recite(start_verse, end_verse):
    if not (0 < start_verse < 13 and 0 < end_verse < 13):
        raise Exception('Please provide numbers between 1 and twelve')
    return [recite_one(i) for i in range(start_verse, end_verse + 1)]


# turn a number into its proper string
def number_to_string(number):
    strings = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
               'eleventh', 'twelfth']
    return strings[number - 1]


# recite one verse
def recite_one(day_number):
    # list of gifts
    gifts = ['a Partridge in a Pear Tree.', 'two Turtle Doves', 'three French Hens', 'four Calling Birds',
             'five Gold Rings',
             'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing',
             'ten Lords-a-Leaping',
             'eleven Pipers Piping', 'twelve Drummers Drumming']

    # construction the first half of the verse
    verse_first_half = 'On the {} day of Christmas my true love gave to me: '.format(number_to_string(day_number))

    # construction of the second half of the verse
    verse_second_half = gifts[0]
    for i in range(2, day_number + 1):
        # the first time we insert and, the following times we insert a comma
        if i == 2:
            verse_second_half = gifts[i - 1] + ', and ' + verse_second_half
        else:
            verse_second_half = gifts[i - 1] + ', ' + verse_second_half

    return verse_first_half + verse_second_half
