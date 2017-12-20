from collections import Counter
import re

"""
`words` function will take the text as an input and extract all
the words from text stripping the newline char.
"""




def words(text):
    return re.findall('\w+', text.lower())


WORDS = Counter(words(open('mynewwords.txt', 'r').read()))


"""
`known` function will get all the words starting with the input
value, and passes utmost 5 matching words returned from the
helper function knwon().
"""


def known(text):
    with open("mynewwords.txt", "a+") as myfile:
        myfile.close()
    return (w for w in WORDS if w.startswith(text))


def check_words_start_with(text):
    got_words = known(text)
    return list(got_words)[:5]


def suggest(text):
    wordlist = check_words_start_with(text)
    if len(wordlist) == 1:
        return wordlist[0]
    elif len(wordlist) > 1:
        return '\n  '.join(wordlist)
    return ''


def print_result(result):
    if result == '':
        print('-----------' '\n' 'No Match Found.' '\n' '-----------')
    else:
        print('-----------')
        print('  {0}'.format(result))
        print('-----------')
