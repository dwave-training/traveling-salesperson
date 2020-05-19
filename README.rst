==================
Traveling Salesman
==================

This exercise contains two student exercises which illustrate the use of 
the Hybrid Solver Service (HSS) and one alternative sampler.

Exercise 1
----------

The program ``hss_exercise.py`` is an exercise for students.
It is a 7-city Traveling Salesman problem.
The students need to call the Hybrid Solver Service, call the Traveling
Salesman QUBO generator from ``dwave_networkx``, and enter their own access 
token.
To run your program, type ``python hss_exercise.py``. You have successfully
completed the exercise when you are able to see a result of 5422 miles (the
minimum distance solution for the 7-city Traveling Salesman problem.)

Exercise 2
----------

The program ``compare_solver_exercise.py`` is an exercise for students.
It is a 7-city Traveling Salesman problem.
The students need to call an alternative sampler - they can choose 
``SimulatedAnnealingSampler``, or ``TabuSampler``. They also need to call the
Traveling Salesman QUBO generator from ``dwave_networkx``.
To run your program, type ``python compare_solver_exercise.py``. You have 
successfully completed the exercise when you are able to see a result in
miles under 10000. (The alternate solvers do not necessarily find the
ground state)
