/**
The Builder pattern is useful when you need to construct complex objects. The construction is done step by step, with each step potentially able to be customized according to the requirements of the specific object being built.

In the context of bond e-trading, let's say we're dealing with BondTrade objects. Each BondTrade involves a bond, a buyer, a seller, a quantity, and a trade price. However, not all this information is available at the same time, 
and we don't want to create incomplete BondTrade objects. This is where the Builder pattern comes in handy.

Let's have a look at the Builder pattern implementation:

You can create a BondTrade object using the builder as follows:

With this pattern, you can ensure that the BondTrade object is always in a complete state and it's easy to add new parameters to the BondTrade class in the future.

*/

public class BuilderPattern {

    // Define the BondTrade class
    public static class BondTrade {
        private final String bond;
        private final String buyer;
        private final String seller;
        private final int quantity;
        private final double tradePrice;

        private BondTrade(Builder builder) {
            this.bond = builder.bond;
            this.buyer = builder.buyer;
            this.seller = builder.seller;
            this.quantity = builder.quantity;
            this.tradePrice = builder.tradePrice;
        }

        public static class Builder {
            private String bond;
            private String buyer;
            private String seller;
            private int quantity;
            private double tradePrice;

            public Builder bond(String bond) {
                this.bond = bond;
                return this;
            }

            public Builder buyer(String buyer) {
                this.buyer = buyer;
                return this;
            }

            public Builder seller(String seller) {
                this.seller = seller;
                return this;
            }

            public Builder quantity(int quantity) {
                this.quantity = quantity;
                return this;
            }

            public Builder tradePrice(double tradePrice) {
                this.tradePrice = tradePrice;
                return this;
            }

            public BondTrade build() {
                return new BondTrade(this);
            }
        }
    }

    // Main application
    public static void main(String[] args) {
        BuilderPattern.BondTrade bondTrade = new BuilderPattern.BondTrade.Builder()
            .bond("Corporate Bond A")
            .buyer("Buyer A")
            .seller("Seller B")
            .quantity(100)
            .tradePrice(102.25)
            .build();

        System.out.println("BondTrade created with bond: " + bondTrade.bond);
    }
}




