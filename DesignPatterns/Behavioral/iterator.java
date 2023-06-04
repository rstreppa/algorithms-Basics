/**
The Iterator pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. 
This pattern is very commonly used in Java Collection Framework where java.util.Iterator interface provides methods for traversing through a collection.

In the context of our bond e-trading system, suppose we have a collection of bonds and we want to iterate through them. We could implement an iterator as follows:

In this code, BondCollection creates an iterator for the client. The client then uses this iterator to iterate through the bonds. 
This way, the client doesn't need to know the internal details of how the bonds are stored in the collection.
*/



import java.util.*;

public class IteratorPattern {
    
    public static class Bond {
        private String name;
        private int price;

        public Bond(String name, int price) {
            this.name = name;
            this.price = price;
        }

        @Override
        public String toString() {
            return "Bond{" +
                    "name='" + name + '\'' +
                    ", price=" + price +
                    '}';
        }
    }

    public interface BondIterator {
        boolean hasNext();
        Bond next();
    }

    public static class BondCollection {
        List<Bond> bondList;

        public BondCollection() {
            bondList = new ArrayList<>();

            // add some bonds to bondList
            addBond(new Bond("Bond A", 100));
            addBond(new Bond("Bond B", 200));
        }

        public void addBond(Bond bond) {
            bondList.add(bond);
        }

        public BondIterator createIterator() {
            return new BondListIterator(bondList);
        }
    }

    public static class BondListIterator implements BondIterator {
        List<Bond> bondList;
        int position = 0;

        public BondListIterator(List<Bond> bondList) {
            this.bondList = bondList;
        }

        @Override
        public boolean hasNext() {
            return position < bondList.size() && bondList.get(position) != null;
        }

        @Override
        public Bond next() {
            Bond bond = bondList.get(position);
            position = position + 1;
            return bond;
        }
    }

    public static void main(String args[]) {
        BondCollection bonds = new BondCollection();
        BondIterator bondIterator = bonds.createIterator();

        while (bondIterator.hasNext()) {
            Bond bond = bondIterator.next();
            System.out.println(bond);
        }
    }
}
