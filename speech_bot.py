import pyttsx3
engine = pyttsx3.init()
engine.say('Hello everyone!!! Welcome to KCG College Of Technology. Let me introduce myself, My name is Sparky the Speech bot. Basically I am not an ai machine. I have been developed by using pyttsx3 python module')
engine.say('You guys came to explore Engenius and I am sure you guys will enjoy the event. Okay, Now my developer will explain you about her simple chat bot')
engine.say('Bye kuddos!!! See you next time. Until then enjoy with my new friend chat bot')
engine.setProperty('rate',180)
engine.setProperty('volume', 0.9)
engine.runAndWait()