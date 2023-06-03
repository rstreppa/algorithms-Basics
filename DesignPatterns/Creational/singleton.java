/**
This shows that we successfully created a single TradingManager instance and used it to trade a bond. This is just a simple demonstration; in a real e-trading system, the trade method would involve much more complex logic.
This Singleton pattern ensures that there's only ever one TradingManager in our application, which is beneficial because we have a single point of control and coordination for all trades.

This program will output:
Trading 10 units of bond: Corporate Bond

*/


public class TradingManager {
    private static TradingManager instance;

    // Make constructor private so it cannot be instantiated from outside
    private TradingManager() {}

    public static synchronized TradingManager getInstance() {
        if (instance == null) {
            instance = new TradingManager();
        }
        return instance;
    }

    // Trade method
    public void trade(Bond bond, int quantity) {
        System.out.println("Trading " + quantity + " units of bond: " + bond.getName());
        // Implement the logic of trading
    }
}

// Define a Bond class for use in our TradingManager
class Bond {
    private final String name;

    Bond(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}

// Main class to test the Singleton instance
public class Main {
    public static void main(String[] args) {
        TradingManager manager = TradingManager.getInstance();

        Bond bond = new Bond("Corporate Bond");
        manager.trade(bond, 10);
    }
}
