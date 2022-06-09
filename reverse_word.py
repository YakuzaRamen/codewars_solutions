def reverse_words(text: str) -> str:
    result = ''

    for word  in text.split(' '):
        result +=f'{word[::-1]} '

    return result[0:len(text)]