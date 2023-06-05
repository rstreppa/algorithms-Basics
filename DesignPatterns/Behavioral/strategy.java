/**
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

For a bond e-trading system, an example of the Strategy pattern could be having different algorithms for calculating the price of a bond based on different market conditions. 
Let's illustrate this with an example:
In this code, PricingStrategy is a strategy interface that defines a calculatePrice method. 
NormalMarketConditionPricing and VolatileMarketConditionPricing are concrete strategies that implement the PricingStrategy. 
The Bond class uses a PricingStrategy to calculate its price.
*/

public class StrategyPattern {

    interface PricingStrategy {
        double calculatePrice(double faceValue, double coupon, int yearsToMaturity);
    }

    static class NormalMarketConditionPricing implements PricingStrategy {
        public double calculatePrice(double faceValue, double coupon, int yearsToMaturity) {
            // Implement the pricing logic for normal market conditions here...
            return faceValue + coupon * yearsToMaturity;
        }
    }

    static class VolatileMarketConditionPricing implements PricingStrategy {
        public double calculatePrice(double faceValue, double coupon, int yearsToMaturity) {
            // Implement the pricing logic for volatile market conditions here...
            return faceValue + 0.9 * coupon * yearsToMaturity;
        }
    }

    static class Bond {
        private PricingStrategy pricingStrategy;

        public Bond(PricingStrategy pricingStrategy) {
            this.pricingStrategy = pricingStrategy;
        }

        public double calculatePrice(double faceValue, double coupon, int yearsToMaturity) {
            return this.pricingStrategy.calculatePrice(faceValue, coupon, yearsToMaturity);
        }
    }

    public static void main(String[] args) {
        Bond bond1 = new Bond(new NormalMarketConditionPricing());
        System.out.println("Bond Price: " + bond1.calculatePrice(1000, 50, 10));

        Bond bond2 = new Bond(new VolatileMarketConditionPricing());
        System.out.println("Bond Price: " + bond2.calculatePrice(1000, 50, 10));
    }
}
