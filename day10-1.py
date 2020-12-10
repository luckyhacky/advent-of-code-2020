import re

input = """80
87
10
122
57
142
134
59
113
139
101
41
138
112
46
96
43
125
36
54
133
17
42
98
7
114
78
67
77
28
149
58
20
105
31
19
18
27
40
71
117
66
21
72
146
90
97
94
123
1
119
30
84
61
91
118
2
29
104
73
13
76
24
148
68
111
131
83
49
8
132
9
64
79
124
95
88
135
3
51
39
6
60
108
14
35
147
89
34
65
50
145
128"""


data = sorted(list(map(int, input.split("\n"))))


j1 = 1 # for input adapter
j3 = 1 # for input adapter ( see 3 jolts higher than the highes rated adapter)
last = data[0]

print("input length = " + str(len(data)))

for a in data:
    if a - last == 1:
        j1 += 1
    elif a - last == 3:
        j3 += 1
    else:
        if last != data[0]:
            print("out of range", last, a)
    last = a
        


print("offset 1 = " + str(j1) + " - offset 3 = " + str(j3))
print("solution: " + str(j1 * j3))

