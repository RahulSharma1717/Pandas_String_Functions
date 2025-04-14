# Find the movie with the longest name.

import pandas as pd

df = pd.read_csv('IMDB Top 250 Movies.csv')
pd.set_option('display.max_columns', None)

df['title_length'] = df['name'].str.len()
longest_name = df[df['title_length'] == df['title_length'].max()]
print(longest_name)


"""Output:
    rank                                               name  year  rating  \
67    68  Dr. Strangelove or: How I Learned to Stop Worr...  1964     8.4   

         genre certificate run_time  \
67  Comedy,War          PG   1h 35m   

                                              tagline   budget box_office  \
67  The comedy classic from celebrated director ST...  1800000    9523464   

                                                casts        directors  \
67  Peter Sellers,George C. Scott,Sterling Hayden,...  Stanley Kubrick   

                                        writers  title_length  
67  Stanley Kubrick,Terry Southern,Peter George            68 
"""