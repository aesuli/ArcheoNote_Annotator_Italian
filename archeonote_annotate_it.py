import os
import pickle
import sys
from io import StringIO
# import concurrent.futures
#
# import multiprocessing
from tarfile import ReadError

from utils.archive_utils import new_zip_archive
from utils.output_utils import html_template
from utils.pdf_to_txt import convert_archive_to_txt, convert_pdf_to_txt

print('Imports', flush=True)

import nltk

try:
    nltk.sent_tokenize('this is a test to check if punkt is installed')
except:
    nltk.download('punkt')

print('Functions', flush=True)


def add_surrounding_word(features, word, postag, inpos):
    inpos = '+' + str(inpos) if inpos > 0 else str(inpos)
    features.update({
        inpos + ':word.lower()': word.lower(),
        'word[:3]': word[:3],
        'word[:2]': word[:2],
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        inpos + ':word.istitle()': word.istitle(),
        inpos + ':word.isupper()': word.isupper(),
        inpos + ':postag': postag,
        inpos + ':postag[:2]': postag[:2],
    })


def word2features(sent, i, window=2):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[:3]': word[:3],
        'word[:2]': word[:2],
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    for j in range(window):
        j += 1
        if i - j >= 0:
            word1 = sent[i - j][0]
            postag1 = sent[i - j][1]
            add_surrounding_word(features, word1, postag1, inpos=-j)
        else:
            features['BOS' + str(j)] = True

        if i + j <= len(sent) - 1:
            word1 = sent[i + j][0]
            postag1 = sent[i + j][1]
            add_surrounding_word(features, word1, postag1, inpos=+j)
        else:
            features['EOS' + str(j)] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def get_input_as_txt(input_filename):  # , executor):
    try:
        return list(convert_archive_to_txt(input_filename))  # , executor)
    except ReadError:
        print('Not a zip file', flush=True)
    try:
        with open(input_filename, 'rb') as f:
            return [convert_pdf_to_txt(f.read(), input_filename)]
    except:
        print('Not a pdf file', flush=True)

    with open(input_filename, 'r', encoding='utf-8') as f:
        return [(f.read(), os.path.splitext(os.path.basename(input_filename))[0])]


def annotate_text(text, crf, input_filename):
    sent_text = nltk.sent_tokenize(text)
    tokenized_text = list()
    for sentence in sent_text:
        tokens = nltk.word_tokenize(sentence)
        tokenized_text.append(list(zip(tokens, ['_'] * len(tokens))))
    print('Indexed', flush=True)

    X = [sent2features(sentence) for sentence in tokenized_text]
    annotation = crf.predict(X)
    print('Annotated', flush=True)
    with StringIO() as output:
        output.write('<div class="header">ArcheoNote - Input file: <b>' + input_filename + '</b></div>')

        output.write('<div class="content">')
        last_annot = ''
        for sent, annots in zip(tokenized_text, annotation):
            for word, annot in zip(sent, annots):
                word = word[0]
                this_annot = annot[2:]
                if this_annot != last_annot:
                    last_annot = this_annot
                    output.write('</span> <span class="' + this_annot + '" title="' + this_annot + '">')
                else:
                    output.write(' ')
                output.write(word)
            output.write('<br/>')
        output.write('</div>')

        output.write('''<div class="footer">
            <b>Annotation types:</b>
            <span class='ARTEFACT annotation'>ARTEFACT</span> 
            <span class='BIOLOGICALREMAIN annotation'>BIOLOGICALREMAIN</span>
            <span class='COLOUR annotation'>COLOUR</span>
            <span class='MATERIAL annotation'>MATERIAL</span>
            <span class='PERIOD annotation'>PERIOD</span>
            <span class='PLACE annotation'>PLACE</span>
            <span class='SITE annotation'>SITE</span>
            <span class='TECHNIQUE annotation'>TECHNIQUE</span>
            <span class='TIMESPAN annotation'>TIMESPAN</span> <span class='right'>ArcheoNote - Italian model - release of December 2019</span>
            </div>
            <span>''')

        html_output = html_template.format(output.getvalue())
    return html_output, input_filename + ".html"


if __name__ == '__main__':
    print('Vars', flush=True)

    input_filename = sys.argv[1]
    model_filename = './models/archeonote_it_crf.model'

    print('Loading', flush=True)
    with open(model_filename, mode='rb') as infile:
        crf = pickle.load(infile)
    print('Model loaded', flush=True)

    # executor = concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count() - 1 or 1)
    texts = get_input_as_txt(input_filename)  # , executor)
    results = [annotate_text(text, crf, fname) for text, fname in texts]

    print('Text loaded', flush=True)
    try:
        new_zip_archive(results)
    except Exception as e:
        print("An error occurred while creating the output zip archive. Please find below the error explanation."
              " No output will be produced")
        print(e, flush=True)

    # executor.shutdown()
