def str_capitalize(string):
    s_lower = str_lower(string)
    s1 = chr(ord(s_lower[0]) - 32)
    s2 = s_lower[1::]

    return s1 + s2


def str_count(string, substring, start=0, end=None):
    if len(substring) > len(string):
        return -1

    if end is None:
        end = len(string)

    count = 0
    for i in range(start, end - len(substring) + 1, 1):
        str_slice = string[i:i + len(substring):1]
        same = True

        for j in range(len(substring)):
            if substring[j] != str_slice[j]:
                same = False
                break

        if same:
            count += 1

    return count


def str_endswith(string, suffix, start=0, end=None):
    if len(suffix) > len(string):
        return False

    if end is None:
        end = len(string)

    str_slice = string[start:end + 1]

    for i in range(-1, -(len(suffix) + 1), -1):
        if str_slice[i] != suffix[i]:
            return False

    return True


def str_find(string, elem, start=0, end=None):
    if len(elem) > len(string):
        return -1

    if end is None:
        end = len(string)

    for i in range(start, end - len(elem) + 1, 1):
        substring = string[i:i + len(elem)]

        same = True

        for j in range(len(substring)):
            if substring[j] != elem[j]:
                same = False
                break

        if same:
            return i

    return -1


def str_join(iterable, separator=''):
    st = str(iterable[0])
    for i in range(1, len(iterable)):
        st += separator + str(iterable[i])

    return st


def str_replace(string, substring, replace_str, count=None):
    if count is None:
        count = str_count(string, substring)

    replaced = ''
    i = 0
    j = 0

    if count > 0:
        while i < len(string) and j < count:
            index = str_find(string, substring, i)
            if index != -1:
                replaced += string[i:index] + replace_str
                i = index + len(substring)
                j += 1
            else:
                replaced += string[i:]
                return replaced
        if j >= count:
            replaced += string[i:]
            return replaced

    else:
        return string


def str_rfind(string, elem, start=0, end=None):
    if len(elem) > len(string):
        return -1

    if end is None:
        end = len(string)

    count = str_count(string, elem, start, end)

    index = str_find(string, elem, start, end)

    for i in range(1, count):
        index = str_find(string, elem, index + 1, end)

    return index


def str_startswith(string, suffix, start=0, end=None):
    if len(suffix) > len(string):
        return False

    if end is None:
        end = len(string)

    str_slice = string[start:end + 1]

    for i in range(len(suffix)):
        if str_slice[i] != suffix[i]:
            return False

    return True


def str_strip(string):
    s = string[:]
    while s[0] == ' ' or s[0] == '\t':
        s = s[1:]
    while s[-1] == ' ' or s[-1] == '\t':
        s = s[:-1]

    return s


def str_lower(s):
    lower_s = ''
    for i in s:
        if 65 <= ord(i) <= 90:
            lower_s += chr(ord(i) + 32)
        else:
            lower_s += chr(ord(i))

    return lower_s

