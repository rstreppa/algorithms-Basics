/**
Let's move on to the Prototype pattern. This is another creational pattern that specifies the kind of objects to create using a prototypical instance and creates new objects by cloning this prototype.
Let's say we have a Bond class that's relatively expensive to instantiate, perhaps because it needs to fetch data from a database or an external service. 
But once we have one instance of Bond, we might want to create more that are similar, but not identical - they may represent the same type of bond, but have different values for some properties.

In this example, we have a Bond class that we can create a clone of by calling the clone() method. This way, we can quickly create new Bond objects without having to go through the expensive instantiation process for each one.
To manage the prototypes, we might use a BondCache class that holds a Map of prototypes. When we want a new Bond, we first ask the BondCache for a prototype and then clone that prototype.

We could use the Prototype pattern in our main application like this:

This code will output:
Bond : corporate
Bond : government
*/


import java.util.HashMap;

public class PrototypePattern {

    // Define abstract Bond class
    public static abstract class Bond implements Cloneable {
        protected String type;
        protected double price;

        abstract void setPrice(double price);

        public String getType() {
            return type;
        }

        public Object clone() {
            Object clone = null;
            try {
                clone = super.clone();
            } catch (CloneNotSupportedException e) {
                e.printStackTrace();
            }
            return clone;
        }
    }

    // Define concrete CorporateBond class
    public static class CorporateBond extends Bond {
        public CorporateBond() {
            this.type = "corporate";
        }

        @Override
        public void setPrice(double price) {
            this.price = price;
        }
    }

    // Define concrete GovernmentBond class
    public static class GovernmentBond extends Bond {
        public GovernmentBond() {
            this.type = "government";
        }

        @Override
        public void setPrice(double price) {
            this.price = price;
        }
    }

    // Define BondCache to store prototypes
    public static class BondCache {

        private static HashMap<String, Bond> bondMap  = new HashMap<>();

        public static Bond getBond(String bondType) {
            Bond cachedBond = bondMap.get(bondType);
            return (Bond) cachedBond.clone();
        }

        public static void loadCache() {
            CorporateBond corporateBond = new CorporateBond();
            corporateBond.setPrice(100.0);
            bondMap.put("corporate", corporateBond);

            GovernmentBond governmentBond = new GovernmentBond();
            governmentBond.setPrice(200.0);
            bondMap.put("government", governmentBond);
        }
    }

    // Main application
    public static void main(String[] args) {
        BondCache.loadCache();

        Bond clonedBond = BondCache.getBond("corporate");
        System.out.println("Bond : " + clonedBond.getType());

        Bond clonedBond2 = BondCache.getBond("government");
        System.out.println("Bond : " + clonedBond2.getType());
    }
}
