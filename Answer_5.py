# Find out the oldest movie in the dataset.

import pandas as pd

df = pd.read_csv('IMDB Top 250 Movies.csv')
pd.set_option('display.max_columns', None)

oldest_movie = df.loc[df['year'] == df['year'].min()]
print("Oldest Movie:\n", oldest_movie)


"""Output:
Oldest Movie:
      rank     name  year  rating                genre certificate run_time  \
127   128  The Kid  1921     8.3  Comedy,Drama,Family      Passed    1h 8m   

                                               tagline  budget box_office  \
127  This is the great film he has been working on ...  250000      41960   

                                                 casts        directors  \
127  Charles Chaplin,Edna Purviance,Jackie Coogan,C...  Charles Chaplin   

             writers  
127  Charles Chaplin 
"""