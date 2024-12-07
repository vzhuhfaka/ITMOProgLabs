
def read_lines_split_comma(file_path: str) -> list:
    lines = []
    with open(file_path) as f:
        for line in f.readlines():
            lines.append(line.strip().split(','))

    return lines
