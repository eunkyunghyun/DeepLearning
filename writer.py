"""
This is developed to promote numerous tasks in working with YOLOv5.
To receive the latest information, please refer to our GitHub browser.
"""

from glob import glob

paths = glob("[Path of dataset's label]", recursive=True)

for path in paths:
    f = open(path, 'r')
    lines = f.readlines()
    text = []
    for line in lines:
        separate = line.split(' ')
        separate[0] = "[Sequence of data]"
        text.append(" ".join(separate))
    fb = open(path, 'w')
    fb.truncate(0)
    fb.writelines(text)
