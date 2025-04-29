package client;

import remotes.Search;
import java.rmi.Naming;

public class ClientRequest {
    public static void main(String[] args) {
        try {
            String searchQuery = (args.length < 1) ? "p2p" : args[0];
            String url = "rmi://localhost:1099/REMOTE_SEARCH";
            Search access = (Search) Naming.lookup(url);
            String result = access.query(searchQuery);
            System.out.println("Found: " + result);
        } catch (Exception e) {
            System.out.println("ClientRequest Exception: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
