

#include <iostream>
#include "ToyFactory.cpp"

using namespace std;


int main()
{
	int type;
	while (true)
	{
		cout << "Enter type or zero for exit" << endl;
		cin >> type;
		if (!type)
			break;
		Toy* v = ToyFactory::createToy(type);
		if (v)
		{
			v->showProduct();
			delete v;
		}
	}
	cout << "Exit..." << endl;
	return(0);
}

