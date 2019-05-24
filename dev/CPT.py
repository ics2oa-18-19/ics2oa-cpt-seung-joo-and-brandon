import time
import random
import time

high_score = 0

scramble = ['L', 'L2', 'L*', 'R', 'R2', 'R*',  'D', 'D2', 'D*', 'B', 'B*', 'B2', 'F', 'F2', 'F*', 'U', 'U2', 'U*']

while len(scramble) < 21:
    random.shuffle(scramble)

    print(scramble)

    start = input("Press enter to start the time")

    print("SOLVE")

    begin = time.time()

    endtimer = input("Press enter to stop the timer")

    end = time.time()

    elapsed = end - begin

    elapsed = float(elapsed)

    elapsed = round(elapsed, 2)

    if high_score == 0:
        high_score = elapsed
        print('The high score is', high_score, "Seconds")
    
    if elapsed < high_score:
        difference = high_score - elapsed
        print('You beat your high score by', difference, "Seconds")

        difference = (round, 2)

    print("The time you took is", elapsed, "Seconds")
    


