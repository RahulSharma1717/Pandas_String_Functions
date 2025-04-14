# Display the data where the movie titles satrt with 'The'.

import pandas as pd

df = pd.read_csv('IMDB Top 250 Movies.csv')
pd.set_option('display.max_columns', None)

The_movie = df[df['name'].str.split().str[0] == 'The']
print(The_movie)


"""Output:
     rank                                               name  year  rating  \
0       1                           The Shawshank Redemption  1994     9.3   
1       2                                      The Godfather  1972     9.2   
2       3                                    The Dark Knight  2008     9.0   
3       4                              The Godfather Part II  1974     9.0   
6       7      The Lord of the Rings: The Return of the King  2003     9.0   
8       9  The Lord of the Rings: The Fellowship of the Ring  2001     8.8   
9      10                     The Good, the Bad and the Ugly  1966     8.8   
12     13              The Lord of the Rings: The Two Towers  2002     8.8   
15     16                                         The Matrix  1999     8.7   
21     22                           The Silence of the Lambs  1991     8.6   
26     27                                     The Green Mile  1999     8.6   
31     32                                        The Pianist  2002     8.5   
35     36                                      The Lion King  1994     8.5   
38     39                                       The Departed  2006     8.5   
39     40                                 The Usual Suspects  1995     8.5   
40     41                                       The Prestige  2006     8.5   
45     46                                   The Intouchables  2011     8.5   
57     58                                The Lives of Others  2006     8.4   
60     61                                        The Shining  1980     8.4   
61     62                                 The Great Dictator  1940     8.4   
68     69                              The Dark Knight Rises  2012     8.4   
76     77                                           The Boat  1981     8.4   
93     94                                           The Hunt  2012     8.3   
101   102                                      The Apartment  1960     8.3   
111   112                                          The Sting  1973     8.3   
127   128                                            The Kid  1921     8.3   
129   130                                         The Father  2020     8.2   
131   132                            The Wolf of Wall Street  2013     8.2   
137   138                                    The Truman Show  1998     8.2   
140   141                                    The Sixth Sense  1999     8.2   
145   146                   The Treasure of the Sierra Madre  1948     8.2   
147   148                                   The Great Escape  1963     8.2   
152   153                                          The Thing  1982     8.2   
154   155                                   The Elephant Man  1980     8.2   
162   163                           The Secret in Their Eyes  2009     8.2   
165   166                       The Bridge on the River Kwai  1957     8.2   
176   177                                      The Gold Rush  1925     8.1   
184   185                           The Grand Budapest Hotel  2014     8.1   
186   187                                        The General  1926     8.1   
187   188                                      The Third Man  1949     8.1   
189   190                                    The Deer Hunter  1978     8.1   
192   193                                  The Wages of Fear  1953     8.2   
198   199                                   The Seventh Seal  1957     8.1   
205   206                                   The Big Lebowski  1998     8.1   
207   208                         The Passion of Joan of Arc  1928     8.2   
214   215                                     The Terminator  1984     8.1   
221   222                                   The Wizard of Oz  1939     8.1   
224   225                        The Best Years of Our Lives  1946     8.1   
225   226                                       The Exorcist  1973     8.1   
226   227                                    The Incredibles  2004     8.0   
229   230                              The Battle of Algiers  1966     8.1   
232   233                                The Grapes of Wrath  1940     8.1   
238   239                                     The Handmaiden  2016     8.1   
239   240                                      The 400 Blows  1959     8.1   
240   241                                 The Sound of Music  1965     8.1   
244   245                                     The Iron Giant  1999     8.1   
245   246                                           The Help  2011     8.1   

                          genre    certificate       run_time  \
0                         Drama              R         2h 22m   
1                   Crime,Drama              R         2h 55m   
2            Action,Crime,Drama          PG-13         2h 32m   
3                   Crime,Drama              R         3h 22m   
6        Action,Adventure,Drama          PG-13         3h 21m   
8        Action,Adventure,Drama          PG-13         2h 58m   
9             Adventure,Western       Approved         2h 58m   
12       Action,Adventure,Drama          PG-13         2h 59m   
15                Action,Sci-Fi              R         2h 16m   
21         Crime,Drama,Thriller              R         1h 58m   
26          Crime,Drama,Fantasy              R          3h 9m   
31        Biography,Drama,Music              R         2h 30m   
35    Animation,Adventure,Drama              G         1h 28m   
38         Crime,Drama,Thriller              R         2h 31m   
39          Crime,Drama,Mystery              R         1h 46m   
40         Drama,Mystery,Sci-Fi          PG-13         2h 10m   
45       Biography,Comedy,Drama              R         1h 52m   
57       Drama,Mystery,Thriller              R         2h 17m   
60                 Drama,Horror              R         2h 26m   
61             Comedy,Drama,War              G          2h 5m   
68                 Action,Drama          PG-13         2h 44m   
76                    Drama,War  Not Available  Not Available   
93                        Drama              R         1h 55m   
101        Comedy,Drama,Romance       Approved          2h 5m   
111          Comedy,Crime,Drama             PG          2h 9m   
127         Comedy,Drama,Family         Passed          1h 8m   
129               Drama,Mystery          PG-13         1h 37m   
131      Biography,Comedy,Crime              R             3h   
137                Comedy,Drama             PG         1h 43m   
140      Drama,Mystery,Thriller          PG-13         1h 47m   
145     Adventure,Drama,Western         Passed          2h 6m   
147     Adventure,Drama,History       Approved         2h 52m   
152       Horror,Mystery,Sci-Fi              R         1h 49m   
154             Biography,Drama             PG          2h 4m   
162       Drama,Mystery,Romance              R          2h 9m   
165         Adventure,Drama,War             PG         2h 41m   
176      Adventure,Comedy,Drama         Passed         1h 35m   
184      Adventure,Comedy,Crime              R         1h 39m   
186     Action,Adventure,Comedy         Passed          1h 7m   
187  Film-Noir,Mystery,Thriller       Approved         1h 33m   
189                   Drama,War              R          3h 3m   
192    Adventure,Drama,Thriller      Not Rated         2h 11m   
198               Drama,Fantasy      Not Rated         1h 36m   
205                Comedy,Crime              R         1h 57m   
207     Biography,Drama,History         Passed         1h 54m   
214               Action,Sci-Fi              R         1h 47m   
221    Adventure,Family,Fantasy              G         1h 42m   
224           Drama,Romance,War       Approved         2h 50m   
225                      Horror              R          2h 2m   
226  Animation,Action,Adventure             PG         1h 55m   
229                   Drama,War      Not Rated          2h 1m   
232                       Drama         Passed          2h 9m   
238      Drama,Romance,Thriller      Not Rated         2h 25m   
239                 Crime,Drama      Not Rated         1h 39m   
240      Biography,Drama,Family              G         2h 52m   
244  Animation,Action,Adventure             PG         1h 26m   
245                       Drama          PG-13         2h 26m   

                                               tagline         budget  \
0    Fear can hold you prisoner. Hope can set you f...       25000000   
1                           An offer you can't refuse.        6000000   
2                                      Why So Serious?      185000000   
3         All the power on earth can't change destiny.       13000000   
6                      The eye of the enemy is moving.       94000000   
8                             The Legend Comes to Life       93000000   
9    They formed an alliance of hate to steal a for...        1200000   
12                              A New Power Is Rising.       94000000   
15                                      Free your mind       63000000   
21   Dr. Hannibal Lecter. Brilliant. Cunning. Psych...       19000000   
26                                 Miracles do happen.       60000000   
31   Music was his passion. Survival was his master...       35000000   
35   See it for the first time ever in 3D (2011 3D ...       45000000   
38   Lies. Betrayal. Sacrifice. How far will you ta...       90000000   
39   The greatest trick the devil ever pulled was t...        6000000   
40                 A Friendship That Became a Rivalry.       40000000   
45   Sometimes you have to reach into someone else'...        9500000   
57   Before the Fall of the Berlin Wall, East Germa...        2000000   
60     Iconic terror from the No 1 bestselling writer.       19000000   
61                             The Comedy Masterpiece!        2000000   
68                                     The Legend Ends      250000000   
76   This is the story of 42 raw recruits caught up...    EM 32000000   
93                               The lie is spreading.  Not Available   
101  Movie-wise, there has never been anything like...        3000000   
111  Recapture "the STING Experience". REMEMBER HOW...        5500000   
127  This is the great film he has been working on ...         250000   
129                             Nothing is as it seems        6000000   
131                                Earn. Spend. Party.      100000000   
137                         All the world's a stage...       60000000   
140                                "I see dead people"       40000000   
145         Storming to a New High in High Adventure !        3000000   
147  put a fence in front of these men...and they'l...        4000000   
152                         Anytime. Anywhere. Anyone.       15000000   
154  An incredible but true story... probably this ...        5000000   
162  Un crimen sin castigo. Un amor puro. Una histo...  Not Available   
165  The towering triumph of adventure from the mak...        3000000   
176  "The Picture I Want to Be Remembered by." -Cha...         923000   
184                                 ventureComedyCrime       25000000   
186  Buster drives "The General" to trainload of la...         750000   
187                      Carol Reed's Classic Thriller  Not Available   
189  One of the most important and powerful films o...       15000000   
192  The complete restored version of the 1953 Fren...  Not Available   
198  A film of visual scope, of imaginative concept...         150000   
205  Hay quienes tratan de ganarse la vida sin move...       15000000   
207                 JOAN of ARC PICTURES Inc. presents  Not Available   
214  La sua missione e una sola: distruggere, uccid...        6400000   
221             Mighty Miracle Show Of 1000 Delights !        2777000   
224  THE SCREEN'S GREATEST LOVE STORY IS THE BEST F...        2100000   
225  The movie you've been waiting for...without th...       11000000   
226                                       Save The Day       92000000   
229  The French Colonel...who was forced even to to...         800000   
232  The thousands who have read the book will know...         800000   
238  Never did they expect to get into a controvers...  Not Available   
239  From the Vanguard of New Film-Makers Comes an ...  Not Available   
240  RADIANCE THAT FLOODS THE SCREEN...AND WARMS TH...        8200000   
244                  Some secrets are too huge to hide       70000000   
245                      Change begins with a whisper.       25000000   

             box_office                                              casts  \
0              28884504  Tim Robbins,Morgan Freeman,Bob Gunton,William ...   
1             250341816  Marlon Brando,Al Pacino,James Caan,Diane Keato...   
2            1006234167  Christian Bale,Heath Ledger,Aaron Eckhart,Mich...   
3              47961919  Al Pacino,Robert De Niro,Robert Duvall,Diane K...   
6            1146457748  Elijah Wood,Viggo Mortensen,Ian McKellen,Orlan...   
8             898204420  Elijah Wood,Ian McKellen,Orlando Bloom,Sean Be...   
9              25253887  Clint Eastwood,Eli Wallach,Lee Van Cleef,Aldo ...   
12            947944270  Elijah Wood,Ian McKellen,Viggo Mortensen,Orlan...   
15            467222728  Keanu Reeves,Laurence Fishburne,Carrie-Anne Mo...   
21            272742922  Jodie Foster,Anthony Hopkins,Lawrence A. Bonne...   
26            286801374  Tom Hanks,Michael Clarke Duncan,David Morse,Bo...   
31            120072577  Adrien Brody,Thomas Kretschmann,Frank Finlay,E...   
35            968511805  Matthew Broderick,Jeremy Irons,James Earl Jone...   
38            291480452  Leonardo DiCaprio,Matt Damon,Jack Nicholson,Ma...   
39             23341568  Kevin Spacey,Gabriel Byrne,Chazz Palminteri,St...   
40            109676311  Christian Bale,Hugh Jackman,Scarlett Johansson...   
45            426588510  François Cluzet,Omar Sy,Anne Le Ny,Audrey Fleu...   
57             77356942  Ulrich Mühe,Martina Gedeck,Sebastian Koch,Ulri...   
60             47335804  Jack Nicholson,Shelley Duvall,Danny Lloyd,Scat...   
61               970263  Charles Chaplin,Paulette Goddard,Jack Oakie,Re...   
68           1081169825  Christian Bale,Tom Hardy,Anne Hathaway,Gary Ol...   
76             11487676  Jürgen Prochnow,Herbert Grönemeyer,Klaus Wenne...   
93        Not Available  Mads Mikkelsen,Thomas Bo Larsen,Annika Wedderk...   
101            18778738  Jack Lemmon,Shirley MacLaine,Fred MacMurray,Ra...   
111           156000000  Paul Newman,Robert Redford,Robert Shaw,Charles...   
127               41960  Charles Chaplin,Edna Purviance,Jackie Coogan,C...   
129            24427162  Anthony Hopkins,Olivia Colman,Mark Gatiss,Oliv...   
131           406878233  Leonardo DiCaprio,Jonah Hill,Margot Robbie,Mat...   
137           264118201  Jim Carrey,Ed Harris,Laura Linney,Noah Emmeric...   
140           672806432  Bruce Willis,Haley Joel Osment,Toni Collette,O...   
145             5014000  Humphrey Bogart,Walter Huston,Tim Holt,Bruce B...   
147              228178  Steve McQueen,James Garner,Richard Attenboroug...   
152            19632715  Kurt Russell,Wilford Brimley,Keith David,Richa...   
154            26023860  Anthony Hopkins,John Hurt,Anne Bancroft,John G...   
162       Not Available  Ricardo Darín,Soledad Villamil,Pablo Rago,Carl...   
165            27200000  William Holden,Alec Guinness,Jack Hawkins,Sess...   
176               29328  Charles Chaplin,Mack Swain,Tom Murray,Henry Be...   
184           173082189  Ralph Fiennes,F. Murray Abraham,Mathieu Amalri...   
186  750000 (estimated)  Buster Keaton,Marion Mack,Glen Cavender,Jim Fa...   
187             1226507  Orson Welles,Joseph Cotten,Alida Valli,Trevor ...   
189            49074379  Robert De Niro,Christopher Walken,John Cazale,...   
192                1098  Yves Montand,Charles Vanel,Peter van Eyck,Folc...   
198              311212  Max von Sydow,Gunnar Björnstrand,Bengt Ekerot,...   
205            46969409  Jeff Bridges,John Goodman,Julianne Moore,Steve...   
207       Not Available  Maria Falconetti,Eugene Silvain,André Berley,M...   
214            78371200  Arnold Schwarzenegger,Linda Hamilton,Michael B...   
221            25637669  Judy Garland,Frank Morgan,Ray Bolger,Bert Lahr...   
224            23661347  Myrna Loy,Dana Andrews,Fredric March,Teresa Wr...   
225           441306145  Ellen Burstyn,Max von Sydow,Linda Blair,Lee J....   
226           631607053  Craig T. Nelson,Samuel L. Jackson,Holly Hunter...   
229              962002  Brahim Hadjadj,Jean Martin,Yacef Saadi,Samia K...   
232  800000 (estimated)  Henry Fonda,Jane Darwell,John Carradine,Charle...   
238       Not Available  Kim Min-hee,Ha Jung-woo,Cho Jin-woong,Moon So-...   
239              127244  Jean-Pierre Léaud,Albert Rémy,Claire Maurier,G...   
240           159428329  Julie Andrews,Christopher Plummer,Eleanor Park...   
244            23335817  Eli Marienthal,Harry Connick Jr.,Jennifer Anis...   
245           216639112  Viola Davis,Emma Stone,Octavia Spencer,Bryce D...   

                                             directors  \
0                                       Frank Darabont   
1                                 Francis Ford Coppola   
2                                    Christopher Nolan   
3                                 Francis Ford Coppola   
6                                        Peter Jackson   
8                                        Peter Jackson   
9                                         Sergio Leone   
12                                       Peter Jackson   
15                      Lana Wachowski,Lilly Wachowski   
21                                      Jonathan Demme   
26                                      Frank Darabont   
31                                      Roman Polanski   
35                            Roger Allers,Rob Minkoff   
38                                     Martin Scorsese   
39                                        Bryan Singer   
40                                   Christopher Nolan   
45                       Olivier Nakache,Éric Toledano   
57                    Florian Henckel von Donnersmarck   
60                                     Stanley Kubrick   
61                                     Charles Chaplin   
68                                   Christopher Nolan   
76                                   Wolfgang Petersen   
93                                   Thomas Vinterberg   
101                                       Billy Wilder   
111                                    George Roy Hill   
127                                    Charles Chaplin   
129                                     Florian Zeller   
131                                    Martin Scorsese   
137                                         Peter Weir   
140                                 M. Night Shyamalan   
145                                        John Huston   
147                                       John Sturges   
152                                     John Carpenter   
154                                        David Lynch   
162                               Juan José Campanella   
165                                         David Lean   
176                                    Charles Chaplin   
184                                       Wes Anderson   
186                       Clyde Bruckman,Buster Keaton   
187                                         Carol Reed   
189                                     Michael Cimino   
192                              Henri-Georges Clouzot   
198                                     Ingmar Bergman   
205                   Joel Coen,Ethan Coen(uncredited)   
207                                Carl Theodor Dreyer   
214                                      James Cameron   
221  Victor Fleming,George Cukor(uncredited),Mervyn...   
224                                      William Wyler   
225                                   William Friedkin   
226                                          Brad Bird   
229                                   Gillo Pontecorvo   
232                                          John Ford   
238                                     Park Chan-wook   
239                                  François Truffaut   
240                                        Robert Wise   
244                                          Brad Bird   
245                                        Tate Taylor   

                                               writers  
0                          Stephen King,Frank Darabont  
1                      Mario Puzo,Francis Ford Coppola  
2      Jonathan Nolan,Christopher Nolan,David S. Goyer  
3                      Francis Ford Coppola,Mario Puzo  
6            J.R.R. Tolkien,Fran Walsh,Philippa Boyens  
8            J.R.R. Tolkien,Fran Walsh,Philippa Boyens  
9     Luciano Vincenzoni,Sergio Leone,Agenore Incrocci  
12           J.R.R. Tolkien,Fran Walsh,Philippa Boyens  
15                      Lilly Wachowski,Lana Wachowski  
21                             Thomas Harris,Ted Tally  
26                         Stephen King,Frank Darabont  
31                   Ronald Harwood,Wladyslaw Szpilman  
35      Irene Mecchi,Jonathan Roberts,Linda Woolverton  
38                William Monahan,Alan Mak,Felix Chong  
39                               Christopher McQuarrie  
40   Jonathan Nolan,Christopher Nolan,Christopher P...  
45   Olivier Nakache,Éric Toledano,Philippe Pozzo d...  
57                    Florian Henckel von Donnersmarck  
60          Stephen King,Stanley Kubrick,Diane Johnson  
61                                     Charles Chaplin  
68     Jonathan Nolan,Christopher Nolan,David S. Goyer  
76                Wolfgang Petersen,Lothar G. Buchheim  
93                   Thomas Vinterberg,Tobias Lindholm  
101                        Billy Wilder,I.A.L. Diamond  
111                                      David S. Ward  
127                                    Charles Chaplin  
129                 Christopher Hampton,Florian Zeller  
131                      Terence Winter,Jordan Belfort  
137                                      Andrew Niccol  
140                                 M. Night Shyamalan  
145                              John Huston,B. Traven  
147          Paul Brickhill,James Clavell,W.R. Burnett  
152                Bill Lancaster,John W. Campbell Jr.  
154       Christopher De Vore,Eric Bergren,David Lynch  
162               Eduardo Sacheri,Juan José Campanella  
165          Pierre Boulle,Carl Foreman,Michael Wilson  
176                                    Charles Chaplin  
184            Stefan Zweig,Wes Anderson,Hugo Guinness  
186           Buster Keaton,Clyde Bruckman,Al Boasberg  
187         Graham Greene,Orson Welles,Alexander Korda  
189      Michael Cimino,Deric Washburn,Louis Garfinkle  
192  Georges Arnaud,Henri-Georges Clouzot,Jérôme Gé...  
198                                     Ingmar Bergman  
205                               Ethan Coen,Joel Coen  
207                 Joseph Delteil,Carl Theodor Dreyer  
214        James Cameron,Gale Anne Hurd,William Wisher  
221    Noel Langley,Florence Ryerson,Edgar Allan Woolf  
224                Robert E. Sherwood,MacKinlay Kantor  
225                               William Peter Blatty  
226                                          Brad Bird  
229                    Franco Solinas,Gillo Pontecorvo  
232                    Nunnally Johnson,John Steinbeck  
238        Sarah Waters,Chung Seo-kyung,Park Chan-wook  
239                    François Truffaut,Marcel Moussy  
240        Georg Hurdalek,Howard Lindsay,Russel Crouse  
244                 Tim McCanlies,Brad Bird,Ted Hughes  
245                       Tate Taylor,Kathryn Stockett
"""