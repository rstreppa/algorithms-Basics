/**
The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. 
This pattern is common in event handling systems.

In a bond e-trading system, an example use of the Observer pattern could be for updating different system components whenever a bond's price changes. 
In this example, Bond is the subject being observed, and TradingAlgorithm represents an observer. Whenever the bond's price changes (bond.setPrice()), all registered observers (i.e., trading algorithms) get notified.For example, you might have multiple trading algorithms that need to be notified when a bond's price changes so they can make decisions.

Here's a basic example:
In this example, Bond is the subject being observed, and TradingAlgorithm represents an observer. 
Whenever the bond's price changes (bond.setPrice()), all registered observers (i.e., trading algorithms) get notified.
*/

import java.util.ArrayList;
import java.util.List;

public class ObserverPattern {

    interface Observer {
        void update(double price);
    }

    static class Bond {
        private List<Observer> observers = new ArrayList<>();
        private double price;

        void attach(Observer observer) {
            observers.add(observer);
        }

        void notifyAllObservers() {
            for (Observer observer : observers) {
                observer.update(price);
            }
        }

        void setPrice(double price) {
            this.price = price;
            notifyAllObservers();
        }
    }

    static class TradingAlgorithm implements Observer {
        private String name;

        TradingAlgorithm(String name) {
            this.name = name;
        }

        @Override
        public void update(double price) {
            System.out.println("Trading Algorithm " + name + " notified. New Price: " + price);
            // Implement trading logic here...
        }
    }

    public static void main(String[] args) {
        Bond bond = new Bond();

        bond.attach(new TradingAlgorithm("Algorithm1"));
        bond.attach(new TradingAlgorithm("Algorithm2"));

        bond.setPrice(100.25);
        bond.setPrice(101.50);
    }
}
