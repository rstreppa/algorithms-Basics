/**
The Composite pattern is a structural design pattern that lets you compose objects into tree structures to represent part-whole hierarchies. Composite allows clients to treat individual objects and compositions of objects uniformly.

In the bond e-trading system, let's say we have different types of bonds, and we want to keep track of their total value. Some bonds can be standalone, while others could be composed of multiple other bonds. 
Here's how you can implement the Composite pattern:
And here's how you could use it in your main application:

In this example, BondComponent is the base component, IndividualBond is the leaf, and BondComposite is the composite. Both IndividualBond and BondComposite implement BondComponent so they can be treated uniformly.
*/

import java.util.ArrayList;
import java.util.List;

public class CompositePattern {

    // Define BondComponent interface and its implementations
    public interface BondComponent {
        double getPrice();
    }

    public static class IndividualBond implements BondComponent {
        private double price;

        public IndividualBond(double price) {
            this.price = price;
        }

        @Override
        public double getPrice() {
            return price;
        }
    }

    public static class BondComposite implements BondComponent {
        private List<BondComponent> components = new ArrayList<>();

        public void addComponent(BondComponent component) {
            components.add(component);
        }

        @Override
        public double getPrice() {
            double total = 0;
            for (BondComponent component : components) {
                total += component.getPrice();
            }
            return total;
        }
    }

    // Main application
    public static void main(String[] args) {
        IndividualBond bond1 = new IndividualBond(100);
        IndividualBond bond2 = new IndividualBond(200);
        IndividualBond bond3 = new IndividualBond(300);

        BondComposite composite1 = new BondComposite();
        composite1.addComponent(bond1);
        composite1.addComponent(bond2);

        BondComposite composite2 = new BondComposite();
        composite2.addComponent(bond3);
        composite2.addComponent(composite1);

        System.out.println(composite2.getPrice());  // Outputs: 600.0
    }
}
