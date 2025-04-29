package client;

import remotes.Search;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

public class ClientRequest {
    public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
        String searchQuery = (args.length < 1) ? "p2p" : args[0];
        String url = "rmi://localhost:1099/REMOTE_SEARCH";
        Search access = (Search) Naming.lookup(url);
        String result = access.query(searchQuery);
        System.out.println("Found: " + result);
    }
}
