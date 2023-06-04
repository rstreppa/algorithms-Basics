/**
The Command pattern is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. 
This transformation lets you pass requests as a method argument, delay or queue a request's execution, and support undoable operations.

In our bond e-trading system, we can consider the process of buying or selling a bond as a request. Here's a simplified implementation:
In the main application, the client can set a command and execute it:
Here, BuyBondCommand and SellBondCommand are concrete command objects that encapsulate a request. TradingDesk acts as an invoker object, and BondTradingSystem is the receiver object.

*/


public class CommandPattern {

    public static class Bond {
        private String name;
        private int price;

        public Bond(String name, int price) {
            this.name = name;
            this.price = price;
        }

        @Override
        public String toString() {
            return name + " at price " + price;
        }
    }

    public interface OrderCommand {
        void execute();
    }

    public static class BuyBondCommand implements OrderCommand {
        private BondTradingSystem system;
        private Bond bond;

        public BuyBondCommand(BondTradingSystem system, Bond bond) {
            this.system = system;
            this.bond = bond;
        }

        @Override
        public void execute() {
            system.buy(bond);
        }
    }

    public static class SellBondCommand implements OrderCommand {
        private BondTradingSystem system;
        private Bond bond;

        public SellBondCommand(BondTradingSystem system, Bond bond) {
            this.system = system;
            this.bond = bond;
        }

        @Override
        public void execute() {
            system.sell(bond);
        }
    }

    public static class BondTradingSystem {
        public void buy(Bond bond) {
            System.out.println("Buying bond: " + bond);
        }

        public void sell(Bond bond) {
            System.out.println("Selling bond: " + bond);
        }
    }

    public static class TradingDesk {
        private OrderCommand command;

        public void setCommand(OrderCommand command) {
            this.command = command;
        }

        public void executeCommand() {
            command.execute();
        }
    }

    public static void main(String[] args) {
        BondTradingSystem system = new BondTradingSystem();
        Bond bond = new Bond("Bond A", 100);

        TradingDesk tradingDesk = new TradingDesk();

        // Buy command
        tradingDesk.setCommand(new BuyBondCommand(system, bond));
        tradingDesk.executeCommand();

        // Sell command
        tradingDesk.setCommand(new SellBondCommand(system, bond));
        tradingDesk.executeCommand();
    }
}
