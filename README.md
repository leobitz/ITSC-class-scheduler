# ITSC-class-scheduler
Creates schedule for college classes given student sections, class rooms and teachers list

## Usage

$ ./ga.py -i 500 -p 40 -c 0.8 -m 0.1

- -h -> Prints help
- -i -> specifies number of iterations, default is 100
- -p -> specifies size of population, default is 20
- -m -> mutation rate,  from 0 to 1, range, default is 0.1
- -c -> child ratio new population, from 1 to 0 range, default is 0.9
- -g -> mating pool random parent candidates, default is 4

The script uses the classes.csv file from last semester course offer as an exexample. go to the result folder and check out the schedule output of html files. schedule for rooms, for the teacher and for the students. 

## progress and future plan

- [x] scheduling with 0 clashes
- [ ] considering lab and class courses
- [ ] Fixed class constraint
- [ ] considering teacher and class preference 
- [ ] AI that considers many other constraints with simple representation.

## Algorithm

The script uses a genetic algorithm by which it creates several candidates and based on their fitness to the current problem, it chooses the evolving parents and continue that process until a certain fitness is reached.

Written in python, needs numpy

## Licence
Licensed under the MIT License

