/**
The Interpreter pattern is a behavioral design pattern that provides a way to evaluate language grammar or expression. 
This pattern involves implementing an expression interface which tells to interpret a particular context.

Let's take an example from our bond e-trading system. We might have a simple filtering system for bonds based on their type and price. 
We could interpret a string such as "bond AND price > 100" to filter all bonds of type 'bond' and price greater than 100.

This is a simple interpretation, and actual parsing of expressions can be complex. Here, AndExpression, OrExpression, and TerminalExpression are interpreters, and they interpret a string based on the rules we defined. 
isHighPriceBond is an interpreter which will return true if the string is "Bond Price > 100".

*/

public class InterpreterPattern {

    public interface Expression {
        boolean interpret(String context);
    }

    public static class TerminalExpression implements Expression {
        private String data;

        public TerminalExpression(String data) {
            this.data = data;
        }

        @Override
        public boolean interpret(String context) {
            return context.contains(data);
        }
    }

    public static class OrExpression implements Expression {
        private Expression expr1 = null;
        private Expression expr2 = null;

        public OrExpression(Expression expr1, Expression expr2) {
            this.expr1 = expr1;
            this.expr2 = expr2;
        }

        @Override
        public boolean interpret(String context) {
            return expr1.interpret(context) || expr2.interpret(context);
        }
    }

    public static class AndExpression implements Expression {
        private Expression expr1 = null;
        private Expression expr2 = null;

        public AndExpression(Expression expr1, Expression expr2) {
            this.expr1 = expr1;
            this.expr2 = expr2;
        }

        @Override
        public boolean interpret(String context) {
            return expr1.interpret(context) && expr2.interpret(context);
        }
    }

    public static void main(String[] args) {
        Expression bond = new TerminalExpression("Bond");
        Expression highPrice = new TerminalExpression("Price > 100");

        Expression isHighPriceBond = new AndExpression(bond, highPrice);

        System.out.println("Is this a high-priced bond? " + isHighPriceBond.interpret("Bond Price > 100"));
    }
}
