/**
The Facade pattern is another Structural design pattern that provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

In the context of a bond e-trading system, let's consider a subsystem that involves various operations like authentication, portfolio management, trading, and notifications. 
For a user, these individual operations can be complex. So, we introduce a Facade that provides a simplified interface to these subsystems.

Here's an example:
In the main application, the client can use the Facade to execute a trade:
The output would be:
User authenticated.
Portfolio managed.
Trade executed.
Notifications sent.

In this example, BondTradingFacade is the facade that simplifies the interaction with the complex subsystem that includes Authentication, PortfolioManagement, Trading, and Notifications.
*/

public class FacadePattern {

    // Define the subsystem classes
    public static class Authentication {
        public void authenticateUser() {
            System.out.println("User authenticated.");
        }
    }

    public static class PortfolioManagement {
        public void managePortfolio() {
            System.out.println("Portfolio managed.");
        }
    }

    public static class Trading {
        public void executeTrade() {
            System.out.println("Trade executed.");
        }
    }

    public static class Notifications {
        public void sendNotifications() {
            System.out.println("Notifications sent.");
        }
    }

    // Define the Facade
    public static class BondTradingFacade {
        private Authentication authentication;
        private PortfolioManagement portfolioManagement;
        private Trading trading;
        private Notifications notifications;

        public BondTradingFacade() {
            this.authentication = new Authentication();
            this.portfolioManagement = new PortfolioManagement();
            this.trading = new Trading();
            this.notifications = new Notifications();
        }

        public void executeTrade() {
            authentication.authenticateUser();
            portfolioManagement.managePortfolio();
            trading.executeTrade();
            notifications.sendNotifications();
        }
    }

    // Main application
    public static void main(String[] args) {
        BondTradingFacade facade = new BondTradingFacade();
        facade.executeTrade();
    }
}
