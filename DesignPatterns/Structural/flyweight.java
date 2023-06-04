/**
The Flyweight pattern is a structural design pattern that's used to reduce the memory and resource usage for complex models containing many similar objects. 
It achieves this by sharing as much data as possible with other similar objects, these shared objects are called flyweights.

In the context of bond e-trading, we can consider the case of managing a large number of Bond objects. Each bond object has some unique information (like its identifier) and some shared information (like the issuer information, 
which can be the same for many bonds). We can use the Flyweight pattern to reduce the memory usage by sharing the issuer information.

Here's an example:
In the main application, you would use it like this:

In this example, BondIssuerFactory is a factory for flyweight BondIssuer objects. 
It ensures that only one BondIssuer object is created for each issuer name. Bond objects with the same issuer will share a BondIssuer object, reducing memory usage.

*/


import java.util.HashMap;
import java.util.Map;

public class FlyweightPattern {

    // Define the BondIssuer class
    public static class BondIssuer {
        private String name;

        public BondIssuer(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }
    }

    // Define the Bond class
    public static class Bond {
        private String identifier;
        private BondIssuer issuer;

        public Bond(String identifier, BondIssuer issuer) {
            this.identifier = identifier;
            this.issuer = issuer;
        }

        // other bond-specific methods
    }

    // Define the BondIssuerFactory class
    public static class BondIssuerFactory {
        private Map<String, BondIssuer> issuers;

        public BondIssuerFactory() {
            this.issuers = new HashMap<>();
        }

        public BondIssuer getIssuer(String name) {
            if (!issuers.containsKey(name)) {
                issuers.put(name, new BondIssuer(name));
            }
            return issuers.get(name);
        }
    }

    // Main application
    public static void main(String[] args) {
        BondIssuerFactory factory = new BondIssuerFactory();
        
        Bond bond1 = new Bond("123", factory.getIssuer("IssuerA"));
        Bond bond2 = new Bond("456", factory.getIssuer("IssuerA"));  // reuses existing issuer
        
        // ... other bonds with the same or different issuers
    }
}
