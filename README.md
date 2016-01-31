# Python Final Assignment
#### Roger Lo
The query.py file provides functions for querying some statistics regarding the master thesis from the Faculty of Humanities at VU Amsterdam compiled in 2015.

Before more information is provided for the functions, it is useful to briefly examine some features and structure of the data.

## Data
The folder ```./thesis_vu_2015``` contains the master theses from the following programs.

#### Programs and Languages
The abbreviation for each program can be used in the querying functions.
* **arch**: Archaeology
* **ciw**: Communication and Informatics
* **erf**: Heritage Studies
* **esmus**: Museum Conservator
* **fil**: Philosophy
* **ges**: History
* **kcw**: Arts and Culture
* **ltk**: Literary Studies
* **ohs**: Classics and Ancient Civilizations
* **ph**: Philosophy of Management and Organizations
* **rgs**: History (Research)
* **rkcw**: Arts and Culture (Research)
* **rltk**: Literary Studies (Research)
* **rohs**: Classics and Ancient Civilizations (Research)
* **rtlw**: Linguistics (Research)
* **tlw**: Linguistics

All theses are written in English or Dutch.
* **en**: English
* **nl**: Dutch

#### XML format
Theses are stored in .naf files, which have an XML structure shown in the following diagram.

![XML structure](http://screenshot.net/mo7e0s3?tw)

*Note that the thesis by Ruben Verhagen in ```./thesis_vu_2015/fil/en``` is an empty file. Please delete this thesis before running the functions, otherwise the functions will raise an error.*

## Query Functions
All the functions are in the query.py file. Please make sure the query.py file and the current running .py file are saved in the same directory as the folder ```./thesis_vu_2015``` (**NOT IN** the folder ```./thesis_vu_2015```) before importing and using the functions.

The module can be imported using the following code:
```python
import query
```

#### Average Number of Tokens or Types
We can use the function ```average_number``` to get the average number of tokens or types of the theses in the specified program(s) and language(s). For example, if we want to query the average number of tokens of the these in the programs Linguistics and Linguistics (Research) written in English, we can use the code:
```python
query.average_number("token", program=["tlw", "rtlw"], language=["en"])
```

This function prints the output:
```python
25058.2
```

Similarly, to query the average number of types of the same theses, we use the code:
```python
query.average_number("type", program=["tlw", "rtlw"], language=["en"]) # Output: 2026.6
```
Please notice the syntax and type of the arguments here:
* ```"token"``` or ```"type"``` have to be a single string.
* ```program``` has to be a list of string(s) indicating the program(s), e.g., ```["arch"]```.
* ```language``` has to be a list of string(s) indicating the language(s), e.g., ```["en", "nl"]```.

Please stick to this syntax and type when using the function. (Later functions also share a similar syntax.) Failing to observe this practice will result in errors.

#### Average Number of Sentences
The function ```average_number_sent``` can be used to query this statistic. For instance, if we want to get the average number of sentences in the these from the programs History and History (Research) in both English and Dutch, then we can use the following code:
```python
query.average_number_sent(program=["ges", "rgs"], language=["en", "nl"])
```

Output:
```python
1211.1
```

#### 10 Longest Sentences
The function ```longest_sent``` prints the first ```n``` longest sentences from the theses specified. For example, if we want to know the first 10 longest sentences from the English theses compiled in the program Arts and Culture, use the following code:
```python
query.longest_sent(10, program=["kcw"], language=["en"])
```

Output is like this:
```python
Rank 1, 729 words, from thesis_vu_2015/kcw/en/Scriptie_Schilder_trim.txt.naf.nohyphen:
The answers to the questions briefly formulated per respondent Respondent1 Bart Eysink Smeets Topic Education Subtopic Motivation Desire to exert creativity ; he thought the Eindhoven Design Academy was the best for his this ; his parents also studied at the academy Influence of academy taking risks ; making things ; working according to traditional methods Disagreement with working according to traditional methods ; the importance of academy aesthetics , Development during opposing against the aesthetic design principles of the education academy ; designing objects/products with a story he wants to tell Topic Designing Subtopic Purpose , goals designing funny or weird objects/products which tell a story and make people think about a certain phenomenon ; it is about telling a story and think about it , not to believe it Sense of I have a sense of social responsibility , but that is not Responsibility directly related to my design principles ; I think people should be aware about their behaviour and about the objects and products they use ; Inspiration parents : they taught him that you have to start by solving an ( invented ) problem ; Helmut Smits ; Fons Schiedon ; Joep van Lieshout ; Maxim Hartman , Steven de Peven ; Gummbah ; absurdism ; 32 opinions ; a striking phenomenon ; seeing things different than they are , in a different context Principles it is not about aesthetics ; it s too easy to make something beautiful ; honesty is more important than responsibility ; people should understand the object/product ; the story or concept of the object/product is most important , not the material ; Material use does not always matter ; most important is that the story is clear ; sometimes a material can contribute to the story Production process starting point : solving a problem , you can invent a problem ; blowing up a phenomenon ; Topic Future Subtopic Ambitions I would like to make my own work and to work at an organisation , such as KesselsKramer where I work now ; not specific functional objects ; artworks ; Respondent 2 Luuk Wiehink Topic Education Subtopic Motivation studying fashion design at the first place , after the preliminary program decided to study product design ; ArtEZ appeared to be accessible ; nice teachers ; nice workplace Influence of academy the design process , material experiments , working according to traditional methods , exploring the possibilities of a material ; starting from the material Disagreement with once during a project : not having the possibility to develop academy your own theme ; some teachers were outdated , their visions on design , they did not work with new ; too much about working from traditional methods and too less connection with the industry and market Development during the user and society as starting point ; breaking the traditional education use of an object or material Topic Designing Subtopic Purpose , goals giving objects/materials a new destination , recycling objects/materials ; solving social problems ; designing functional objects ; Sense of responsibility contributing to society , making a better society/world , Inspiration materials , the user/society , traditional use of product/material ; ( responding to ) social issues Principles simplicity in form ; pure in form ; not hiding the construction , but showing the construction and the qualities of the material the designer is a manager , not a maker ; affordability Material use existing object/material ; organic material ; recycling materials ; Production process starting from an existing material , functional object or social problem ; experimenting with the material 33 Topic Future Subtopic Ambitions making more money with designing ; continuing my activities ; continuing working with the industry ; Respondent 3 Joris de Groot Topic Education Subtopic Motivation desire to design and make things not especially functional and for the industry only ; attracted by the workplace and the products made by students at ArtEZ , Influence of academy the story behind the product ; material experiments ; searching for new forms ; working with traditional methods ; Disagreement with teachers who pushed me too far to continue experimenting in academy the process , which gave me less time to make a final product Development during putting the material centre stage ; experimenting with education materials ; simple forms ; not much decoration ; Topic Designing Subtopic Purpose , goals showing the beauty and possibilities of existing hidden machines and techniques and the qualities of materials ; making new products for firms with their existing machines and expanding their target groups ; Sense of responsibility producing in the Netherlands because of the better social agreements and knowledge Inspiration firms who produce objects ; technologies to produce an object ; Principles functionality ; the designer has to take account for its product ; affordability Material use depending on the firm ; recycling left-over material Production process ( for my own pleasure ) I want to work and experiment with materials , techniques and machines . 

Rank 2, 299 words, from thesis_vu_2015/kcw/en/Droog_and_Dutch_Design_-_Master_Thesis_by_Nina_Klijs_trim.txt.naf.nohyphen:
Utrecht , 9 June 2015 Nina Klijs Droog and Dutch Design Thesis by Nina Maria Klijs 4 TABLE OF CONTENT 1 Introduction 1.1 Introduction to the research 6 - - 7 1.2 Relevance and limitation of the research 7 1.3 Structure of the research 8 2 Literature Review 2.1 Defining Droog Design 9 - - 10 2.2 The construction of a narrative 10 11 2.3 The manifestation of Dutch Design as separate entity 11 - - 12 2.4 A critical stance regarding Droog and Dutch Design 12 - - 14 2.5 Conclusion 14 - - 15 3 Theoretical and methodological framework 3.1 Discourse analysis within new museology 16 - - 17 3.2 Methodology 18 3.3 Details about data collection 18 - - 19 4 Politics part I : the policy and activities of the Centraal Museum 4.1 The Centraal Museum 20 4.2 Policy of the Centraal Museum 20 - - 21 4.3 Policy with regard to the collection Applied Arts 22 - - 23 4.4 Acquisition activities with regard to the collection Applied Arts 23 - - 24 4.5 Exhibition activities with regard to the collection Apllied Arts 24 26 4.5 Policy with regard to traveling exhibitions 26 - - 27 5 Politics part II : the roles and interests surrounding the creation of the exhibition 5.1 The events that preceded the exhibition 28 - - 29 5.2 The role and interests of the Mondriaan Foundation 29 - - 31 5.3 The role and interests of the Living Design Centre OZONE 31 - - 33 Droog and Dutch Design Thesis by Nina Maria Klijs 5 5.4 The role and interests of Droog Design 33 5.5 The roles and interests of the Centraal Museum s curators 33 - - 34 5.5.1 The role and interests of Fashion and Costume curator Jos Teunissen 34 - - 36 5.5.2 The role and interests of Applied Arts and Design curator Ida van Zijl 36 - - 37 6 Poetics : the production of meaning within the context of the exhibition 6.1 The structure of the exhibition 38 6.2 The production of meaning in the catalogue s content 38 42 6.3 The production of meaning in the catalogue s graphic design 42 44 6.4 The production of meaning in the exhibition s spatial design 44 - - 48 7 Conclusion 49 - - 51 Bibliography 52 - - 54 Appendix A H ( interviews ) 55 - - 98 Appendix I ( Images ) 99 - - 103 Droog and Dutch Design Thesis by Nina Maria Klijs 6 1 INTRODUCTION 1.1 Introduction to the research When design fanatics from abroad are asked to define Dutch Design , one often hears keywords such as sober , conceptual and ironic . 

Rank 3, 282 words, from thesis_vu_2015/kcw/en/N._Pecht_scriptie_final_draft_trim.txt.naf.nohyphen:
Left wing and right wing found a consensus in Americanization : universalist tendencies that defined the mood of the fifties .43 Doneson affirms that Americanization was a goal for minorities : equality and freedom as conformity and assimilation were ideas to be found on both the left and the right , and that Jews began to mingle more with non-Jews and to assimilate into the mainstream of American society .44 This social-political atmosphere in America of the 1950s , reflected on the representation of minorities in popular culture during that time .45 37 Doneson , p. 59 38 Lev , p. 65 39 Plunka , p. 110 40 Doneson , p. 83 41 Ibid , Plunka , p. 110 42 Doneson , p. 64 43 Ibid. , p. 63 44 Ibid , p. 65 45 Ibid , p. 76 13 In the case of THE DIARY OF ANNE FRANK , this caused a de-emphasizing of the particular Jewish aspects of the story , according to Barnouw , Doneson , Plunka and Rosenfeld .46 On this , Alan Mintz states that Anne s Jewishness is , in the script of Goodrich and Hackett , not hidden , but made to seem inessential .47 As an example of this , Plunka states even the Hanukkah celebration is reduced to a generic festive ( read : non-Jewish ) celebration .48 This specific scene has been discussed often , as it was Goodrich and Hackett who decided to make the celebration the key ( and final ) scene of the first Act of a two-Act play , while Anne Frank wrote only two sentences about it in her diary .49 According to Doneson , Goodrich and Hackett used the scene to achieve audience identification .50 Doneson affirms that Hanukkah can be like Christmas , just a little different and that religious ritual should at least be not strange 51 Therefore , Goodrich and Hackett decided that the Hanukkah celebration should be performed in English , so that the American audience could understand the words used during the ritual . 

Rank 4, 254 words, from thesis_vu_2015/kcw/en/MANTOAN_thesis_final_trim.txt.naf.nohyphen:
The event took place in Moscow in the summer of 1959 in the frame of a series of promotional events the two governments organized in the adversary country , and it was meant to promote the reciprocal understanding of each other s cultures .15 As largely discussed by Greg Castillo , the debate underlined the exploitation of such official events to trumpet the magnificence and the successes of the two powers constantly looking for a chance to dictate their law on the other ; 16 in this event America aimed to display its rapid advances with regard to domestic technology and tried to shift the terms of the debate from military hardware to modern house ware , a domain of uncontested American pre_eminence .17 At the same time , they endeavoured to make the Soviet people dissatisfied with what they were receiving from their nation , and make them realize that the slight improvements projected in their standard of living were only a drop in the bucket compared to what they could and should have .18 It was clear that the Kitchen Debate was addressed to showcase commodities that the Eastern Bloc economies could not yet emulate , both for their design underdevelopment and for the constraint to stick to the heavy industries promoted by Stalin_era socialism ; 19 this resulted as an expedient to put Soviet socialism against American capitalism , assessing the two world orders in terms of their ability to deliver the goods to citizens .20 Moreover , while the debate s mobilisation of domestic material culture garnered far less media attention than 13 Castillo 2010 , chapter 4 and Betts 2010 , pp. 126_130 . 

Rank 5, 250 words, from thesis_vu_2015/kcw/en/VANDERVEER_MAdesigncultures_Thesis_trim.txt.naf.nohyphen:
John A. Walker argues that a canon is established once a number of histories exist which celebrate more or less the same set of great or pioneer designers and their classic or cult objects .3 Walker continues to address the critique these historical canons have received , in that they are unnatural phenomena since they are historically constructed and rely on the simplistic and linear notion that the baton of genius or avant garde innovation is being transferred from one grand designer to the other in an endless chain of achievement .4 The canonical stage marks the design as fixed by means of repetitive accordance ; when the authoritative interpretation of professionals finally reaches a wider audience through textbooks and popular articles , the canon is disseminated and leaves three options : the work may become a cultural monument beyond the reach of criticism , or it may suffer a decline in reputation and be forgotten , or it may be subject to reinterpretation and re-evaluation by a younger generation of critics examining it from new perspectives .5 According to Stuurman and Grever , a canon can be defined as a historical grand narrative , consisting of selected figures , events , story lines , ideas and values , colligated by definite plots , perspectives and explanations in which significance is frequently privileged over triviality and causes an emphasis on large events and grand personae rather than on gradually changing patterns , trends and forces .6 After the discussion of the canon , the development of Dutch contemporary jewellery history after the emergence of a canon will be discussed . 

Rank 6, 241 words, from thesis_vu_2015/kcw/en/MANTOAN_thesis_final_trim.txt.naf.nohyphen:
Inflation as a capitalist vice was declared conquered all over propaganda statements .35 As Mark Landsman and Donna Harsch comprehensively described in their studies , even if the GDR promised every kind of wealth , it could never keep up with its promises , nor it was ever able to solidly satisfy its people even with basic goods , food and supplies .36 Also in terms of commodities and consumer goods the GDR government remained always unsatisfactory , as stated by Anne Kaminski who also concisely investigated the correlation between advertisement , shortages and waiting lists .37 As Raymond Stokes analysed in Plastics and the New Society : the German Democratic Republic in the 1950 s and 1960 s , starting from the late 1950 s , the government engaged in the Chemisierung programme , a plan of state chemicalisation that aimed to produce and promote plastic as an alternative to sheet metal shortage and as a step toward modernization , East fashion .38 However , according also to Eli Rubin , bad quality of plastic influenced the consumers who had to acknowledge that products were worse than those produced in the West , were the state opened to new technologies and materials .39 East German consumers were perennially dissatisfied , always searching for something special with an unsatisfied desire for something else .40 In Continuities and discontinuities of consumer mentality in West Germany in the 1950 s Michael Wildt offers a pretty extensive account on how different the situation in terms of consumption was in the West if compared to the East at the 34 Ibid . 

Rank 7, 238 words, from thesis_vu_2015/kcw/en/A.Caccese_MA-Thesis-final_trim.txt.naf.nohyphen:
41 But with the advent of mechanized transport and the increase in size , towns became more and more anonymous , architecture lost its place as the main reference points of the city , and wayfinding systems became indispensable .42 For the authors , architecture needs to regain its voice and its ability to contextualize the city through its recognition value , and its main focus should be on expressing identity and authenticity .43 The book also explains the components of a wayfinding system , the history of pictograms , and introduces the discussion about the influence of digital wayfinding in our everyday life and how it has altered our sense of direction .44 GPS-supported telephones replaced print maps and changed navigation habits by messing with a person s ability to identify the spatial context and the path necessary to go from one place to another ; all that is left is a journey through a tunnel that actually increases the sense of disorientation .45 But even though there is no way to prevent the tendency towards virtual navigation , there is still the need to include guidance systems and signage in the urban landscape and buildings , especially to provide the public with a general overview .46 And in order to continue relevant , the conventional guidance system needs to be well designed which means to design a system that is , above all , synoptic .47 Finally , fifty wayfinding projects from different areas are presented , with examples of museums , airports , schools , and medical facilities , among others . 

Rank 8, 234 words, from thesis_vu_2015/kcw/en/MANTOAN_thesis_final_trim.txt.naf.nohyphen:
56 order to keep the tradition alive .167 This choice did not only help them to re_establish their Germaness and re_enact their own culture as Western Germans , but also acted as a remembrance engine with regard to other part of the country they had to part from starting from 1961.168 West German women , perfectly mindful of the existence of their East German halves invested their time in the kitchen not only to replicate dishes coming from their direct experience , but also trying to reproduce those belonging to their Eastern part , in a sort of remembrance for those traditions they considered lost , erased by the Soviet power .169 Cooking knowledge became a means of reviving German past positively and of recasting the nation through the mix and match of tradition and new trends , which allowed the negotiation of a new collective identity springing from the private and feminine sphere .170 In West Germany food could be national , regional or international and became a fundamental part of the post war redefinition of the nation , mingling new tendencies to old practices while ensuring that traditions of German cuisine remained intact and continue to develop .171 Food developed its own sense of commemoration on which women could build upon , seizing their share of culture making .172 Kitchen appliances became symbols of the irrevocable bound between women and their domestic role , representing a maternal figure not only for their families , but also symbolically for the nation . 

Rank 9, 224 words, from thesis_vu_2015/kcw/en/MANTOAN_thesis_final_trim.txt.naf.nohyphen:
20 Ibid. , p. x. 7 nuclear weapons , tests , diplomatic summits , and the Space Race , it somehow encouraged the Soviet bloc to measure its progress through direct comparisons with Western per capita private consumption , the Achilles heel of economies based on state_owned heavy industries .21 Furthermore , Castillo underlined how rather than constituting unilateral assertions of Cold war superiority , this exhibition manifested the influence that each superpower wielded over the self_image projected by its rival .22 The episode of the Kitchen Debate revealed functional to shake not only basics themes pivotal for the mere political sphere , but it also borne ideological conveyances : citizen enfranchisement , housework and gender equity , and the economics of mass consumption and planned obsolescence , themes that reverberated also in Germany .23 The US government clear promotion of the notion of better life which described both a modernist aesthetic and a prescription for global production and consumption , was not only a crass way to underline American supremacy but , for their own admission , constituted an exercise in cultural americanisation .24 Interesting the effect this event had during the following years on the East bloc has been analyzed thoroughly in literature , especially from the German stance Although journalists and historians credited the Kitchen Debate with turning the American post_war home and its contents into icons of anticommunism , the 1959 Moscow exhibition was the campaign s parting volley rather than it s opening shot . 

Rank 11, 219 words, from thesis_vu_2015/kcw/en/VANDERVEER_MAdesigncultures_Thesis_trim.txt.naf.nohyphen:
In 2006 , Ted Noten declared that contemporary jewellery is dead , an illusion , autistic , and superfluous .40 According to Noten , contemporary jewellery is dead because in its struggle for emancipation it eventually got stuck hanging on the walls of galleries , museums and such , [ p ] rotected by the stylized gravediggers of the art world , on display in its transparent coffin ; contemporary jewellery is an illusion because its myth of uniqueness is constantly advocated and the dogmatic faith in the incessant urge of contemporary jewellery design to be innovative avowed ; contemporary jewellery is autistic since it makes use of cryptic language , it refuses to engage with the banalities of daily reality , and it has become isolated by removing itself from any form of critical context because of its incomprehensive language ; contemporary jewellery is superfluous because it eliminated the wearer the only contribution contemporary jewellery could offer exclusively to the field of the visual arts and therefore it has to settle for its position in the fringes of the fringes which is thoroughly uninteresting since it is validated only by those few square inches necessary for its own conception .41 Noten suggests that for contemporary jewellery to be viable its maker needs to set aside the inflicted dogmas and return to craft in order to place centuries of conformism and defiance at his or her disposal . 

Rank 11, 219 words, from thesis_vu_2015/kcw/en/Scriptie_Te_Velde_trim.txt.naf.nohyphen:
As 27 former director of Premsela , Dingeman Kuilman explains , after 1993 the term Dutch Design became linked to a specific generation of designers .28 According to him , the term was born abroad and was created by media .29 Although no proper research has endeavoured to confirm the accuracy of this claim , the emergence of Dutch Design as a term was closely intertwined with the emergence of a specific group of designers .30 While a much larger group of anonymous colleagues designed the greater part of ( objects in ) the Netherlands , design historian Mienke Simon Thomas agrees that it was in fact a specific group of designers who fixed the image of Dutch design .31 According to design historian Damon Taylor , it was through the efforts of art historian Renny Ramakers and designer Gijs Bakker who established the Droog Design label .32 Following their debut at the Salone del Mobile ( the international furniture fair in Milan ) in 1993 , Droog Design became immensely successful internationally .33 The designs made under the label of Droog were mainly comprised of products made in limited serial editions34 , which were sold to the world through an appeal to a discourse of Dutchness .35 The prominence of Droog Design as emphatically Dutch was essential for canonising design from the Netherlands as Dutch Design .36 II .2 Droog , the Spirit of the Dutchman What conceptions of Dutchness did Droog establish ? 
```

Notice the tie here. Also the length of these sentences is not totally accurate as the parser did not parse the sentences right...

#### Frequency of Each Token or Type
The function ```dict_freq``` prints and return a counter dictionary. For example, if we want to know the frquency of each token and type in the Dutch thesis from the program Classics and Ancient Civilizations, we can use the following functions:
```python
query.dict_freq("token", program=["ohs"], language=["nl"])
query.dict_freq("type", program=["ohs"], language=["nl"])
```

These functions return two counter dictionaries.

#### The Type Token Ratio
Use the function ```type_token_ratio``` to get the type token ratio of desired these. For instance,
```python
query.type_token_ratio(program=["arch"], language=["en"])
```

Output:
```python
0.07088182265202427
```

#### The Frequency of Each Entity
The function ```dict_entity_freq``` returns a counter dictionary that maps each entity to its frequency, based on selected theses. For example,
```python
query.dict_entity_freq(program=["ges"], language=["en"])
```

#### The Most Frequent Persons or Locations
The function ```most_common_entity``` can print the first ```n``` most frequent persons or locations, based on selected theses. For example:
```python
query.most_common_entity("person", 10, program=["tlw", "rtlw"], language=["en"])
```

The output is:
```python
Rank	Entity	Frequency
1	Wolfe Tone	16
2	engels	15
3	Dostoevsky	13
4	Michael Ondaatje	11
5	Polycarp	9
6	Patrick Pearse	7
7	Benedict Anderson	5
8	Roger Casement	5
9	Oscar Wilde	4
10	Mikhail Bakhtin	3
```
And the code:
```python
query.most_common_entity("place", 5, program=["tlw", "rtlw"], language=["en"])
```

gives:
```python
Rank	Entity	Frequency
1	Ireland	94
2	Van	43
3	Canada	40
4	ik	36
5	canadian	34
```
