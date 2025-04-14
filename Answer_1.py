# Read the file and create a new column called title-length containing the length of each movie.

import pandas as pd

df = pd.read_csv('IMDB Top 250 Movies.csv')
pd.set_option('display.max_columns', None)

df['title_length'] = df['name'].str.len()
print(df)


"""Output:
     rank                      name  year  rating                       genre  \
0       1  The Shawshank Redemption  1994     9.3                       Drama   
1       2             The Godfather  1972     9.2                 Crime,Drama   
2       3           The Dark Knight  2008     9.0          Action,Crime,Drama   
3       4     The Godfather Part II  1974     9.0                 Crime,Drama   
4       5              12 Angry Men  1957     9.0                 Crime,Drama   
..    ...                       ...   ...     ...                         ...   
245   246                  The Help  2011     8.1                       Drama   
246   247               Dersu Uzala  1975     8.2   Adventure,Biography,Drama   
247   248                   Aladdin  1992     8.0  Animation,Adventure,Comedy   
248   249                    Gandhi  1982     8.0     Biography,Drama,History   
249   250        Dances with Wolves  1990     8.0     Adventure,Drama,Western   

    certificate run_time                                            tagline  \
0             R   2h 22m  Fear can hold you prisoner. Hope can set you f...   
1             R   2h 55m                         An offer you can't refuse.   
2         PG-13   2h 32m                                    Why So Serious?   
3             R   3h 22m       All the power on earth can't change destiny.   
4      Approved   1h 36m  Life Is In Their Hands -- Death Is On Their Mi...   
..          ...      ...                                                ...   
245       PG-13   2h 26m                      Change begins with a whisper.   
246           G   2h 22m  There is man and beast at nature's mercy. Ther...   
247           G   1h 30m                     Wish granted! (DVD re-release)   
248          PG   3h 11m             His Triumph Changed The World Forever.   
249       PG-13    3h 1m  Inside everyone is a frontier waiting to be di...   

            budget     box_office  \
0         25000000       28884504   
1          6000000      250341816   
2        185000000     1006234167   
3         13000000       47961919   
4           350000            955   
..             ...            ...   
245       25000000      216639112   
246        4000000          14480   
247  Not Available  Not Available   
248       22000000       52767889   
249       22000000      424208848   

                                                 casts  \
0    Tim Robbins,Morgan Freeman,Bob Gunton,William ...   
1    Marlon Brando,Al Pacino,James Caan,Diane Keato...   
2    Christian Bale,Heath Ledger,Aaron Eckhart,Mich...   
3    Al Pacino,Robert De Niro,Robert Duvall,Diane K...   
4    Henry Fonda,Lee J. Cobb,Martin Balsam,John Fie...   
..                                                 ...   
245  Viola Davis,Emma Stone,Octavia Spencer,Bryce D...   
246  Maksim Munzuk,Yuriy Solomin,Mikhail Bychkov,Vl...   
247  Scott Weinger,Robin Williams,Linda Larkin,Jona...   
248  Ben Kingsley,John Gielgud,Rohini Hattangadi,Ro...   
249  Kevin Costner,Mary McDonnell,Graham Greene,Rod...   

                    directors  \
0              Frank Darabont   
1        Francis Ford Coppola   
2           Christopher Nolan   
3        Francis Ford Coppola   
4                Sidney Lumet   
..                        ...   
245               Tate Taylor   
246            Akira Kurosawa   
247  Ron Clements,John Musker   
248      Richard Attenborough   
249             Kevin Costner   

                                             writers  title_length  
0                        Stephen King,Frank Darabont            24  
1                    Mario Puzo,Francis Ford Coppola            13  
2    Jonathan Nolan,Christopher Nolan,David S. Goyer            15  
3                    Francis Ford Coppola,Mario Puzo            21  
4                                      Reginald Rose            12  
..                                               ...           ...  
245                     Tate Taylor,Kathryn Stockett             8  
246    Akira Kurosawa,Yuriy Nagibin,Vladimir Arsenev            11  
247             Ron Clements,John Musker,Ted Elliott             7  
248                                      John Briley             6  
249                                    Michael Blake            18  

[250 rows x 14 columns]
"""