import requests
import pandas as pd

# Reading the data.
Experian_url_df = pd.read_excel('Experian_success_url.xlsx')
pan_info = pd.read_excel('pan_info.xlsx')

# filtering the data frames for required features.
Experian_url_df = Experian_url_df[['raw_data','pan_card']]
pan_info = pan_info.rename(columns={'borrower_pan':'pan_card'})

merge_df = pd.merge(Experian_url_df, pan_info, on='pan_card', how='inner')
merge_df = merge_df.sort_values('pan_card')
merge_df = merge_df.reset_index()
path = r'D:\XML Parsing Project\Data Files\cleaned_xml' + '\\'
for url in merge_df['raw_data']:
    url = str(url)
    url = url.strip()
    r = requests.get(url, allow_redirects=True)
    open(path + url.split('/')[-1],'wb').write(r.content)