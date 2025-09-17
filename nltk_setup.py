import nltk

packages = [
    "stopwords",
    "punkt",
    "averaged_perceptron_tagger",
    "maxent_ne_chunker",
    "words",
]

for pkg in packages:
    nltk.download(pkg)
