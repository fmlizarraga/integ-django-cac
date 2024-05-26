# esta es la misma funcion del ejercicio 3
def count_words(string: str):
    words = string.lower().split()
    wordcount = {}
    
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    
    return wordcount

def most_freq_word(freqs: dict[str,int]):
    max_word = ''
    max_freq = 0

    for word, freq in freqs.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq

    return (max_word, max_freq)