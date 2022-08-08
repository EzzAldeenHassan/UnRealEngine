def duplicate_encode(word):
    count = {}
    outword = ''
    word = word.lower()
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for k in word:
        if count[k] > 1:
            outword += ')'
        else:
            outword += '('
    print( word, '=>', outword )

duplicate_encode("din")
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")
