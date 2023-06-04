/**
The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently. 
It separates the abstract elements of a class from the implementation details, providing the means to replace the implementation details without modifying the abstraction.

In our bond e-trading context, let's consider an abstraction Trade with the method execute(). 
We can have different types of trades, such as BuyTrade and SellTrade. However, the execution of these trades can vary based on the type of bond, for example GovernmentBond or CorporateBond.

Here's how we can set this up:
And here's how you could use it in your main application:

In this example, Trade and TradeExecutor can evolve independently without impacting each other. The Bridge pattern allows you to avoid permanent binding between an abstraction and its implementation. 
It's particularly useful when the implementation must be selected or switched at runtime.

The "bridge" is represented by the abstract class AbstractTrade. This class is the bridge between the abstraction (Trade interface) and its implementation (TradeExecutor interface).
In other words, AbstractTrade separates the Trade interface from the TradeExecutor interface, allowing them to vary independently. 
This bridge allows the Trade (abstraction) to interact with the TradeExecutor (implementation) without knowing the concrete classes that implement TradeExecutor. 
The concrete classes BuyTrade and SellTrade that extend AbstractTrade work with different implementations of TradeExecutor (GovernmentBondExecutor and CorporateBondExecutor), but the bridge itself remains the same.
*/

public class BridgePattern {

    // Define Trade interface and its abstract implementation
    public interface Trade {
        void execute();
    }

    public static abstract class AbstractTrade implements Trade {
        protected TradeExecutor executor;

        protected AbstractTrade(TradeExecutor executor) {
            this.executor = executor;
        }

        @Override
        public abstract void execute();
    }

    // Define BuyTrade and SellTrade classes
    public static class BuyTrade extends AbstractTrade {
        public BuyTrade(TradeExecutor executor) {
            super(executor);
        }

        @Override
        public void execute() {
            executor.executeTrade();
            System.out.println("Buy trade executed.");
        }
    }

    public static class SellTrade extends AbstractTrade {
        public SellTrade(TradeExecutor executor) {
            super(executor);
        }

        @Override
        public void execute() {
            executor.executeTrade();
            System.out.println("Sell trade executed.");
        }
    }

    // Define TradeExecutor interface and its implementations
    public interface TradeExecutor {
        void executeTrade();
    }

    public static class GovernmentBondExecutor implements TradeExecutor {
        @Override
        public void executeTrade() {
            System.out.println("Government Bond traded.");
        }
    }

    public static class CorporateBondExecutor implements TradeExecutor {
        @Override
        public void executeTrade() {
            System.out.println("Corporate Bond traded.");
        }
    }

    // Main application
    public static void main(String[] args) {
        Trade buyTrade = new BuyTrade(new GovernmentBondExecutor());
        buyTrade.execute();

        Trade sellTrade = new SellTrade(new CorporateBondExecutor());
        sellTrade.execute();
    }
}
