/**
The Memento pattern provides a way to capture and externalize an object's internal state without violating encapsulation, so that the object can be restored to this state later if needed. 
This is particularly useful when we need to provide some sort of undo functionality.

In a bond trading context, a use case for the Memento pattern could be to save the state of a bond order before it's executed. 
If we then need to revert the order for some reason (maybe the market conditions changed rapidly), we can do so easily.

Here's an example:
This example models a bond order ("Bond order 1", "Bond order 2", etc.) that's being set and then saved via Mementos. 
Later, the originator can restore its state from any of these saved Mementos, providing an 'undo' functionality.

*/


public class MementoPattern {
    static class Memento {
        private String bondOrder;

        public Memento(String bondOrderSave) {
            bondOrder = bondOrderSave;
        }

        public String getSavedBondOrder() {
            return bondOrder;
        }
    }

    static class Originator {
        private String bondOrder;

        public void set(String newBondOrder) {
            System.out.println("Originator: Setting bond order to " + newBondOrder);
            this.bondOrder = newBondOrder;
        }

        public Memento storeInMemento() {
            System.out.println("Originator: Saving to Memento.");
            return new Memento(bondOrder);
        }

        public String restoreFromMemento(Memento memento) {
            bondOrder = memento.getSavedBondOrder();
            System.out.println("Originator: Bond order after restoring from Memento: " + bondOrder);
            return bondOrder;
        }
    }

    static class Caretaker {
        private List<Memento> savedStates = new ArrayList<>();

        public void addMemento(Memento m) {
            savedStates.add(m);
        }

        public Memento getMemento(int index) {
            return savedStates.get(index);
        }
    }

    public static void main(String[] args) {
        List<Memento> savedStates = new ArrayList<>();

        Originator originator = new Originator();
        Caretaker caretaker = new Caretaker();

        originator.set("Bond order 1");
        caretaker.addMemento(originator.storeInMemento());

        originator.set("Bond order 2");
        caretaker.addMemento(originator.storeInMemento());

        originator.set("Bond order 3");
        caretaker.addMemento(originator.storeInMemento());

        // Restore to desired state
        originator.restoreFromMemento(caretaker.getMemento(0));
    }
}
