def solution(x):
    l = len(x)
    final = []
    for i in range(l):
        c = x[i]
        if 'a' <= c <= 'z':
            # Calculate the position of the character in the alphabet
            pos = ord(c) - ord('a')
            # Invert the position to obtain the corresponding character
            final.append(chr(ord('a') + 25 - pos))
        else:
            final.append(c)
    return ''.join(final)


if __name__ == "__main__":
    t1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    print(solution(t1))

    t2 = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
    print(solution(t2))
