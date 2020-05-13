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
# TODO:  Add code here to import your sampler

# TODO:  Add code here to import your Traveling Salesman QUBO generator


## ------- provided distance matrix -------
distance_matrix = [
        [0, 2230, 1631, 1566, 1346, 1352, 1204],
        [2230, 0, 845, 707, 1001, 947, 1484],
        [1631, 845, 0, 627, 773, 424, 644],
        [1566, 707, 627, 0, 302, 341, 1027],
        [1346, 1001, 773, 302, 0, 368, 916],
        [1352, 947, 424, 341, 368, 0, 702],
        [1204, 1484, 644, 1027, 916, 702, 0],
    ]


def get_token():
    '''Return your personal access token'''

    # TODO: Enter your token here

    return token


# TODO:  Add code here to define your QUBO dictionary
def get_qubo(G):
    """Returns a dictionary representing a QUBO"""

    # TODO:  Add QUBO construction here

    return Q


# TODO:  Add code here to define your sampler
def get_sampler(token):
    """Returns a sampler"""

    # TODO: Enter your sampler here
    sampler = SomeSampler(endpoint='https://cloud.dwavesys.com/sapi/',
                          token=token)

    return sampler


## ------- Main program -------
if __name__ == "__main__":

    G = nx.Graph()
    j = 0
    for row in distance_matrix:
        for k, item in enumerate(row):
            if j < k:
                G.add_edge(j, k, weight=item)
        j += 1

    Q = get_qubo(G)
    token = get_token()
    sampler = get_sampler(token)
    bqm = dimod.BinaryQuadraticModel.from_qubo(Q)
    response = sampler.sample(bqm)

    start = None
    sample = response.first.sample
    n = len(distance_matrix)
    route = [None] * n

    for (city, time), val in sample.items():
        if val:
            route[time] = city

    if start is not None and route[0] != start:
        # rotate to put the start in front
        idx = route.index(start)
        route = route[-idx:] + route[:-idx]

    if None not in route:
        cost = 0
        for i, j in zip(route, route[1:] + route[:1]):
            cost += distance_matrix[i][j]
        print(route)
        print(cost)
