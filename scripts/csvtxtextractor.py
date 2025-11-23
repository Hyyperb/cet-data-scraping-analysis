# INTENDED  TO BE USED WITH UNIX PIPES

import sys

input_filename = sys.argv[-1]

with open(input_filename) as f:
    for line in f.readlines():
        content = line.strip('"').replace('"\n', "\n")
        if "--adjust-for-cutoffs" in sys.argv and content.strip():
            print(
                content.removeprefix("Stage ")
                .removeprefix("III")
                .removeprefix("II")
                .removeprefix("I")
                .removeprefix("V"),
                end="",
            )

        else:
            if content.strip():
                print(content, end="")
