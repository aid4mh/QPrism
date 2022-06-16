import json 
import boto3

import pandas as pd
def get_bucket(credentials_filepath, bucket_name):

    with open(credentials_filepath) as j:
        d = json.load(j)
    session = boto3.Session(
         aws_access_key_id=d['Access key ID'],
         aws_secret_access_key=d['Secret access key']
    )

    s3 = session.resource('s3')

    my_bucket = s3.Bucket(bucket_name)
    return my_bucket

def get_DQM_mappings(filepath):
    df = pd.read_csv(filepath, header = 0).to_dict('records')
    return {d['Unnamed: 0']: d for d in df}