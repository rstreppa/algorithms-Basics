/**
The Mediator pattern provides a unified interface through which different parts of a program can communicate with each other. 
Instead of components communicating directly with each other — and thus requiring knowledge of their interfaces — components send messages via the Mediator. 
This reduces the dependencies between communicating objects, thereby reducing coupling.

In the context of bond e-trading, we could use the Mediator pattern to manage communication between different components such as the Market Data Feed, Trading Algorithm, and Execution Interface.

Here is a simplified example:
In this example, the ETradingMediator manages the interaction between different components in the trading system. 
When a component sends a message, it does so through the mediator, and the mediator decides where to route the message.

*/

public interface Mediator {
    void sendMessage(String message, Colleague colleague);
}

public abstract class Colleague {
    protected Mediator mediator;

    public Colleague(Mediator m) {
        mediator = m;
    }

    public void send(String message) {
        mediator.sendMessage(message, this);
    }

    public abstract void receive(String message);
}

public class MarketDataFeed extends Colleague {
    public MarketDataFeed(Mediator m) {
        super(m);
    }

    public void receive(String message) {
        System.out.println("Market Data Feed Received: " + message);
    }
}

public class TradingAlgorithm extends Colleague {
    public TradingAlgorithm(Mediator m) {
        super(m);
    }

    public void receive(String message) {
        System.out.println("Trading Algorithm Received: " + message);
    }
}

public class ExecutionInterface extends Colleague {
    public ExecutionInterface(Mediator m) {
        super(m);
    }

    public void receive(String message) {
        System.out.println("Execution Interface Received: " + message);
    }
}

public class ETradingMediator implements Mediator {
    private MarketDataFeed marketDataFeed;
    private TradingAlgorithm tradingAlgorithm;
    private ExecutionInterface executionInterface;

    public void setMarketDataFeed(MarketDataFeed marketDataFeed) {
        this.marketDataFeed = marketDataFeed;
    }

    public void setTradingAlgorithm(TradingAlgorithm tradingAlgorithm) {
        this.tradingAlgorithm = tradingAlgorithm;
    }

    public void setExecutionInterface(ExecutionInterface executionInterface) {
        this.executionInterface = executionInterface;
    }

    public void sendMessage(String message, Colleague originator) {
        if (originator == marketDataFeed) {
            tradingAlgorithm.receive(message);
        } else if (originator == tradingAlgorithm) {
            executionInterface.receive(message);
        } else if (originator == executionInterface) {
            marketDataFeed.receive(message);
        }
    }
}

public class MediatorPatternDemo {
    public static void main(String[] args) {
        ETradingMediator mediator = new ETradingMediator();
        
        MarketDataFeed marketDataFeed = new MarketDataFeed(mediator);
        TradingAlgorithm tradingAlgorithm = new TradingAlgorithm(mediator);
        ExecutionInterface executionInterface = new ExecutionInterface(mediator);

        mediator.setMarketDataFeed(marketDataFeed);
        mediator.setTradingAlgorithm(tradingAlgorithm);
        mediator.setExecutionInterface(executionInterface);

        marketDataFeed.send("EURUSD 1.2");
        tradingAlgorithm.send("Buy EURUSD");
        executionInterface.send("Order Executed");
    }
}
