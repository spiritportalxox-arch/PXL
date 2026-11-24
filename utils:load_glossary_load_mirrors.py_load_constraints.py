def load_glossary(filename):
    # Load glossary from file
    with open(filename, 'r') as f:
        return [line.strip().split('|') for line in f]

def load_mirrors(directory):
    # Load mirrors from directory
    mirrors = []
    for filename in os.listdir(directory):
        if filename.startswith('mirror_'):
            mirrors.append(load_glossary(os.path.join(directory, filename)))
    return mirrors

def load_constraints(filename):
    # Load constraints from file
    with open(filename, 'r') as f:
        return f.read()
