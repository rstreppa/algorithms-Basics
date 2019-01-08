#pragma once
#include <string>

using namespace std;

class Singleton 
{
private: 
	string m_msg;
	double m_balance;
protected:
	Singleton(string msg, double balance = 100.0) noexcept: m_msg(msg), m_balance(balance) {}
	virtual ~Singleton() = default;
	Singleton(const Singleton&) = delete;
	Singleton& operator=(const Singleton&) = delete;
public:
	static Singleton& getInstance(double balance = 100.0) noexcept(std::is_nothrow_constructible<Singleton>::value)
	{
		// Guaranteed to be destroyed.
		// Instantiated on first use.
		// Thread safe in C++11
		// Usage: Node& node = Node::getInstance(<optional balance>);
		static Singleton instance("", balance);
		return instance;
	}
};
