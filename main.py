#!/usr/bin/env python3.8

import sys
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

print("start of processing")

input_folder = sys.argv[1]
output_folder = sys.argv[2]

# load the input file
input_path = pathlib.Path(input_folder)
input_files = list(input_path.iterdir())
input_file = input_files[0]
print(f"input_file: {input_file}")
df = pd.read_csv(input_file)

key_column = 'External Participant ID'
df.loc[df[key_column].str.startswith('IHCV'), 'study'] = 'IHCV'
df.loc[df[key_column].str.startswith('IHMS'), 'study'] = 'IHMS'
df.loc[df[key_column].str.startswith('IHUP'), 'study'] = 'IHUP'

df['WBC'] = df['WBC'].apply(pd.to_numeric, downcast='float', errors='coerce')
df['LY#'] = df['LY#'].apply(pd.to_numeric, downcast='float', errors='coerce')

plt.ylim([0, 15])
plt.axhline(y=3.71, color='lightgray', linestyle=':') 
plt.axhline(y=10.67, color='lightgray', linestyle=':') 
sns.stripplot('study', 'WBC', data=df, jitter=0.2)
sns.despine()

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file_name = f"{output_folder}/result_{now}.png"
print(f"saving result to {output_file_name}")
plt.savefig(output_file_name)

print("end of processing")
