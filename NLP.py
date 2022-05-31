# pip install spacy
# python -m spacy download de_core_news_lg
import pandas as pd
import spacy

sp = spacy.load('de_core_news_lg')
skills = pd.read_csv('./data/competencies/skills_de.csv')
skill_labels = skills['preferredLabel'].copy(deep=True)
termStore = {} 
sequenceStore = {}
URI = 0

for i,sequence in enumerate(skill_labels):
    sequence = sp(sequence)
    label = ''
    for term in sequence:
        if not term.is_stop:
            term = term.lemma_
            term = term.lower()
            if term != '--':
                if term[0] == '-': term = term[1:]
                if term == '\xa0': continue
                label += term + ' '
                if termStore.get(term) == None: 
                    termStore[term] = URI
                    URI += 1
        skill_labels[i] = label[:-1]

for i,sequence in enumerate(skill_labels):
    URI = []
    sequence = sp(sequence)
    for term in sequence:
        URI.append(termStore[str(term)])
    sequenceStore[tuple(URI)] = (i,str(sequence))

course_descriptions = pd.read_xml('./data/course-description/example.xml')['CS_DESC_LONG']
text = sp(course_descriptions[1])

sequence = []
results = []

for term in text:
    term = term.lemma_.lower()
    if term in termStore:
        sequence.append(termStore[term])
    else:
        if sequence != []:
            URI = []
            for i in sequence:
                URI.append(i)
                if tuple(URI) in sequenceStore: 
                    result = sequenceStore[tuple(URI)]
                else: break
            if result: results.append(result)
            result = None
        sequence = []

for result in results:
    print(skills.loc[result[0]])