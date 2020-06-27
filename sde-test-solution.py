import json
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Read a json file and process the benchmark spread')
parser.add_argument('input_file', help='The input json file to read')
parser.add_argument('output_file', help='The output file where the json record will be stored')
args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file

with open(input_file) as data_file:
    data = json.load(data_file)

df = pd.DataFrame(data['data'])
df['tenor'] = df['tenor'].str[:-6].astype(float)
df['yield'] = df['yield'].str[:-1].astype(float) * 100

df_corp = df[df['type']=='corporate']

df_gov = df[df['type']=='government'].sort_values(by=['tenor'])

final_df = pd.DataFrame(columns = ['corporate_bond_id', 'government_bond_id', 'spread_to_benchmark'])

for col in df_corp['tenor']:
    df_gov['tenor_diff'] = abs(df_gov['tenor'] - col)
    df_c = df_corp[df_corp['tenor']==col]
    df_c = df_c.assign(j_key = 'join')
    df_diff = df_gov.sort_values(by=['tenor_diff']).head(1)
    df_diff = df_diff.assign(j_key = 'join')
    diff = df_c['yield'].astype(float) - df_diff['yield'].astype(float)
    df_new_diff = df_diff.merge(df_c, on='j_key')
    df_new_diff.rename(columns = {'id_y': 'corporate_bond_id', 'id_x': 'government_bond_id', 'yield_y': 'corp_yield', 'yield_x': 'gov_yield'}, inplace=True)
    df_new_diff['spread_to_benchmark'] = ((df_new_diff['corp_yield'] - df_new_diff['gov_yield']))
    df_new_diff = df_new_diff[['corporate_bond_id', 'government_bond_id', 'spread_to_benchmark']]
    df_new_diff.dropna(inplace=True)
    df_new_diff['spread_to_benchmark'] = (np.floor(df_new_diff['spread_to_benchmark'])).astype('int32')
    df_new_diff['spread_to_benchmark'] =  df_new_diff['spread_to_benchmark'].astype(str) + ' bps'
    final_df = final_df.append(df_new_diff)

final_df.to_json(output_file, orient='table', index=False)

