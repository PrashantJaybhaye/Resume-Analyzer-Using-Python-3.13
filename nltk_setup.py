import nltk
import ssl

# Handle SSL certificate issues
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

packages = [
    "stopwords",
    "punkt", 
    "averaged_perceptron_tagger",
    "maxent_ne_chunker",
    "words",
    "omw-1.4",  # WordNet data
    "wordnet",  # WordNet
]

print("Downloading NLTK data packages...")
for pkg in packages:
    try:
        nltk.download(pkg, quiet=True)
        print(f"✓ Downloaded {pkg}")
    except Exception as e:
        print(f"✗ Failed to download {pkg}: {e}")

print("NLTK setup completed!")
