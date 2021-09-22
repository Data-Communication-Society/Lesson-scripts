# 01_01

# an example of routine
import datetime
routine_complete = False
counter = 0
start_time = datetime.datetime.now()
while not routine_complete:
    counter += 1
    if counter % 100000 == 0 and counter != 2400000:
        print('{}/2400000 routine completed'.format(counter))
    if counter == 2400000:
        routine_complete = True
        print('routine completed')
        end_time = datetime.datetime.now()
        print('execution time: {}'.format(end_time - start_time))  # should be below 1 second