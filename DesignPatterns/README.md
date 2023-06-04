# Gang of Four Design Patterns in Java for Bond E-Trading

This repository provides detailed examples of the 23 Design Patterns described in the seminal book, **"Design Patterns: Elements of Reusable Object-Oriented Software"** by *Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides* (Addison-Wesley Professional, 1994).

Our examples will be set in the context of a bond e-trading system, showcasing real-world applications of these patterns using Java.

## Table of Contents
1. [Creational Patterns](#creational-patterns)
2. [Structural Patterns](#structural-patterns)
3. [Behavioral Patterns](#behavioral-patterns)
4. [How to Run the Code](#how-to-run-the-code)

## Creational Patterns

Creational patterns concern object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design.

### [Singleton](./Singleton)
Singleton pattern restricts the instantiation of a class to a single instance, useful for controlling actions. An example in bond e-trading would be a `TradingManager` class ensuring only one instance throughout the application.

### [Factory Method](./FactoryMethod)
Factory Method defines an interface for creating an object, but allows subclasses to decide which class to instantiate. This can be used for creating different types of Bonds (`CorporateBond`, `GovernmentBond`) based on provided information.

_More creational patterns to come..._

## Structural Patterns

Structural patterns concern class and object composition. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionalities.
These patterns are concerned with how classes and objects can be composed, to form larger structures.

_More structural patterns to come..._

## Behavioral Patterns

Behavioral patterns are concerned with communication between objects, how objects operate and interact. Rather than focusing on individual object behavior, behavioral patterns focus on the communication among objects.

_More behavioral patterns to come..._

## How to Run the Code

Each folder contains a separate Java project. You can clone the repository and import the project into your preferred Java IDE (like IntelliJ IDEA or Eclipse). 

This README will be updated as more patterns and examples are added to the repository.
