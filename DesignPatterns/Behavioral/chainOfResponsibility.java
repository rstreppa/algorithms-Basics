/**
The Chain of Responsibility pattern is a behavioral design pattern that lets you pass requests along a chain of handlers. 
Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

In our bond e-trading context, let's consider a trade validation process. Here, each validation is a link in the chain, checking one aspect of the trade. 
A Validator interface defines a method validate and setNext. The validate method handles the request, while the setNext method is used to build the chain.

In the main application, the client can build the chain and validate a trade:

In this example, BondValidator, PriceValidator, and QuantityValidator are the handlers in the chain of responsibility. If a validator cannot handle a request (i.e., validation fails), it won't call the next validator.
*/


public class ChainOfResponsibilityPattern {

    public static class Trade {
        private String type;
        private int price;
        private int quantity;

        public Trade(String type, int price, int quantity) {
            this.type = type;
            this.price = price;
            this.quantity = quantity;
        }

        public String getType() {
            return type;
        }

        public int getPrice() {
            return price;
        }

        public int getQuantity() {
            return quantity;
        }
    }

    public interface Validator {
        void setNext(Validator validator);
        void validate(Trade trade);
    }

    public static class BondValidator implements Validator {
        private Validator next;

        @Override
        public void setNext(Validator validator) {
            next = validator;
        }

        @Override
        public void validate(Trade trade) {
            if (trade.getType().equals("bond")) {
                System.out.println("Bond validator passed...");
                if (next != null) {
                    next.validate(trade);
                }
            } else {
                System.out.println("Bond validator failed...");
            }
        }
    }

    public static class PriceValidator implements Validator {
        private Validator next;

        @Override
        public void setNext(Validator validator) {
            next = validator;
        }

        @Override
        public void validate(Trade trade) {
            if (trade.getPrice() > 0) {
                System.out.println("Price validator passed...");
                if (next != null) {
                    next.validate(trade);
                }
            } else {
                System.out.println("Price validator failed...");
            }
        }
    }

    public static class QuantityValidator implements Validator {
        private Validator next;

        @Override
        public void setNext(Validator validator) {
            next = validator;
        }

        @Override
        public void validate(Trade trade) {
            if (trade.getQuantity() > 0) {
                System.out.println("Quantity validator passed...");
                if (next != null) {
                    next.validate(trade);
                }
            } else {
                System.out.println("Quantity validator failed...");
            }
        }
    }

    public static void main(String[] args) {
        Validator bondValidator = new BondValidator();
        Validator priceValidator = new PriceValidator();
        Validator quantityValidator = new QuantityValidator();

        bondValidator.setNext(priceValidator);
        priceValidator.setNext(quantityValidator);

        Trade trade = new Trade("bond", 100, 10);
        bondValidator.validate(trade);
    }
}
