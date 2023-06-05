/**
The Visitor pattern represents an operation to be performed on elements of an object structure. It allows you to define a new operation without changing the classes of the elements on which it operates.
More specifically, it allows objects of the Visitor class to visit the tree and traverse the target class structure via the accept method.
For our bond e-trading system, let's consider that we have different types of bonds, and we want to implemtarget ent a functionality that calculates the yield for each bond type differently. 
Here's how we can use the Visitor pattern to achieve this:
In this example, Bond is an element interface that defines an accept method for accepting a BondVisitor. CorporateBond and GovernmentBond are concrete elements that implement accept method. 
BondVisitor is a visitor interface that defines visit methods for different types of bonds. YieldCalculator is a concrete visitor that implements the visit methods.

*/


public class VisitorPattern {

    interface Bond {
        void accept(BondVisitor visitor);
    }

    static class CorporateBond implements Bond {
        public void accept(BondVisitor visitor) {
            visitor.visit(this);
        }
    }

    static class GovernmentBond implements Bond {
        public void accept(BondVisitor visitor) {
            visitor.visit(this);
        }
    }

    interface BondVisitor {
        void visit(CorporateBond bond);
        void visit(GovernmentBond bond);
    }

    static class YieldCalculator implements BondVisitor {
        public void visit(CorporateBond bond) {
            System.out.println("Calculate yield for corporate bond...");
            // Yield calculation logic for corporate bonds...
        }

        public void visit(GovernmentBond bond) {
            System.out.println("Calculate yield for government bond...");
            // Yield calculation logic for government bonds...
        }
    }

    public static void main(String[] args) {
        BondVisitor yieldCalculator = new YieldCalculator();
        
        Bond corporateBond = new CorporateBond();
        corporateBond.accept(yieldCalculator);

        Bond governmentBond = new GovernmentBond();
        governmentBond.accept(yieldCalculator);
    }
}
