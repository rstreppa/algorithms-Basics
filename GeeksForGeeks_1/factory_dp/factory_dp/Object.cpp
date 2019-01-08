#include <iostream>
#include <string>

using namespace std;

class Toy {
protected:
	string name;
	float price;
public:
	virtual void prepareParts()		= 0;
	virtual void combineParts()		= 0;
	virtual void assempleParts()	= 0;
	virtual void applyLabel()		= 0;
	virtual void showProduct()		= 0;
};


class Car : public Toy 
{
	void prepareParts()		{ cout << "Preparing Car Parts" << endl; }
	void combineParts()		{ cout << "Combining Car Parts" << endl; }
	void assempleParts()	{ cout << "Assembling Car Parts" << endl; }
	void applyLabel()		{ cout << "Applying Car Label" << endl; name = "Car"; price = 10; }
	void showProduct()		{ cout << "Name: " << name << endl << "Price: " << price << endl; }
};

class Bike : public Toy
{
	void prepareParts()		{ cout << "Preparing Bike Parts" << endl; }
	void combineParts()		{ cout << "Combining Bike Parts" << endl; }
	void assempleParts()	{ cout << "Assembling Bike Parts" << endl; }
	void applyLabel()		{ cout << "Applying Bike Label" << endl; name = "Bike"; price = 20; }
	void showProduct()		{ cout << "Name: " << name << endl << "Price: " << price << endl; }
};

class Plane : public Toy
{
	void prepareParts()		{ cout << "Preparing Plane Parts" << endl; }
	void combineParts()		{ cout << "Combining Plane Parts" << endl; }
	void assempleParts()	{ cout << "Assembling Plane Parts" << endl; }
	void applyLabel()		{ cout << "Applying Plane Label" << endl; name = "Plane"; price = 30; }
	void showProduct()		{ cout << "Name: " << name << endl << "Price: " << price << endl; }
};


