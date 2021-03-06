import time
from pygame import mixer

def music_control(file,stop):
    """This function gives music control"""
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    a = input()
    if a == stop:
        mixer.music.stop()

if __name__ == '__main__':
    init_water = time.time()
    init_eyes = time.time()
    init_physical_exercise = time.time()
    water_seconds = 2400 # 40 minutes
    eyes_seconds = 1200 # 20 minutes
    exercise_seconds = 2700 # 45 minutes

    print("*** Welcome to Healthy Programmer ***\n\nAt every\n\t 40 minutes, drinking water time \n\t 30 minutes, eye exercise time \n\t 45 minutes, Physical activity time\n\nTo stay healthy while using laptop for hours is must! Open this app and let me take care of you! Have a good day. \n ")

    while True:
        if time.time() - init_water > water_seconds:
            print("Water Drinking time! Type Drank to stop the alarm")
            music_control("water.mp3","Drank")
            init_water= time.time()
        if time.time() - init_eyes > eyes_seconds:
            print("Eye Exercise time! Type EyeDone to stop the alarm")
            # music_control("eyeexercise.mp3","EyeDone")
            init_eyes=time.time()
        if time.time() - init_physical_exercise > exercise_seconds:
            print("Physical Exercise time! Type ExDone to stop the alarm")
            music_control("physcialexercise.mp3","ExDone")
            init_physical_exercise=time.time()

    print("Your duty hours is over! Thank you, Good Day")
