# Gang of Four Design Patterns in Java for Bond E-Trading

This repository provides detailed examples of the 23 Design Patterns described in the seminal book, **"Design Patterns: Elements of Reusable Object-Oriented Software"** by *Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides* (Addison-Wesley Professional, 1994).

Our examples are set in the context of a bond e-trading system, showcasing real-world applications of these patterns using Java.

## Table of Contents
1. [Creational Patterns](#creational-patterns)
2. [Structural Patterns](#structural-patterns)
3. [Behavioral Patterns](#behavioral-patterns)
4. [How to Run the Code](#how-to-run-the-code)

## Creational Patterns

Creational patterns concern object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design.

### [Singleton](./Singleton)
Singleton pattern restricts the instantiation of a class to a single instance, useful for controlling actions. An example in bond e-trading would be a `TradingManager` class ensuring only one instance throughout the application.

### [Prototype](./Prototype)
Prototype pattern provides a way to copy the original object without making the code dependent on their classes. Used in bond e-trading when a `Bond` object is created and we need to produce a duplicate bond with minor changes.

### [Builder](./Builder)
Builder pattern constructs complex objects step by step. It can create different types or representations of an object using the same construction code. In our bond e-trading system, it could be used to create a complex `BondTrade` object.

### [Factory Method](./FactoryMethod)
Factory Method defines an interface for creating an object, but allows subclasses to decide which class to instantiate. This can be used for creating different types of Bonds (`CorporateBond`, `GovernmentBond`) based on provided information.

### [Abstract Factory](./AbstractFactory)
Abstract Factory is a super-factory which creates other factories. In bond e-trading, an `AbstractBondFactory` might provide an interface for creating a family of related `Bond` objects.

_More creational patterns..._

## Structural Patterns

Structural patterns concern class and object composition. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionalities.

### [Adapter](./Adapter)
Adapter pattern allows objects with incompatible interfaces to collaborate. It can be used in bond e-trading to interface with legacy or external systems with different interfaces.

### [Bridge](./Bridge)
Bridge pattern splits a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation which can be developed independently of each other. In our context, `Bond` can be the abstraction, `BondType` can be the implementation hierarchy.

### [Composite](./Composite)
Composite pattern lets clients treat individual objects and compositions of objects uniformly. In bond e-trading, a `BondPortfolio` (composite) can contain multiple `Bond` objects (individual objects).

### [Decorator](./Decorator)
Decorator pattern lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors. In our context, we could add `TradeBooking`, `TradeClearing` behaviors to `BondTrade` object.

### [Facade](./Facade)
Facade pattern provides a simplified interface to a complex subsystem. In bond e-trading, a `TradeFacade` could simplify multiple complex objects and processes like `TradeClearing`, `TradeSettlement`.

### [Flyweight](./Flyweight)
Flyweight pattern saves memory by sharing parts of object state among multiple objects. In our context, multiple `Bond` objects can share common state like `BondType`.

### [Proxy](./Proxy)
Proxy pattern provides a surrogate or placeholder for another object. In bond e-trading, a `BondTradeProxy` could control access to the `BondTrade` object.

_More structural patterns..._

## Behavioral Patterns

Behavioral patterns are concerned with communication between objects, how objects operate and interact. Rather than focusing on individual object behavior, behavioral patterns focus on the communication among objects.

### [Chain of Responsibility](./ChainOfResponsibility)
Chain of Responsibility pattern passes requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain. In our bond e-trading system, we can have a chain of `TradeValidator` handlers to validate a trade.

### [Command](./Command)
Command pattern turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request's execution, and support undoable operations. In our context, `TradeExecution` can be a command in bond e-trading.

### [Interpreter](./Interpreter)
Interpreter pattern can evaluate sentences in a language. In our bond e-trading system, it can be used for evaluating and executing trade orders given in a specific language.

### [Iterator](./Iterator)
Iterator pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. In our bond e-trading system, it can be used to iterate over a `BondPortfolio`.

### [Mediator](./Mediator)
Mediator pattern reduces coupling between components by making them communicate indirectly, through a special mediator object. The `TradeMediator` can coordinate `Trader`, `MarketData`, `OrderManagement` in bond e-trading.

### [Memento](./Memento)
Memento pattern lets you save and restore the previous state of an object without revealing the details of its implementation. In our context, `BondTradeMemento` can store and restore the state of a `BondTrade`.

### [Observer](./Observer)
Observer pattern defines a subscription mechanism to notify multiple objects about any events that happen to the object they're observing. In our bond e-trading system, `TradeExecutionObserver` can notify other components about the status of a trade execution.

### [State](./State)
State pattern allows an object to change its behavior when its internal state changes. `BondTrade` can change its behavior based on its `TradeState`.

### [Strategy](./Strategy)
Strategy pattern allows an object to choose a behavior at runtime. `BondPricingStrategy` can be chosen at runtime in bond e-trading.

### [Template Method](./TemplateMethod)
Template Method pattern defines the skeleton of an algorithm in a base class but lets subclasses override specific steps of the algorithm without changing its structure. `BondIssuance` can define the steps but let `CorporateBondIssuance` and `GovernmentBondIssuance` implement the steps.

### [Visitor](./Visitor)
Visitor pattern allows adding new behaviors to existing class hierarchy without altering any existing code. `BondRatingVisitor` can add rating functionality to `Bond` classes.

## How to Run the Code

Each folder contains a separate Java project. You can clone the repository and import the project into your preferred Java IDE (like IntelliJ IDEA or Eclipse). 

This README will be updated as more patterns and examples are added to the repository.
