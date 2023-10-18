# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## ------- import packages -------
import networkx as nx
import dimod
# TODO:  Import your sampler

# TODO:  Import your Traveling Salesperson QUBO generator


def get_qubo(G, lagrange, n):
    """Returns a dictionary representing a QUBO"""

    # TODO:  Add QUBO construction here

    offset = 2 * n * lagrange

    return Q, offset


def get_sampler():
    """Returns a sampler"""

    # TODO: Enter your sampler here


    return sampler


## ------- Main program -------
if __name__ == "__main__":

    lagrange = 4000
    n = 7
    G = nx.Graph()
    G.add_weighted_edges_from([
        (0, 1, 2230),
        (0, 2, 1631),
        (0, 3, 1566),
        (0, 4, 1346),
        (0, 5, 1352),
        (0, 6, 1204),
        (1, 2, 845),
        (1, 3, 707),
        (1, 4, 1001),
        (1, 5, 947),
        (1, 6, 1484),
        (2, 3, 627),
        (2, 4, 773),
        (2, 5, 424),
        (2, 6, 644),
	(3, 4, 302),
	(3, 5, 341),
	(3, 6, 1027),
	(4, 5, 368),
	(4, 6, 916),
	(5, 6, 702)
    ])
    Q, offset = get_qubo(G, lagrange, n)
    sampler = get_sampler()
    bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=offset)
    response = sampler.sample(bqm, label="Training - TSP")

    start = None
    sample = response.first.sample
    cost = response.first.energy
    route = [None] * n

    for (city, time), val in sample.items():
        if val:
            route[time] = city

    if start is not None and route[0] != start:
        # rotate to put the start in front
        idx = route.index(start)
        route = route[-idx:] + route[:-idx]

    if None not in route:
        print(route)
        print(cost)
