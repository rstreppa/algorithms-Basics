/**
The Decorator pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. 
It involves a set of decorator classes that are used to wrap concrete objects. Decorator classes mirror the type of the objects they decorate, they add or override behavior.

In the context of our bond e-trading system, let's consider that we have a basic bond trading operation and we want to add more features to it like logging and notifications. 
These additional features can be seen as decorations on the basic trading operation.

When you run this program, you'll get:
Executing Basic Bond Trade...
Logging Bond Trade...
Sending Notification for Bond Trade...

In this example, BasicBondTrade is the concrete object which gets decorated first with LoggingBondTrade and then with NotificationBondTrade.

In the Decorator pattern, making the decorator class (BondTradeDecorator in this case) abstract is a common practice but not a strict requirement. This is done for two primary reasons:
Consistency: It helps ensure that all specific decorators (like LoggingBondTrade and NotificationBondTrade) have a consistent interface.
Preventing instantiation: It prevents the decorator class from being instantiated on its own, which typically doesn't make sense in the context of this pattern. 
The decorator class is designed to "decorate" or add functionality to instances of other classes, so creating an instance of the decorator class by itself wouldn't be very useful.
However, if you have a valid use case for creating instances of the decorator class, you could make it a concrete class instead of an abstract one. 
You could also provide default implementation for the added behavior, which can be overridden by specific decorators.
So, in the context of Java's Decorator pattern, it's generally a good idea to declare the decorator class as abstract, but it's not a hard rule and depends on your specific needs and use case.

*/


public class DecoratorPattern {

    // Define the BondTrade interface and its concrete implementation
    public interface BondTrade {
        void executeTrade();
    }

    public static class BasicBondTrade implements BondTrade {
        @Override
        public void executeTrade() {
            System.out.println("Executing Basic Bond Trade...");
        }
    }

    // Define the abstract BondTradeDecorator and its concrete implementations
    public static abstract class BondTradeDecorator implements BondTrade {
        protected BondTrade decoratedTrade;

        public BondTradeDecorator(BondTrade decoratedTrade) {
            this.decoratedTrade = decoratedTrade;
        }

        public void executeTrade() {
            decoratedTrade.executeTrade();
        }
    }

    public static class LoggingBondTrade extends BondTradeDecorator {
        public LoggingBondTrade(BondTrade decoratedTrade) {
            super(decoratedTrade);
        }

        @Override
        public void executeTrade() {
            super.executeTrade();
            System.out.println("Logging Bond Trade...");
        }
    }

    public static class NotificationBondTrade extends BondTradeDecorator {
        public NotificationBondTrade(BondTrade decoratedTrade) {
            super(decoratedTrade);
        }

        @Override
        public void executeTrade() {
            super.executeTrade();
            System.out.println("Sending Notification for Bond Trade...");
        }
    }

    // Main application
    public static void main(String[] args) {
        BondTrade trade = new BasicBondTrade();
        BondTrade loggingTrade = new LoggingBondTrade(trade);
        BondTrade notificationTrade = new NotificationBondTrade(loggingTrade);

        notificationTrade.executeTrade();
    }
}
