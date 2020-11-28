import gc
import json
import os
import re
import spacy

doc_dir = 'D:/enwiki20201020/'
stop_file = 'stopwords_default.txt'
sp = spacy.load('en_core_web_sm')

# TODO: try to load existing index
master_index = dict()

with open(stop_file, 'r', encoding='utf-8') as infile:
    stopwords = infile.readlines()


def integrate_doc_index(file, doc_index, article_id):
    for item in doc_index:
        if item['term'] not in master_index:
            master_index[item['term']] = list()
        entry = {'file': file, 'id': article_id, 'count': item['count'], 'pct': item['pct']}
        master_index[item['term']].append(entry)


def process_article(article):
    result = list()
    tokens = list()
    doc = sp(article['title'] + ' ' + article['text'])
    # TODO tokenize with regex \w+ instead
    # TODO lowercase everything first
    # TODO update stopwords
    for word in doc:
        if word.text.lower() in stopwords:
            continue
        tokens.append(word.lemma_)
    unique = list(set(tokens))
    for term in unique:
        item = {'term': term}
        count = len([i for i in tokens if i == term])
        pct = count / len(tokens)
        item['count'] = count
        item['pct'] = pct
        result.append(item)
    return result


def process_file(file):
    with open(doc_dir + file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    for article in data:
        doc_index = process_article(article)
        integrate_doc_index(file, doc_index, article['id'])
        save_master_index()
        exit()


def save_master_index():
    with open('master_index.json', 'w', encoding='utf-8') as outfile:
        json.dump(master_index, outfile, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    for file in os.listdir(doc_dir):
        # TODO: skip files/articles already in existing index
        process_file(file)
        save_master_index()
        exit(0)
        gc.collect()