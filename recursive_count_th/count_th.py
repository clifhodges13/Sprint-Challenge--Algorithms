'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    if len(word) < 2:
        return count
    if word.find('th') == -1:
        return count

    if len(word) > 1:
        if word[0]+word[1] == 'th':
            return count + 1 + count_th(word[1:])
        else:
            return count_th(word[1:])
    
    return count


print('birth',count_th('birth'))
print('bird',count_th('bird'))
print('fish',count_th('fish'))
print('thht',count_th('thht'))
