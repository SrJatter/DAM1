package col.hotel.controller;

import col.hotel.model.Room;
import col.hotel.model.Worker;

import java.util.HashMap;
import java.util.Map;

public class Hotel {
    private static Hotel instance;
    private int money;
    private Map<String, Room> rooms;
    private Map<Integer, Worker> workers;
    private Hotel() {
        this.money = 1000;
        this.rooms = new HashMap<>();
        this.workers = new HashMap<>();
    }

    public static Hotel getInstance() {
        if (instance == null) {
            instance = new Hotel();
        }
        return instance;
    }
    public Map<String, Room> getRooms() {
        return rooms;
    }
}

