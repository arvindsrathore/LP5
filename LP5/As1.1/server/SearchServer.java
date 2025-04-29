package server;

import remotes.Search;
import remotes.SearchQuery;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class SearchServer {
    public static void main(String[] args) throws RemoteException, MalformedURLException {
        Search search = new SearchQuery();
        LocateRegistry.createRegistry(1099); // Starts RMI registry at port 1099
        Naming.rebind("rmi://localhost:1099/REMOTE_SEARCH", search);
        System.out.println("Search Server ready");
    }
}