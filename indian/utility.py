from indian.models import Words
import csv

def populate_data():
    with open("indian/word_search.tsv") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        count = 0
        for line in tsvreader:
            word = line[0]
            word_frequency = line[1]
            word_length = len(word)

            Words.objects.create(name=word, frequency=word_frequency, word_length=word_length)