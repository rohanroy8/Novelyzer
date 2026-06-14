def sort_by(val: tuple[str, int]):
    return val[1]

def word_count(text: str) -> int:
    l = text.split()

    return len(l)

def char_count(text: str) -> list[tuple[str, int]]:
    charKV: dict[str, int] = {}
    for i in text:
        i = i.lower()
        charKV[i] = charKV.get(i,0) + 1

    wcount: list[tuple[str,int]] = []
    for key in charKV:
        current = (key,charKV[key])
        wcount.append(current)

    sorted_wcount = sorted(wcount, reverse=True, key=sort_by)

    return sorted_wcount

def word_frequency(text: str) -> list[tuple[str, int]]:
    wlist = text.split()
    freq: dict[str, int] = {}

    for item in wlist:
        if(len(item) < 6):
            continue

        item = item.lower()
        freq[item] = freq.get(item,0) + 1


    freq_count: list[tuple[str,int]] = []
    for key in freq:
        current: tuple[str, int] = (key, freq[key])
        freq_count.append(current)

    freq_count = sorted(freq_count, reverse=True, key=sort_by)

    return freq_count

