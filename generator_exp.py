import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.process_time()
people = people_generator(1000000)
print(people)
t2 = time.process_time()

print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

print ('Took ' + str(t2-t1) + ' Seconds')