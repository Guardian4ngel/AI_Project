import functions

try:
    temp = ''
    text = None

    print('Start Typing a word. If you need Suggestions, then press Enter/Return:\n '
          'Enter < for backspace of a char.')

    while True:

        if text is None:
            text = ''
        text = input(temp)
        temp += text

        if text == '':
            print('Your word is: ', temp)
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