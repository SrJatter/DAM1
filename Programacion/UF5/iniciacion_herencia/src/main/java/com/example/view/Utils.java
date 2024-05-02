package com.example.view;

import com.example.exceptions.CrossingException;
import com.example.model.character.Character;
import com.example.model.character.NPC;
import com.example.model.character.Player;
import com.example.model.enums.Place;
import com.example.model.items.Item;

import java.util.ArrayList;
import java.util.Comparator;

public class Utils {
    public boolean charactersRegistered(ArrayList<Character> characters) {
        return !characters.isEmpty();
    }

    public boolean charactersInPlace(ArrayList<Character> characters, Place place) {
        for (Character character : characters) {
            if (character.getLocation().equals(place)) {
                return true;
            }
        }
        return false;
    }

    public int winPoints(NPC npc, Item item) {
        int points = 2;
        if (npc.getPreference().equals(item.getType())) {
            points += 5;
        }
        if (npc.getStudy().equals(item.getStudy())) {
            points += 4;
        }
        return points;
    }
    public Item searchItem(ArrayList<Item> items, String name) {
        for (Item item : items) {
            if (item.getName().equals(name)) {
                return item;
            }
        }
        return null;
    }
    public Character searchCharacter(ArrayList<Character> characters, String name) {
        for (Character character : characters) {
            if (character.getName().equals(name)) {
                return character;
            }
        }
        return null;
    }
    public NPC searchNPC(ArrayList<NPC> npcs, String name) {
        for (NPC npc : npcs) {
            if (npc.getName().equals(name)) {
                return npc;
            }
        }
        return null;
    }
    public Player searchPlayer(ArrayList<Player> players, String name) {
        for (Player player : players) {
            if (player.getName().equals(name)) {
                return player;
            }
        }
        return null;
    }
    public void checkNumInRange(int num, int min, int max, boolean switchErr) throws CrossingException {
        if (num < min || num > max) {
            if (switchErr) {
                throw new CrossingException(CrossingException.USAGE_OUT_OF_RANGE);
            } else {
                throw new CrossingException(CrossingException.PRICE_OUT_OF_RANGE);
            }
        }
    }
    public int checkInteger(String num) throws CrossingException {
        try {
            return Integer.parseInt(num);
        } catch (NumberFormatException e) {
            throw new CrossingException(CrossingException.WRONG_DATA);
        }
    }
    public boolean checkItemExist(ArrayList<Item> items, String name) {
        for (Item item : items) {
            if (item.getName().equals(name)) {
                return true;
            }
        }
        return false;
    }
    public boolean checkCharacterExist(ArrayList<Character> characters, String name) {
        for (Character character : characters) {
            if (character.getName().equals(name)) {
                return true;
            }
        }
        return false;
    }
    public ArrayList<NPC> getNPCs(ArrayList<Character> characters) {
        ArrayList<NPC> npcs = new ArrayList<>();
        for (Character character : characters) {
            if (character instanceof NPC) {
                 npcs.add((NPC) character);
            }
        }
        return npcs;
    }
    public boolean checkNPCExist(ArrayList<NPC> npcs, String name) {
        for (NPC npc : npcs) {
            if (npc.getName().equals(name)) {
                return true;
            }
        }
        return false;
    }
//    public ArrayList<Player> getSortedPlayers(ArrayList<Player> players) {
//        players.sort(Comparator
//                .comparingInt(Player::getLvl)
//                .thenComparingInt(Player::getFriendshipPoints)
//                .thenComparing(Player::getName));
//        return players;
//    }
    public ArrayList<Player> getPlayers(ArrayList<Character> characters) {
        ArrayList<Player> players = new ArrayList<>();
        for (Character character : characters) {
            if (character instanceof Player) {
                players.add((Player) character);
            }
        }
        return players;
    }
    public boolean checkPlayerExist(ArrayList<Player> players, String name) {
        for (Player player : players) {
            if (player.getName().equals(name)) {
                return true;
            }
        }
        return false;
    }
    public String capitalize(String str) {
        return str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase();
    }

    public boolean checkCommand(String[] co, int num) throws CrossingException {
        if (co.length != num) {
            throw new CrossingException(CrossingException.WRONG_ARGUMENTS);
        }
        return true;
    }
    public boolean checkCommandInRange(String[] co, int min, int max) throws CrossingException {
        if (co.length < min || co.length > max) {
            throw new CrossingException(CrossingException.WRONG_ARGUMENTS);
        }
        return true;
    }


}
