[![Open in Leap IDE](	
	https://cdn-assets.cloud.dwavesys.com/shared/latest/badges/leapide.svg)](
	https://ide.dwavesys.io/#https://github.com/dwave-training/traveling-salesman)

# Traveling Salesman

This exercise contains two exercises which illustrate the use of 
the Hybrid Solver Service (HSS) and one alternative sampler.

## Exercise 1

The program ``hss_exercise.py`` is the first exercise.
It is a 7-city Traveling Salesman problem.
First, you need to call the Hybrid Solver Service, call the Traveling
Salesman QUBO generator from ``dwave_networkx``, and then enter your access 
token.
To run your program from the command-line, type ``python hss_exercise.py``. 
You have successfully
completed the exercise when you are able to see a result of 5422 miles (the
minimum distance solution for the 7-city Traveling Salesman problem.)

## Exercise 2 

The program ``compare_solver_exercise.py`` is the second exercise.
It is a 7-city Traveling Salesman problem.
First, you need to call an alternative sampler - you can choose 
``SimulatedAnnealingSampler``, or ``TabuSampler``. You also need to call the
Traveling Salesman QUBO generator from ``dwave_networkx``.
To run your program from the command-line, 
type ``python compare_solver_exercise.py``. You have 
successfully completed the exercise when you are able to see a result in
miles under 10000. (The alternate solvers do not necessarily find the
ground state)

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
