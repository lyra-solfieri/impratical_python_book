"""
Carregando um arquivo de texto em uma lista
"""
import sys

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            load_text = in_file.read().strip().split('\n')
            load_text = [x.lower() for x in load_text]
            return load_text
        
    except IOError as e:
        print("{}\nError abrindo {}".format(e,file),file=sys.stderr)
        sys.exit(1)

