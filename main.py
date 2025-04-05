import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, BigInteger, Float, String, Date, MetaData


df = pd.read_csv(
    'movies_metadata.csv',
    quotechar='"',
    low_memory=False)

# df['budget'] = df['budget'].astype(str).str.replace(',','')
# df['revenue'] = df['revenue'].astype(str).str.replace(',','')
# df['id'] = df['id'].astype(str)

# df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
# df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
# df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
# df['vote_count'] = pd.to_numeric(df['vote_count'], errors='coerce')
# df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
# df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
# df = df[df['id'].str.isnumeric()]
# df['id'] = df['id'].astype(int)

# username = 'postgres'
# password = 'm1nh4mu54'
# host = 'localhost'
# port = '5432'
# database = 'analytics'

# engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# df.to_sql('movies_metadata.csv', con=engine, if_exists='replace',index=False)


# metadata = MetaData()

# movies_metadata = Table('movies_metadata', metadata,
#     Column('adult', String),
#     Column('belongs_to_collection', String),
#     Column('budget', BigInteger),
#     Column('genres', String),
#     Column('homepage', String),
#     Column('id', BigInteger, primary_key=True),
#     Column('imdb_id', String),
#     Column('original_language', String),
#     Column('original_title', String),
#     Column('overview', String),
#     Column('popularity', Float),
#     Column('poster_path', String),
#     Column('production_companies', String),
#     Column('production_countries', String),
#     Column('release_date', Date),
#     Column('revenue', BigInteger),
#     Column('runtime', Float),
#     Column('spoken_languages', String),
#     Column('status', String),
#     Column('tagline', String),
#     Column('title', String),
#     Column('video', String),
#     Column('vote_average', Float),
#     Column('vote_count', BigInteger),
# )

# df.to_sql('movies_metadata.csv', con=engine, if_exists='append', index=False)

print(123)