# Display the movies whose taglines end with a ? or !

import pandas as pd

df = pd.read_csv('IMDB Top 250 Movies.csv')
pd.set_option('display.max_columns', None)

tagline_end = df[(df['tagline'].str.endswith('?')) | (df['tagline'].str.endswith('!'))]
print(tagline_end)


"""Output:
     rank                              name  year  rating  \
2       3                   The Dark Knight  2008     9.0   
4       5                      12 Angry Men  1957     9.0   
7       8                      Pulp Fiction  1994     8.9   
11     12                        Fight Club  1999     8.8   
17     18   One Flew Over the Cuckoo's Nest  1975     8.7   
19     20                     Seven Samurai  1954     8.6   
38     39                      The Departed  2006     8.5   
42     43                        Casablanca  1942     8.5   
44     45                          Harakiri  1962     8.6   
46     47                      Modern Times  1936     8.5   
59     60                    Paths of Glory  1957     8.4   
61     62                The Great Dictator  1940     8.4   
63     64       Witness for the Prosecution  1957     8.4   
86     87                      High and Low  1963     8.4   
95     96                                 M  1931     8.3   
96     97                Lawrence of Arabia  1962     8.3   
97     98                North by Northwest  1959     8.3   
98     99                           Vertigo  1958     8.3   
99    100                             Ikiru  1952     8.3   
101   102                     The Apartment  1960     8.3   
102   103                A Clockwork Orange  1971     8.3   
109   110             To Kill a Mockingbird  1962     8.3   
117   118                          Die Hard  1988     8.2   
120   121                   Bicycle Thieves  1948     8.3   
124   125                            Dangal  2016     8.3   
130   131                     All About Eve  1950     8.2   
133   134             Judgment at Nuremberg  1961     8.3   
136   137                   Pan's Labyrinth  2006     8.2   
144   145                           Yojimbo  1961     8.2   
145   146  The Treasure of the Sierra Madre  1948     8.2   
151   152                          Rashomon  1950     8.2   
161   162                 Dial M for Murder  1954     8.2   
166   167                     Trainspotting  1996     8.1   
174   175                Children of Heaven  1997     8.2   
177   178                    Before Sunrise  1995     8.1   
181   182                 On the Waterfront  1954     8.1   
189   190                   The Deer Hunter  1978     8.1   
194   195                      Sherlock Jr.  1924     8.2   
210   211                             Rocky  1976     8.1   
218   219                           Network  1976     8.1   
220   221                     Before Sunset  2004     8.1   
221   222                  The Wizard of Oz  1939     8.1   
224   225       The Best Years of Our Lives  1946     8.1   
229   230             The Battle of Algiers  1966     8.1   
232   233               The Grapes of Wrath  1940     8.1   
240   241                The Sound of Music  1965     8.1   
241   242             It Happened One Night  1934     8.1   

                         genre certificate run_time  \
2           Action,Crime,Drama       PG-13   2h 32m   
4                  Crime,Drama    Approved   1h 36m   
7                  Crime,Drama           R   2h 34m   
11                       Drama           R   2h 19m   
17                       Drama         18+   2h 13m   
19                Action,Drama   Not Rated   3h 27m   
38        Crime,Drama,Thriller           R   2h 31m   
42           Drama,Romance,War          PG   1h 42m   
44        Action,Drama,Mystery   Not Rated   2h 13m   
46        Comedy,Drama,Romance           G   1h 27m   
59                   Drama,War    Approved   1h 28m   
61            Comedy,Drama,War           G    2h 5m   
63         Crime,Drama,Mystery    Approved   1h 56m   
86         Crime,Drama,Mystery   Not Rated   2h 23m   
95      Crime,Mystery,Thriller      Passed   1h 39m   
96   Adventure,Biography,Drama    Approved   3h 38m   
97    Action,Adventure,Mystery    Approved   2h 16m   
98    Mystery,Romance,Thriller          PG    2h 8m   
99                       Drama   Not Rated   2h 23m   
101       Comedy,Drama,Romance    Approved    2h 5m   
102               Crime,Sci-Fi           X   2h 16m   
109                Crime,Drama    Approved    2h 9m   
117            Action,Thriller           R   2h 12m   
120                      Drama   Not Rated   1h 29m   
124     Action,Biography,Drama   Not Rated   2h 41m   
130                      Drama      Passed   2h 18m   
133                  Drama,War    Approved   2h 59m   
136          Drama,Fantasy,War           R   1h 58m   
144      Action,Drama,Thriller   Not Rated   1h 50m   
145    Adventure,Drama,Western      Passed    2h 6m   
151        Crime,Drama,Mystery   Not Rated   1h 28m   
161             Crime,Thriller          PG   1h 45m   
166                      Drama           R   1h 33m   
174         Drama,Family,Sport          PG   1h 29m   
177              Drama,Romance           R   1h 41m   
181       Crime,Drama,Thriller    Approved   1h 48m   
189                  Drama,War           R    3h 3m   
194      Action,Comedy,Romance      Passed      45m   
210                Drama,Sport          PG       2h   
218                      Drama           R    2h 1m   
220              Drama,Romance           R   1h 20m   
221   Adventure,Family,Fantasy           G   1h 42m   
224          Drama,Romance,War    Approved   2h 50m   
229                  Drama,War   Not Rated    2h 1m   
232                      Drama      Passed    2h 9m   
240     Biography,Drama,Family           G   2h 52m   
241             Comedy,Romance      Passed   1h 45m   

                                               tagline         budget  \
2                                      Why So Serious?      185000000   
4    Life Is In Their Hands -- Death Is On Their Mi...         350000   
7    Girls like me don't make invitations like this...        8000000   
11   How much can you know about yourself if you've...       63000000   
17             If he's crazy, what does that make you?        3000000   
19   Will Take Its Place With the Seven Greatest Fi...      125000000   
38   Lies. Betrayal. Sacrifice. How far will you ta...       90000000   
42                Where Love Cuts as Deep as a Dagger!         950000   
44   The World Has Never Understood Why the Japanes...  Not Available   
46   He stands alone as the greatest entertainer of...        1500000   
59   Never has the screen thrust so deeply into the...         935000   
61                             The Comedy Masterpiece!        2000000   
63    The most electrifying entertainment of our time!        3000000   
86      142 Screenful Minutes of Thrills and Suspense!  Not Available   
95   IT STAGGERS THE SENSES!...SHOCKS the Imaginati...  Not Available   
96    A Mighty Motion Picture Of Action And Adventure!       15000000   
97   Alfred Hitchcock takes you.... North by Northw...        3101000   
98   A Hitchcock thriller. You should see it from t...        2479000   
99                 One of the Great Films of Our Time!  Not Available   
101  Movie-wise, there has never been anything like...        3000000   
102  Being the adventures of a young man ... who co...        2200000   
109  The most beloved and widely read Pulitzer Priz...        2000000   
117  It will blow you through the back wall of the ...       28000000   
120             The Prize Picture They Want to Censor!         133000   
124      You think our girls are any lesser than boys?  Not Available   
130              It's all about women---and their men!        1400000   
133  More than a motion picture...It is an overwhel...        3000000   
136  What happens when make-believe believes it's r...       19000000   
144  Better if all these men were dead. Think about...  Not Available   
145         Storming to a New High in High Adventure !        3000000   
151             The husband, the wife...or the bandit?         250000   
161           Kiss By Kiss...Supreme Suspense Unfurls!        1400000   
166  Choose life. Choose a job. Choose a starter ho...        1500000   
174         A Little Secret...Their Biggest Adventure!  Not Available   
177  Jump on and live a Eurorail journey you will n...        2500000   
181      The Man Lived by the Jungle Law of the Docks!         910000   
189  One of the most important and powerful films o...       15000000   
194          every inch of footage holds such a laugh!  Not Available   
210  You have a ringside seat for the bloodiest bic...         960000   
218  "NETWORK"... the humanoids, the love story, th...        3800000   
220  What if you had a second chance with the one t...  Not Available   
221             Mighty Miracle Show Of 1000 Delights !        2777000   
224  THE SCREEN'S GREATEST LOVE STORY IS THE BEST F...        2100000   
229  The French Colonel...who was forced even to to...         800000   
232  The thousands who have read the book will know...         800000   
240  RADIANCE THAT FLOODS THE SCREEN...AND WARMS TH...        8200000   
241  Two great lovers of the screen in the grandest...         325000   

             box_office                                              casts  \
2            1006234167  Christian Bale,Heath Ledger,Aaron Eckhart,Mich...   
4                   955  Henry Fonda,Lee J. Cobb,Martin Balsam,John Fie...   
7             213928762  John Travolta,Uma Thurman,Samuel L. Jackson,Br...   
11            101209702  Brad Pitt,Edward Norton,Meat Loaf,Zach Grenier...   
17            109114817  Jack Nicholson,Louise Fletcher,Michael Berryma...   
19               346258  Toshirô Mifune,Takashi Shimura,Keiko Tsushima,...   
38            291480452  Leonardo DiCaprio,Matt Damon,Jack Nicholson,Ma...   
42              4626532  Humphrey Bogart,Ingrid Bergman,Paul Henreid,Cl...   
44        Not Available  Tatsuya Nakadai,Akira Ishihama,Shima Iwashita,...   
46               463618  Charles Chaplin,Paulette Goddard,Henry Bergman...   
59                 5252  Kirk Douglas,Ralph Meeker,Adolphe Menjou,Georg...   
61               970263  Charles Chaplin,Paulette Goddard,Jack Oakie,Re...   
63                 7693  Tyrone Power,Marlene Dietrich,Charles Laughton...   
86        Not Available  Toshirô Mifune,Yutaka Sada,Tatsuya Nakadai,Kyô...   
95                35566  Peter Lorre,Ellen Widmann,Inge Landgut,Otto We...   
96             45720631  Peter O'Toole,Alec Guinness,Anthony Quinn,Jack...   
97               142319  Cary Grant,Eva Marie Saint,James Mason,Jessie ...   
98              7798146  James Stewart,Kim Novak,Barbara Bel Geddes,Tom...   
99                96302  Takashi Shimura,Nobuo Kaneko,Shin'ichi Himori,...   
101            18778738  Jack Lemmon,Shirley MacLaine,Fred MacMurray,Ra...   
102            26960374  Malcolm McDowell,Patrick Magee,Michael Bates,W...   
109              599146  Gregory Peck,John Megna,Frank Overton,Rosemary...   
117           141603197  Bruce Willis,Alan Rickman,Bonnie Bedelia,Regin...   
120              436655  Lamberto Maggiorani,Enzo Staiola,Lianella Care...   
124       Not Available  Aamir Khan,Sakshi Tanwar,Fatima Sana Shaikh,Sa...   
130              151052  Bette Davis,Anne Baxter,George Sanders,Celeste...   
133               12180  Spencer Tracy,Burt Lancaster,Richard Widmark,M...   
136            83862032  Ivana Baquero,Ariadna Gil,Sergi López,Maribel ...   
144               46808  Toshirô Mifune,Eijirô Tôno,Tatsuya Nakadai,Yôk...   
145             5014000  Humphrey Bogart,Walter Huston,Tim Holt,Bruce B...   
151               81379  Toshirô Mifune,Machiko Kyô,Masayuki Mori,Takas...   
161               31207  Ray Milland,Grace Kelly,Robert Cummings,John W...   
166            16767475  Ewan McGregor,Ewen Bremner,Jonny Lee Miller,Ke...   
174       Not Available  Mohammad Amir Naji,Amir Farrokh Hashemian,Baha...   
177             5987386  Ethan Hawke,Julie Delpy,Andrea Eckert,Hanno Pö...   
181  910000 (estimated)  Marlon Brando,Karl Malden,Lee J. Cobb,Rod Stei...   
189            49074379  Robert De Niro,Christopher Walken,John Cazale,...   
194       Not Available  Buster Keaton,Kathryn McGuire,Joe Keaton,Erwin...   
210           117250402  Sylvester Stallone,Talia Shire,Burt Young,Carl...   
218            23690757  Faye Dunaway,William Holden,Peter Finch,Robert...   
220       Not Available  Ethan Hawke,Julie Delpy,Vernon Dobtcheff,Louis...   
221            25637669  Judy Garland,Frank Morgan,Ray Bolger,Bert Lahr...   
224            23661347  Myrna Loy,Dana Andrews,Fredric March,Teresa Wr...   
229              962002  Brahim Hadjadj,Jean Martin,Yacef Saadi,Samia K...   
232  800000 (estimated)  Henry Fonda,Jane Darwell,John Carradine,Charle...   
240           159428329  Julie Andrews,Christopher Plummer,Eleanor Park...   
241               11477  Clark Gable,Claudette Colbert,Walter Connolly,...   

                                             directors  \
2                                    Christopher Nolan   
4                                         Sidney Lumet   
7                                    Quentin Tarantino   
11                                       David Fincher   
17                                        Milos Forman   
19                                      Akira Kurosawa   
38                                     Martin Scorsese   
42                                      Michael Curtiz   
44                                    Masaki Kobayashi   
46                                     Charles Chaplin   
59                                     Stanley Kubrick   
61                                     Charles Chaplin   
63                                        Billy Wilder   
86                                      Akira Kurosawa   
95                                          Fritz Lang   
96                                          David Lean   
97                                    Alfred Hitchcock   
98                                    Alfred Hitchcock   
99                                      Akira Kurosawa   
101                                       Billy Wilder   
102                                    Stanley Kubrick   
109                                    Robert Mulligan   
117                                     John McTiernan   
120                                   Vittorio De Sica   
124                                      Nitesh Tiwari   
130                               Joseph L. Mankiewicz   
133                                     Stanley Kramer   
136                                 Guillermo del Toro   
144                                     Akira Kurosawa   
145                                        John Huston   
151                                     Akira Kurosawa   
161                                   Alfred Hitchcock   
166                                        Danny Boyle   
174                                       Majid Majidi   
177                                  Richard Linklater   
181                                         Elia Kazan   
189                                     Michael Cimino   
194                                      Buster Keaton   
210                                   John G. Avildsen   
218                                       Sidney Lumet   
220                                  Richard Linklater   
221  Victor Fleming,George Cukor(uncredited),Mervyn...   
224                                      William Wyler   
229                                   Gillo Pontecorvo   
232                                          John Ford   
240                                        Robert Wise   
241                                        Frank Capra   

                                               writers  
2      Jonathan Nolan,Christopher Nolan,David S. Goyer  
4                                        Reginald Rose  
7                        Quentin Tarantino,Roger Avary  
11                            Chuck Palahniuk,Jim Uhls  
17                Lawrence Hauben,Bo Goldman,Ken Kesey  
19        Akira Kurosawa,Shinobu Hashimoto,Hideo Oguni  
38                William Monahan,Alan Mak,Felix Chong  
42     Julius J. Epstein,Philip G. Epstein,Howard Koch  
44                Yasuhiko Takiguchi,Shinobu Hashimoto  
46                                     Charles Chaplin  
59      Stanley Kubrick,Calder Willingham,Jim Thompson  
61                                     Charles Chaplin  
63          Agatha Christie,Billy Wilder,Harry Kurnitz  
86          Hideo Oguni,Ryûzô Kikushima,Eijirô Hisaita  
95           Thea von Harbou,Fritz Lang,Egon Jacobsohn  
96                          Robert Bolt,Michael Wilson  
97                                       Ernest Lehman  
98         Alec Coppel,Samuel A. Taylor,Pierre Boileau  
99        Akira Kurosawa,Shinobu Hashimoto,Hideo Oguni  
101                        Billy Wilder,I.A.L. Diamond  
102                    Stanley Kubrick,Anthony Burgess  
109                            Harper Lee,Horton Foote  
117       Roderick Thorp,Jeb Stuart,Steven E. de Souza  
120   Cesare Zavattini,Luigi Bartolini,Oreste Biancoli  
124          Piyush Gupta,Shreyas Jain,Nikhil Mehrotra  
130                      Joseph L. Mankiewicz,Mary Orr  
133                         Abby Mann,Montgomery Clift  
136                                 Guillermo del Toro  
144                     Akira Kurosawa,Ryûzô Kikushima  
145                              John Huston,B. Traven  
151  Ryûnosuke Akutagawa,Akira Kurosawa,Shinobu Has...  
161                                    Frederick Knott  
166                            Irvine Welsh,John Hodge  
174                                       Majid Majidi  
177                       Richard Linklater,Kim Krizan  
181      Budd Schulberg,Malcolm Johnson,Robert Siodmak  
189      Michael Cimino,Deric Washburn,Louis Garfinkle  
194    Jean C. Havez,Joseph A. Mitchell,Clyde Bruckman  
210                                 Sylvester Stallone  
218                                    Paddy Chayefsky  
220          Richard Linklater,Julie Delpy,Ethan Hawke  
221    Noel Langley,Florence Ryerson,Edgar Allan Woolf  
224                Robert E. Sherwood,MacKinlay Kantor  
229                    Franco Solinas,Gillo Pontecorvo  
232                    Nunnally Johnson,John Steinbeck  
240        Georg Hurdalek,Howard Lindsay,Russel Crouse  
241                 Robert Riskin,Samuel Hopkins Adams
"""