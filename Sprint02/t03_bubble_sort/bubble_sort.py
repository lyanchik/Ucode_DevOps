def bubble_sort(bulbashka):
    for n in range(len(bulbashka)):
        for i in range(len(bulbashka) - 1):
            if bulbashka[i] > bulbashka[i + 1]:
                bulbashka[i], bulbashka[i + 1] = bulbashka[i + 1], bulbashka[i]