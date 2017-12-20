import functions
import os
import sys


try:

    temp = ''

    text = None

    print('-- start typing a word to make suggestions then press *Enter* ...')
    print('-- you can type < then press *Enter* for backspace a char ...\n')

    while True:

        arr = os.listdir('class') #open classes directory
        for x in range(arr.__len__()):
            with open("mynewwords.txt", "a+") as myfile:  #openfiel
                myfile.write(arr[x]) #put file name in the file mynewword.txt
                myfile.write("\n")

        if text is None:
            text = ''

        text = raw_input(temp)
        temp += text

        if text == '':
            print('your word is: ', temp)
            break

        elif text.strip() == '<':
            temp = temp.replace('<', '')[:-1]
            print(temp)

        result = functions.suggest(temp.strip().lower())

        if result == temp:
            print('Your word is:', temp)
            break

        elif '\n' not in result and result != '':
            print('Were you looking for "{0}"?'.format(result))

            if input().strip().lower() == 'y':
                print('Your word: {0}'.format(result))
                break
            else:
                pass
        else:
            functions.print_result(result)
except KeyboardInterrupt:
    print('\n' 'Quitting...')
