package server;

import remotes.Search;
import remotes.SearchQuery;
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class SearchServer {
    public static void main(String[] args) {
        try {
            Search search = new SearchQuery();
            LocateRegistry.createRegistry(1099); // Starts RMI registry at port 1099
            Naming.rebind("rmi://localhost:1099/REMOTE_SEARCH", search);
            System.out.println("Search Server ready");
        } catch (Exception e) {
            System.out.println("Search Server Exception: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
