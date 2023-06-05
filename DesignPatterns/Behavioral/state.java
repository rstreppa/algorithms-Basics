/**
The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

In the context of bond e-trading, let's consider a BondOrder that can be in one of three states: New, Submitted, or Fulfilled.

Here is a simplified example:
In this code, OrderState is a state interface defining the next and printStatus methods. New, Submitted, and Fulfilled are concrete states implementing OrderState. 
The BondOrder class maintains a reference to an instance of OrderState, representing the current state of the order.

*/


public class StatePattern {

    interface OrderState {
        void next(BondOrder order);
        void printStatus();
    }

    static class New implements OrderState {
        public void next(BondOrder order) {
            order.setState(new Submitted());
        }

        public void printStatus() {
            System.out.println("New order.");
        }
    }

    static class Submitted implements OrderState {
        public void next(BondOrder order) {
            order.setState(new Fulfilled());
        }

        public void printStatus() {
            System.out.println("Order has been submitted.");
        }
    }

    static class Fulfilled implements OrderState {
        public void next(BondOrder order) {
            System.out.println("Order is fulfilled. No further state change possible.");
        }

        public void printStatus() {
            System.out.println("Order has been fulfilled.");
        }
    }

    static class BondOrder {
        private OrderState state = new New();

        void setState(OrderState state) {
            this.state = state;
        }

        void nextState() {
            state.next(this);
        }

        void printStatus() {
            state.printStatus();
        }
    }

    public static void main(String[] args) {
        BondOrder order = new BondOrder();

        order.printStatus();
        order.nextState();

        order.printStatus();
        order.nextState();

        order.printStatus();
        order.nextState();

        order.printStatus();
    }
}
