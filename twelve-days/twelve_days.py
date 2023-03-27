def recite(start_verse, end_verse):
    if start_verse > end_verse:
        raise ValueError('end_verse must be equal or larger than start_verse')
    elif start_verse <= 0 or end_verse <= 0:
        raise ValueError('start or end verse cannot be lower or equal to 0')

    number = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    middle_raw = ['two Turtle Doves', 'three French Hens', 'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']
    last = ' and a Partridge in a Pear Tree.'

    output =[]
    rng = range(start_verse-1, end_verse)
    for i in rng:
        first = f"On the {number[i]} day of Christmas my true love gave to me: "
        middle = ', '.join(reversed([middle_raw[k] for k in range(i)])) + ','
        sentence = first + middle + last
        if i == 0: sentence = sentence.replace(' , and', '')
        output.append(sentence)

    return output

