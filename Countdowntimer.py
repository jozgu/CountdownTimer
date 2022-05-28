#Countdowntimer, Running File 
#Credit Emil Gungaard/BeHeard - 28. May 2022
#Inspiration from https://stackoverflow.com/questions/53485957/python-gui-countdown-timer-dont-use-classes


import functions

#Length of timer (max 59.59 min/sec)
min = 0
sec = 3

#Layout
background_color = "#37ff00" 
text_color = 'white'
text_font = 'Calibri 400' #'font size' 
pad_vertical = 250 #250 is standard
pad_horison = None

functions.main(min, sec, background_color, text_color, text_font,pad_vertical,pad_horison)