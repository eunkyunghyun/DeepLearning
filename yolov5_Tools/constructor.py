"""
This was developed to promote numerous tasks in working with YOLOv5.
To receive the latest information, please refer to our GitHub browser.
The parts marked as a pair of parentheses signify what must be inputted personally.
"""

from glob import glob

paths = glob("(PATH OF DATASET'S LABEL)", recursive=True)
text = []

for path in paths:
    with open(path, 'r+') as f:
        lines = f.readlines()
        text.clear()
        for line in lines:
            separate = line.split(' ')
            separate[0] = "(SEQUENCE OF DATA)"
            text.append(" ".join(separate))
        f.truncate(0)
        f.seek(0)
        f.writelines(text)
