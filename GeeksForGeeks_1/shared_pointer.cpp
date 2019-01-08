#include <iostream>
#include "shared_ptr.h"

using namespace std;

class Base
{
private:
	int data;
public:
	Base() : data(0) { std::cout << "  Base::Base()\n"; }
	virtual ~Base() { std::cout << "  Base::~Base()\n"; }

	void set_data(int data) 
	{
		this->data = data;
	}
	int get_data() const 
	{
		return this->data;
	}
};

class Derived : public Base
{
public:
	Derived() { std::cout << "  Derived::Derived()\n"; }
	~Derived() { std::cout << "  Derived::~Derived()\n"; }
};

shared_ptr<Base> function()
{
	shared_ptr<Base> ptr = new Derived();
	return ptr;
}

int main(int argc, char **argv)
{
	// Default constructor
	shared_ptr<Base> ptr1;

	{
		// Parameterized constructor
		shared_ptr<Base> ptr2 = function();

		// operator function call
		ptr2->set_data(100);

		// copy constructor call
		shared_ptr<Base> ptr3 = ptr2;

		// assignment operator call
		ptr1 = ptr3;
	}
	// operator function call
	cout << "  data set to: " << (*ptr1).get_data() << std::endl;

	int kkk;
	cin >> kkk;
	return kkk;
}