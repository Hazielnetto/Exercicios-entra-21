def is_anagram(string1, string2):

    for l in string1:

        if l not in string2:

            return False

    return True

print(is_anagram(str(input('String 1: ')).lower(), str(input('String 2: ')).lower()))