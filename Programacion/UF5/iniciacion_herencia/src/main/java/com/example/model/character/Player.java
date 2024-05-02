package com.example.model.character;

import com.example.model.enums.Place;
import com.example.model.items.Item;

import java.util.ArrayList;

public class Player extends Character implements Comparable<Player>{
    private int calacoins;
    private int lvl;
    private int friendshipPoints;
    private ArrayList<Item> inventory;

    public Player(String name) {
        super(name, Place.SECRETARIA);
        this.calacoins = 100;
        this.lvl = 1;
        this.friendshipPoints = 0;
        this.inventory = new ArrayList<>();
    }

    public void increaseCalacoins(int calacoins) {
        this.calacoins += calacoins;
    }
    public void decreaseCalacoins(int calacoins) {
        this.calacoins -= calacoins;
    }

    public void levelUp() {
        this.lvl += 1;
        this.calacoins += 50;
    }

    public void riseFriendshipPoints(int friendshipPoints) {
        this.friendshipPoints += friendshipPoints;
        do {
            if (this.friendshipPoints >= 15) {
                this.friendshipPoints -= 15;
                levelUp();
            }
        } while (this.friendshipPoints >= 15);
    }

    public void buy(Item item) {
        int price = item.getPrice();
        this.calacoins -= price;
        addItemToInventory(item);
    }
    public void addItemToInventory(Item item) {
        this.inventory.add(item);
    }

    @Override
    public String toString() {
        return super.toString() + " - Calacoins: " + calacoins + " - Nivell: " + lvl + " - Punts: " + friendshipPoints;
    }

    public int getCalacoins() {
        return calacoins;
    }

    public int getLvl() {
        return lvl;
    }


    public int getFriendshipPoints() {
        return friendshipPoints;
    }

    public ArrayList<Item> getInventory() {
        return inventory;
    }

    @Override
    public int compareTo(Player o) {
        if (lvl > o.getLvl()) {
            return -1;
        } else if (lvl < o.getLvl()){
            return 1;
        }
        if (friendshipPoints > o.getFriendshipPoints()) {
            return -1;
        } else if (friendshipPoints < o.getFriendshipPoints()){
            return 1;
        }
        return getName().compareToIgnoreCase(o.getName());
    }
}
