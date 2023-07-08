from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
import spacy

'''
all_columns= ['soleadify_id', 'veridion_id', 'company_name', 'company_legal_names',
       'company_commercial_names', 'main_country_code', 'main_country',
       'main_region', 'main_city_district', 'main_city', 'main_postcode',
       'main_street', 'main_street_number', 'main_latitude', 'main_longitude',
       'locations', 'num_locations', 'company_type', 'year_founded',
       'employee_count', 'estimated_revenue', 'short_description',
       'long_description', 'business_tags', 'business_model', 'product_type',
       'naics_vertical', 'primary_naics6_code', 'primary_naics6_label',
       'secondary_naics6_codes', 'secondary_naics6_labels',
       'aggregated_sector', 'aggregated_industry', 'main_business_category',
       'main_industry', 'main_sector', 'website_url', 'website_domain',
       'instagram_url', 'linkedin_url', 'ios_app_url', 'android_app_url',
       'youtube_url', 'tiktok_url', 'cms', 'alexa_rank', 'technologies',
       'sics_codified_industry', 'sics_codified_industry_code', 'twitter_url',
       'instagram_url', 'linkedin_url', 'ios_app_url', 'android_app_url',
       'youtube_url', 'tiktok_url', 'cms', 'alexa_rank', 'technologies',
       'sics_codified_industry', 'sics_codified_industry_code',
       'sics_codified_subsector', 'sics_codified_subsector_code', 'instagram_url',
        'linkedin_url', 'ios_app_url', 'android_app_url',
       'youtube_url', 'tiktok_url', 'cms', 'alexa_rank', 'technologies',
       'sics_codified_industry', 'sics_codified_industry_code',
       'sics_codified_subsector', 'sics_codified_subsector_code',
       'sics_codified_sector', 'sics_codified_sector_code', 'sic_codes',
       'sic_labels', 'ibc_insurance_labels', 'ibc_insurance_codes',
       'created_at', 'last_updated_at', 'website_number_of_pages',
       'website_external_links', 'website_technical_issues', 'seo_score',
       'seo_issues']
'''

            #   0               1               2
used_cols=['company_type','business_model', 'product_type', 
            #   3               4               5
           'website_url', 'main_industry', 'technologies',
            #   6
            'company_name'
           ]

nlp = spacy.load("en_core_web_sm")
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_colwidth', None)

def extract_company_names(sentence):
    try:
        doc = nlp(sentence)
        company_names = []
        for ent in doc.ents:
            if ent.label_ == "ORG":
                company_names.append(ent.text)
        return company_names
    except:
        return ""

#def technologies_predict(domain, file):
#    df = pd.read_parquet(file, engine='fastparquet', columns=used_cols)
#    dev_technologies = ['javascript', 'mysql', 'jquery', 'react', 'apache', 'php', 'ruby', 'yoast', 'bootstrap', 'litespeed']
#    technical_weights ={t:[] for t in dev_technologies}
#    a = [ df[ used_cols[5] ][ index ] for index in range(df.shape[0]) 
#        if df[ used_cols[5] ][ index ] is not None and df[ used_cols[4] ][ index ] == domain ]
#    for t in dev_technologies:
#        technical_weights[t].append( {'count':str( a ).count(t)})
#    weights = [list(i[0].values())[0] for i in technical_weights.values()]
#    weights = [(elem/sum(weights)) * 1 for elem in weights]
#    choice = np.random.choice(a=dev_technologies, size=1, p=weights)
#    return choice

def domain_predict(name, file):
    try:
        df = pd.read_parquet(file, engine='fastparquet', columns=used_cols)
        X_train = df[used_cols[6]]
        Y_train = df[used_cols[4]]
        vectorizer = CountVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        model = MultinomialNB()
        model.fit(X_train, Y_train)
        X_predict = vectorizer.transform([name])
        Y_predict = model.predict(X_predict)
        return Y_predict[0]
    except:
        return ""
