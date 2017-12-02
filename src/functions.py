from collections import Counter
import re


def words(text):
    """
    This function will take the text as an input and extract all
    the words from text stripping the newline char.
    """
    return re.findall('\w+', text.lower())


WORDS = Counter(words(open('words.txt', 'r').read()))


def check_words_start_with(text):
    """
    This function will get all the words starting with the input
    value, and passes utmost 7 matching words returned from the
    helper function knwon().
    """
    got_words = known(text)
    return list(got_words)[:7]


def known(text):
    return (w for w in WORDS if w.startswith(text))


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
