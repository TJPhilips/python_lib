1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
#Import relevant libraries
from gpiozero import *
from time import sleep
import random
 
#Set pin numbers
led_1 = LED(12)
led_2 = LED(22)
led_3 = LED(4)
rgb = RGBLED(red=14, green=17, blue=27) #was red, green blue RGB
 
#define buttons and links
button_1 = Button(5)
button_2 = Button(24)
button_3 = Button(2)
 
#Input player names
player_1 = raw_input("Enter the name of Player 1: ")
player_2 = raw_input("Enter the name of Player 2: ")
player_3 = raw_input("Enter the name of Player 3: ")
 
#Initialise score variables
player_1_score = 0
player_2_score = 0
player_3_score = 0
 
#Initialise round number variable
round_num = 0
 
#Start the game
while True:
 
    trick = False   #Set trick mode
    round_num = round_num +1 #Increment round number by one for each iteration
 
    wait = 0
 
    time = random.uniform(0, 10)        #Randomly generate time delay between 0 and 10 seconds
    color_2 = random.uniform(0, 1)      #Randomly generate green colour value (on or off)
    color_3 = random.uniform(0, 1)      #Randomly generate blue colour value (on or off)
 
    fix = random.randint(0,3)           #Randomly generate number for trick question between 0 and 3 inclusive
 
    if color_2 == 0 and color_3 == 0:   #If all colours are off by chance
        color_2 = 1                     #Set green pixel to on
 
    print " "                               #Print blank line for better formatting
    print "Round", str(round_num) + ":"     #Print round number
    print "Get Ready!"
 
    sleep(time)     #Wait for random amount of time
 
    if fix == 3:                #Approx 25% of the time
        trick = True            #Set trick mode
        rgb.color = (1, 0, 0)   #Make RGB LED Red
    else:
        rgb.color = (0, color_2, color_3) #Turn on RGB LED to random colour
 
    while True:
        if button_1.is_pressed and trick == False:                      #If player 1 button is pressed
            print player_1, "wins!"                                     #Display winning message
            player_1_score = player_1_score + 1                         #Increment score by one
            rgb.color = (0,0,0)                                         #Turn LED off
            print player_1, ":", player_1_score                  #Display scores
            print player_2, ":", player_2_score
            print player_3, ":", player_3_score
            wait = 0                                                    #Reset wait value
            break
        elif button_1.is_pressed and trick == True:
            print player_1, "Oh dear! You hit a trick -1 point!"                                  #Display winning message
            player_1_score = player_1_score - 1                         #Increment score by one
            rgb.color = (0,0,0)                                         #Turn LED off
            print player_1, ":", player_1_score             #Display scores
            print player_2, ":", player_2_score
            print player_3, ":", player_3_score
            wait = 0                                                    #Reset wait value
            break
 
        if button_2.is_pressed and trick == False:
            print player_2, "wins!"
            player_2_score = player_2_score + 1
            rgb.color = (0,0,0)
            print player_1, ":", player_1_score                 #Display scores
            print player_2, ":", player_2_score
            print player_3, ":", player_3_score
            wait = 0                                                    #Reset wait value
            break
 
        elif button_2.is_pressed and trick == True:
            print player_2, "Oh dear! You hit a trick -1 point!"
            player_2_score = player_2_score - 1
            rgb.color = (0,0,0)
            print player_1, ":", player_1_score                   #Display scores
            print player_2, ":", player_2_score
            print player_3, ":", player_3_score
            wait = 0
            break
 
        if button_3.is_pressed and trick == True:
            print player_3, "Oh dear! You hit a trick -1 point!"
            player_3_score = player_3_score -1
            rgb.color = (0,0,0)
            print player_1, ":", player_1_score                   #Display scores
            print player_2, ":", player_2_score
            print player_3, ":", player_3_score
            wait = 0                                                    #Reset wait value
            break
 
        elif button_3.is_pressed and trick == False:
            print player_3, "wins!"
            player_3_score = player_3_score +1
            rgb.color = (0,0,0)
            print player_1, ":", player_1_score                 #Display scores
            print player_2, ":", player_2_score
            print player_3, ":", player_3_score
            wait = 0
            break
 
        if trick == True and wait == 10000:                            #If on trick question time out after approx 5 seconds
            print "Well Done"
            rgb.color = (0,0,0)
            print player_1, ":", player_1_score                  #Display scores
            print player_2, ":", player_2_score
            print player_3, ":", player_3_score
            wait = 0                                                    #Reset wait value
            break
 
        wait = wait + 1                                                 #Increment wait value by one
 
        led_draw_lights = [player_1_score, player_2_score, player_3_score]
        print led_draw_lights, "led draw light scores"
 
        if led_draw_lights = True
            print "Drawing, LEDs on"
            led_1.on()
            led_2.on()
            led_3.on()
 
 
#    if player_1_score > player_2_score & player_3_score:     #If player one is winning overall
#        led_1.on()                          #Turn on player one LED and turn player two and three LED off
#        led_2.off()
#        led_3.off()
#    elif player_3_score > player_1_score & player_2_score:
#        led_3.on()
#        led_2.off()
#        led_1.off()
#    elif player_2_score > player_1_score & player_3_score:
#        led_2.on()
#        led_1.off()
#        led_3.off()
#    if player_3_score > player_1_score: ADD LED SUPPORT LATER
#    else:                                   #If they are drawing
#        led_1.on()                          #Turn on all LEDs on
#        led_2.on()
#        led_3.on()
