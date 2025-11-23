import pandas as pd
import sys

from rich.progress import track

rows = []

try:
    input_filename = sys.argv[1]
except IndexError:
    input_filename = "./FE2025_PCMMH_MeritList_Provisional.txt"

output_filename = input_filename + ".csv"

with open(input) as f:
    for line in track(f.readlines()):
        if line.strip()[0].isnumeric():
            rows.append(
                {
                    "Merit No": int(line.split()[0]),
                    "Application Id": line.split()[1],
                    "Candidate's Full Name": " ".join(line[:65].split()[2:]),
                    "Category": line[72:92].strip().removesuffix("#").removesuffix("$"),
                    "Gender": line[99:106].strip(),
                    "PWD": line[113:126].strip().startswith("PWD"),
                    "Def": line[113:126].strip().removeprefix("PWD")[-4:],
                    "EWS": line[131:137].strip().removesuffix("@") == "Yes",
                    "TFWS": line[141:147].strip() == "Yes",
                    "Orphan": line[151:158].strip() == "Yes",
                    "Linguistic Minority": line[159:168].strip().startswith("LM"),
                    "Religious Minority": line[159:168].strip().endswith("RM"),
                    "Merit Exam": line[170:181].strip(),
                    "Percentile/Mark": line[186:197].strip(),
                    "MHT-CET-PCM Math Percentile": line[199:210].strip(),
                    "MHT-CET-PCM Physics Percentile": line[212:224].strip(),
                    "MHT-CET-PCM Chemistry Percentile": line[224:236].strip(),
                    "HSC PCM %": line[242:249].strip(),
                    "HSC Math %": line[253:259].strip(),
                    "HSC Physics %": line[260:267].strip(),
                    "HSC / Diplomas / D.Voc. Total %": line[270:277].strip(),
                    "SSC Total %": line[280:287].strip(),
                    "SSC Math %": line[287:294].strip(),
                    "SSC Science %": line[294:301].strip(),
                    "SSC English %": line[301:].removesuffix("\n").strip(),
                    "Candidate Uploaded Receipt Of Validity Certificate": "$" in line,
                    "Candidate Uploaded Receipt Of EWS Certificate": "@" in line,
                    "Candidate Uploaded Receipt Of NCL Certificate": "#" in line,
                }
            )

df = pd.DataFrame(rows)
df.set_index("Merit No", inplace=True)
df.to_csv(output_filename)

print(df)
