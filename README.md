# ITSC-class-scheduler
Creates schedule for college classes given student sections, class rooms and teachers list

## Usage

$ ./ga.py -i 500 -p 40 -c 0.8 -m 0.1

- -h -> Prints help
- -i -> specifies number of iterations, defualt is 100
- -p -> specifies size of population, defualt is 20
- -m -> mutation rate,  from 0 to 1, range, defualt is 0.1
- -c -> child ratio new population, from 1 to 0 range, defualt is 0.9
- -g -> mating pool random parent candidates, defualt is 4

## progress and future plan

- [x] scheduling with 0 clashes
- [ ] considering lab and class courses
- [ ] Fixed class constraint
- [ ] considering teacher and class preference 
- [ ] AI that considers many other constraints with simple representation.

## Algorithm

The script uses a genetic algorithm by which it creates several candidates and based on thier fitness to the current problem, it chooses the evolving parants and continue that process until a certain fitness is reached.
