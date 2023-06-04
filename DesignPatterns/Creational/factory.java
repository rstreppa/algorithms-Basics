/**
Factory Method pattern. This is another creational design pattern that provides an interface for creating objects, but lets subclasses decide which class to instantiate.

A Factory can be useful in an e-trading system when we need to create objects that represent different types of bonds. For example, we could have CorporateBond, GovernmentBond, and MunicipalBond classes, 
all of which implement a Bond interface. A BondFactory could then create the correct type of Bond based on the parameters it's given.

Here is the Bond interface and its implementations:
Then we can implement our BondFactory like this:
Here's how you might use this Factory in the main application:

This code will output:

Corporate Bond
Government Bond
Municipal Bond

The Factory Method pattern allows us to create different types of Bond objects without exposing the instantiation logic to the client. 
This pattern is particularly useful when the object creation process can be complex or when we want to add new types of bonds in the future without changing the client code.
*/


public class FactoryPattern {

    // Define Bond interface and its implementations
    public interface Bond {
        void displayBondDetails();
    }

    public static class CorporateBond implements Bond {
        @Override
        public void displayBondDetails() {
            System.out.println("Corporate Bond");
        }
    }

    public static class GovernmentBond implements Bond {
        @Override
        public void displayBondDetails() {
            System.out.println("Government Bond");
        }
    }

    public static class MunicipalBond implements Bond {
        @Override
        public void displayBondDetails() {
            System.out.println("Municipal Bond");
        }
    }

    // Define BondFactory
    public static class BondFactory {
        public Bond createBond(String type) {
            if ("corporate".equalsIgnoreCase(type)) {
                return new CorporateBond();
            } else if ("government".equalsIgnoreCase(type)) {
                return new GovernmentBond();
            } else if ("municipal".equalsIgnoreCase(type)) {
                return new MunicipalBond();
            }
            return null;
        }
    }

    // Main application
    public static void main(String[] args) {
        BondFactory bondFactory = new BondFactory();

        Bond bond1 = bondFactory.createBond("corporate");
        bond1.displayBondDetails(); // Corporate Bond

        Bond bond2 = bondFactory.createBond("government");
        bond2.displayBondDetails(); // Government Bond

        Bond bond3 = bondFactory.createBond("municipal");
        bond3.displayBondDetails(); // Municipal Bond
    }
}
