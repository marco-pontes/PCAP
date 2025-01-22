from modules.oop.examples.vehicle.CombustionVehicle import CombustionVehicle
from modules.oop.examples.vehicle.ElectricVehicle import ElectricVehicle


class HybridVehicle(ElectricVehicle, CombustionVehicle):
    pass