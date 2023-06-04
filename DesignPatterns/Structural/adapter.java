/**
The Adapter pattern works as a bridge between two incompatible interfaces. This type of design pattern comes under structural patterns, as it combines the capability of two independent interfaces.
In the context of bond e-trading, imagine you have a third-party library that gives information about bonds but in a format that's not directly usable by your system. 
Let's say your system expects a Bond object with a getBondDetails() method, while the third-party library provides a ExternalBond object with a fetchInfo() method.

We need to create an adapter class that can take ExternalBond and make it work with our system which expects a Bond:
And here's how you could use it in your main application:

The Adapter pattern allows you to integrate components that couldn't otherwise work together due to incompatible interfaces, and is particularly useful when you need to work with legacy or third-party code that you can't modify.
*/

public class AdapterPattern {

    // Define Bond interface and its implementation
    public interface Bond {
        String getBondDetails();
    }

    public static class CorporateBond implements Bond {
        @Override
        public String getBondDetails() {
            return "Corporate Bond Details";
        }
    }

    // Define ExternalBond class
    public static class ExternalBond {
        public String fetchInfo() {
            return "External Bond Information";
        }
    }

    // Define BondAdapter class
    public static class BondAdapter implements Bond {
        private ExternalBond externalBond;

        public BondAdapter(ExternalBond externalBond) {
            this.externalBond = externalBond;
        }

        @Override
        public String getBondDetails() {
            return adaptInfo(externalBond.fetchInfo());
        }

        private String adaptInfo(String info) {
            // Transform info into the format needed
            return "Adapted Info: " + info;
        }
    }

    // Main application
    public static void main(String[] args) {
        ExternalBond externalBond = new ExternalBond();
        Bond bondAdapter = new BondAdapter(externalBond);

        System.out.println(bondAdapter.getBondDetails());  // Adapted Info: External Bond Information
    }
}
