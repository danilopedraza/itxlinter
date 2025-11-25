def write_to_file(content, filename):
    with open(filename, 'wb') as f:
        f.write(content)
