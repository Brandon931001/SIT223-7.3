from garage import Vehicle, VehicleType, drive_vehicle, refuel_vehicle

def test_vehicle_creation():
    v = Vehicle("TestCar", VehicleType.CAR, 100, 4, 80, 5000, 2000)
    assert v.name == "TestCar"
    assert v.type == VehicleType.CAR
    assert v.speed == 100
    assert v.capacity == 4
    assert v.fuel_level == 80

def test_drive_vehicle():
    v = Vehicle("DriveTest", VehicleType.CAR, 100, 4, 100, 1000, 500)
    drive_vehicle(v, 50)
    assert v.fuel_level == 95
    assert v.mileage == 1050
    assert v.maintenance_due == 450

def test_refuel_vehicle():
    v = Vehicle("RefuelTest", VehicleType.CAR, 100, 4, 50, 0, 10000)
    refuel_vehicle(v, 30)
    assert v.fuel_level == 80
