from pygame import mixer
from time import time, ctime

no_of_glass = 0

print("You have to drink 5 liters of water every day to stay hydrated!")


def audio(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("log.txt", "a") as f:
        f.write(f"{msg} [{ctime()}]\n")
        f.close()


if __name__ == '__main__':
    water = time()
    eyes = time()
    exercise = time()
    water_time = 30 * 60
    exercise_time = 35 * 60
    eye_time = 45 * 60
    while True:
        if time() - water > water_time and no_of_glass < 35:
            print("Water Drinking time. Enter 'drank' to log the date and time.")
            print(no_of_glass + 1, "glasses of water drank!")
            audio('water.mp3', 'drank')
            water = time()
            log_now("Drank Water at--> ")
            no_of_glass = no_of_glass + 1
            continue
        elif no_of_glass >= 35:
            print("You had enough water to stay hydrated!")
            break
        if time() - eyes > eye_time:
            print("Give rest to your eyes, type 'ok' to log the date and time.")
            audio('eye.mp3', 'ok')
            eye = time()
            log_now("Eyes relaxed at--> ")

        if time() - exercise > exercise_time:
            print("Time to do some physical activity type 'done' to log the date and time.")
            audio('exercise.mp3', 'done')
            exercise = time()
            log_now("Exercise done at--> ")
