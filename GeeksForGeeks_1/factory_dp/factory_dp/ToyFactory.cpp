// creational design pattern
// language neutral (provided it's OO)

// FDP creates objects for you rather than you initializing objects directly
// FDP known as "Virtual Constructor"

// call the factory function and tell the function what object you want

// FDP define an interface (i.e. abstract class) for creating an object
// but let the subclasses decide which class to initiate

// create objects at run time not at compile time, aka benefits of virtual constructor

// Toy <- Car, Bike, Plane <--creates-- ToyFactory <--calls-- main

// We create obejcts without exposing creational logic to the client
// You just tell the client: I want this object!

#include <iostream>
#include "Object.cpp"

using namespace std;

class ToyFactory
{
public:
	static Toy* createToy(int type)
	{
		Toy* toy = nullptr;
		
		switch (type)
		{
		case 1:
			toy = new Car;
			break;
		case 2:
			toy = new Bike;
			break;
		case 3:
			toy = new Plane;
			break;
		default:
			cout << "invalid toy type please re-enter type" << endl;
			return nullptr;
		}

		toy->prepareParts();
		// you can do some pre-processing here 
		toy->combineParts();
		toy->assempleParts();
		toy->applyLabel();

		return toy;
	}
};