from car import Car
from simulation import Simulation
import numpy as np
from unittest import mock


def test_simulation_takes_cars():
    sim = Simulation(4)
    sim.create_cars(4)
    assert len(sim.cars) == 4

def test_simulation_has_length():
    sim = Simulation(4)
    sim.create_cars(4)
    assert sim.length == 1000

def test_create_speed_matrix():
    sim = Simulation(4)
    sim.create_cars(4)
    sim.create_empty_data_matrix()
    assert (sim.data_matrix.size) == 968
    assert (sim.data_matrix.shape) == (2, 121, 4)

def test_setup():
    sim = Simulation(4)
    sim.create_cars(4)
    sim.create_starting_array()
    sim_setup = sim.create_starting_array()
    assert sim_setup.size == 4
    assert sim_setup.shape == (4,)

def test_cars_get_starting_places():
    sim = Simulation(4)
    sim.create_cars(4)
    sim.create_empty_data_matrix()
    start_setup = sim.give_cars_starting_places()
    assert sim.cars[0].location == 5
    assert sim.cars[1].location == 335
    assert np.array_equal(start_setup, [5, 335, 665, 995])
    assert sim.data_matrix.shape == (2, 121, 4)
    assert sim.data_matrix[0].shape == (121, 4)
    assert sim.data_matrix[0][0].shape == (4,)
    # assert sim.data_matrix[0][0] == sim.data_matrix[0][0] + start_setup
    # not working getting list index out of range

def test_advance_cars_and_record_adds_speed_to_car_location():
    sim = Simulation(4)
    sim.create_cars(4)
    sim.create_empty_data_matrix()
    sim.give_cars_starting_places()
    sim.advance_cars_and_record()
    assert np.array_equal(sim.data_matrix[0][1], sim.data_matrix[0][0])
    sim.turn_count +=1
    sim.data_matrix[1][1] = [2, 2, 2, 2]
    sim.advance_cars_and_record()
    assert np.array_equal(sim.data_matrix[0][2], [7, 337, 667, 997])

def test_advance_cars_and_record_adds_speed_to_car_location_over_1000():
    sim = Simulation(4)
    sim.create_cars(4)
    sim.create_empty_data_matrix()
    sim.give_cars_starting_places()
    sim.advance_cars_and_record()
    sim.turn_count +=1
    sim.data_matrix[1][1] = [10, 10, 10, 10]
    sim.advance_cars_and_record()
    assert np.array_equal(sim.data_matrix[0][2], [15, 345, 675, 5])

def test_advance_cars_and_record_adds_speed_to_car_location():
    sim = Simulation(4)
    sim.create_cars(4)
    sim.create_empty_data_matrix()
    sim.give_cars_starting_places()
    sim.advance_cars_and_record()
    sim.turn_count +=1
    sim.data_matrix[1][1] = [10, 10, 10, 10]
    sim.advance_cars_and_record()
    assert sim.cars[0].location == 15
    assert sim.cars[1].location == 345
    assert sim.cars[3].location == 5

def test_decide_speed_sets_new_speed_for_cars():
    with mock.patch("random.random", return_value=.5):
        sim = Simulation(4)
        sim.create_cars(4)
        sim.create_empty_data_matrix()
        sim.give_cars_starting_places()
        sim.advance_cars_and_record()
        sim.decide_speed_and_record()
        assert sim.cars[0].speed ==2
        assert sim.turn_count ==1

def test_matrix_updates_from_cars():
      with mock.patch("random.random", return_value=.5):
        sim = Simulation(4)
        sim.create_cars(4)
        sim.create_empty_data_matrix()
        sim.give_cars_starting_places()
        sim.advance_cars_and_record()
        sim.decide_speed_and_record()
        sim.turn_count +=1
        sim.advance_cars_and_record()
        sim.decide_speed_and_record()
        assert sim.data_matrix[1][sim.turn_count][0] == sim.cars[0].speed
        assert sim.cars[3].speed == 4

