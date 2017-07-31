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

## progress and future plan

- [x] scheduling with 0 clashes
- [ ] considering lab and class courses
- [ ] Fixed class constraint
- [ ] considering teacher and class preference 
- [ ] AI that considers many other constraints with simple representation.

## Algorithm

The script uses a genetic algorithm by which it creates several candidates and based on their fitness to the current problem, it chooses the evolving parents and continue that process until a certain fitness is reached.

## Licence

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

