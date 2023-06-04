/**
The Proxy pattern is a structural design pattern that provides an object that acts as a surrogate or placeholder for another object. 
The proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

In the context of bond e-trading, let's say we have a BondTradeExecutor interface, and a RealBondTradeExecutor class that executes the trade. We could also have a BondTradeExecutorProxy that logs the execution before and after the actual execution.

Here's an example:
In the main application, the client can use the Proxy to execute a trade:
The output would be:
Logging before execution...
Executing Bond Trade...
Logging after execution...

In this example, BondTradeExecutorProxy is the proxy that controls access to the RealBondTradeExecutor.
*/

public class ProxyPattern {

    // Define the BondTradeExecutor interface
    public interface BondTradeExecutor {
        void executeTrade();
    }

    // Define the RealBondTradeExecutor class
    public static class RealBondTradeExecutor implements BondTradeExecutor {
        @Override
        public void executeTrade() {
            System.out.println("Executing Bond Trade...");
        }
    }

    // Define the BondTradeExecutorProxy class
    public static class BondTradeExecutorProxy implements BondTradeExecutor {
        private RealBondTradeExecutor realExecutor;

        public BondTradeExecutorProxy() {
            this.realExecutor = new RealBondTradeExecutor();
        }

        @Override
        public void executeTrade() {
            System.out.println("Logging before execution...");
            realExecutor.executeTrade();
            System.out.println("Logging after execution...");
        }
    }

    // Main application
    public static void main(String[] args) {
        BondTradeExecutor executor = new BondTradeExecutorProxy();
        executor.executeTrade();
    }
}
