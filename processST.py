import pandas as pd

df = pd.read_csv("ST_candidates_selected.txt", delimiter="\t", header=None)

df.to_excel("ST_selected_candidates.xlsx", index=False)