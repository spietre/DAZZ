print("hello world")


year = [2010, 2020]
pop = [3.12, 3.50]

# Import matplotlib.pyplot as plt
# import matplotlib.pyplot as pt


# Make a line plot: year on the x-axis, pop on the y-axis
#pt.plot(year,pop)


# Display the plot with plt.show()
# pt.show()



# import matplotlib.pyplot as plt

# plt.scatter(year, pop)
# plt.show()


import matplotlib.pyplot as plt

help(plt.hist)

values = [0,.6,1.4,1.6,2.2,2.5,2.6,3.2]

plt.hist(values, 3)

plt.show()


















0 IF Age=elder and Tumor=no THEN Cancer=low      support: 2, confidence: 100.0%
1 IF Tumor=no and History=high THEN Cancer=low   support: 2, confidence: 100.0%
2 IF History=low and Cancer=low THEN Heredity=no         support: 3, confidence: 100.0%        
3 IF Heredity=no and Age=younger THEN Cancer=low         support: 4, confidence: 100.0%        
4 IF Tumor=no and Heredity=no THEN Cancer=low    support: 2, confidence: 100.0%
5 IF Tumor=no and Heredity=yes THEN Cancer=low   support: 2, confidence: 100.0%
6 IF Tumor=confirmed and History=high THEN Cancer=high   support: 2, confidence: 100.0%        
7 IF History=high and Cancer=high THEN Tumor=confirmed   support: 2, confidence: 100.0%        
8 IF Heredity=yes and Tumor=confirmed THEN Cancer=high   support: 3, confidence: 100.0%        
9 IF Age=elder and Tumor=non confirmed THEN Cancer=high  support: 2, confidence: 100.0%        
10 IF Tumor=non confirmed and Age=younger THEN Cancer=low        support: 3, confidence: 100.0%
11 IF Heredity=no and History=medium THEN Cancer=low     support: 2, confidence: 100.0%        
12 IF Tumor=no and History=high THEN Age=younger         support: 2, confidence: 100.0%        
13 IF Cancer=low and History=high THEN Age=younger       support: 2, confidence: 100.0%        
14 IF Tumor=confirmed and Heredity=yes THEN Cancer=high  support: 3, confidence: 100.0%        
15 IF History=low and Tumor=non confirmed THEN Heredity=no       support: 2, confidence: 100.0%
16 IF Age=younger and Heredity=no THEN Cancer=low        support: 4, confidence: 100.0%
17 IF Cancer=high and Tumor=confirmed THEN Heredity=yes  support: 3, confidence: 100.0%
18 IF Cancer=high and History=high THEN Heredity=yes     support: 2, confidence: 100.0%
19 IF Age=younger and Cancer=high THEN Heredity=yes      support: 2, confidence: 100.0%
20 IF Cancer=high and Age=younger THEN Tumor=confirmed   support: 2, confidence: 100.0%
21 IF Cancer=low and Tumor=confirmed THEN Heredity=no    support: 2, confidence: 100.0%
22 IF History=low and Age=younger THEN Cancer=low        support: 2, confidence: 100.0%
23 IF Age=younger and Tumor=no THEN History=high         support: 2, confidence: 100.0%
24 IF Cancer=low and History=low THEN Heredity=no        support: 3, confidence: 100.0%
25 IF Cancer=high and Age=younger THEN Heredity=yes      support: 2, confidence: 100.0%
26 IF Age=younger and History=low THEN Cancer=low        support: 2, confidence: 100.0%
27 IF Tumor=confirmed and History=high THEN Heredity=yes         support: 2, confidence: 100.0%
28 IF History=medium and Cancer=high THEN Heredity=yes   support: 2, confidence: 100.0%
29 IF History=medium and Heredity=no THEN Cancer=low     support: 2, confidence: 100.0%
30 IF Tumor=confirmed and Heredity=no THEN Cancer=low    support: 2, confidence: 100.0%
31 IF Heredity=no and Tumor=no THEN Cancer=low   support: 2, confidence: 100.0%
32 IF Cancer=high and History=high THEN Tumor=confirmed  support: 2, confidence: 100.0%
33 IF Tumor=non confirmed and Age=elder THEN Cancer=high         support: 2, confidence: 100.0%
34 IF History=high and Tumor=no THEN Cancer=low  support: 2, confidence: 100.0%
35 IF History=high and Tumor=confirmed THEN Heredity=yes         support: 2, confidence: 100.0%
36 IF Age=younger and Tumor=no THEN Cancer=low   support: 2, confidence: 100.0%
37 IF Tumor=no and Age=younger THEN History=high         support: 2, confidence: 100.0%
38 IF History=high and Tumor=no THEN Age=younger         support: 2, confidence: 100.0%
39 IF Cancer=high and Tumor=non confirmed THEN Age=elder         support: 2, confidence: 100.0%
40 IF Tumor=non confirmed and Cancer=low THEN Age=younger        support: 3, confidence: 100.0%
41 IF History=high and Tumor=confirmed THEN Cancer=high  support: 2, confidence: 100.0%
42 IF Age=younger and Tumor=non confirmed THEN Cancer=low        support: 3, confidence: 100.0%
43 IF Cancer=low and History=high THEN Tumor=no  support: 2, confidence: 100.0%
44 IF Tumor=non confirmed and Heredity=yes THEN History=medium   support: 2, confidence: 100.0%
45 IF Heredity=yes and Tumor=non confirmed THEN History=medium   support: 2, confidence: 100.0%
46 IF Heredity=yes and Tumor=no THEN Cancer=low  support: 2, confidence: 100.0%
47 IF Tumor=non confirmed and History=low THEN Heredity=no       support: 2, confidence: 100.0%
48 IF Cancer=high and History=medium THEN Heredity=yes   support: 2, confidence: 100.0%
49 IF Tumor=non confirmed and Cancer=high THEN Age=elder         support: 2, confidence: 100.0%
50 IF Tumor=confirmed and Cancer=high THEN Heredity=yes  support: 3, confidence: 100.0%
51 IF Cancer=low and Tumor=non confirmed THEN Age=younger        support: 3, confidence: 100.0%
52 IF History=high and Cancer=high THEN Heredity=yes     support: 2, confidence: 100.0%
53 IF Age=younger and History=low THEN Heredity=no       support: 2, confidence: 100.0%
54 IF History=high and Cancer=low THEN Age=younger       support: 2, confidence: 100.0%
55 IF Tumor=no and Age=younger THEN Cancer=low   support: 2, confidence: 100.0%
56 IF Heredity=no and Tumor=confirmed THEN Cancer=low    support: 2, confidence: 100.0%
57 IF Age=elder and History=low THEN Heredity=no         support: 2, confidence: 100.0%
58 IF History=low and Age=younger THEN Heredity=no       support: 2, confidence: 100.0%
59 IF Age=younger and Cancer=high THEN Tumor=confirmed   support: 2, confidence: 100.0%
60 IF Tumor=confirmed and Cancer=low THEN Heredity=no    support: 2, confidence: 100.0%
61 IF History=high and Cancer=low THEN Tumor=no  support: 2, confidence: 100.0%
62 IF Tumor=no and Age=elder THEN Cancer=low     support: 2, confidence: 100.0%
63 IF History=low and Age=elder THEN Heredity=no         support: 2, confidence: 100.0%