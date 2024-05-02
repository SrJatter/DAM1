package com.example.view;

import com.example.exceptions.CrossingException;
import com.example.model.character.Character;
import com.example.model.character.NPC;
import com.example.model.character.Player;
import com.example.model.enums.Color;
import com.example.model.enums.IType;
import com.example.model.enums.Place;
import com.example.model.enums.Studies;
import com.example.model.items.Flower;
import com.example.model.items.Furniture;
import com.example.model.items.Item;
import com.example.model.items.Tool;
import com.example.view.messages.Messages;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Options {
    private String[] command;
    private Utils u = new Utils();
    private Messages ms = new Messages();
    private ArrayList<Character> characters = new ArrayList<>();
    private ArrayList<Player> players;
    private ArrayList<NPC> npcs;
    private ArrayList<Item> items = new ArrayList<>();
    private String name;
    private Studies study;
    private  Place place;
    private IType type;
    public void registerPlayer() throws CrossingException {
        if (u.checkCommand(command, 2)) {
            name = u.capitalize(command[1]);
            if (!u.checkCharacterExist(characters, name)) {
                characters.add(new Player(name));
                System.out.println(ms.getMessage(Messages.PLAYER_REGISTERED));
            } else {
                throw new CrossingException(CrossingException.PLAYER_ALREADY_EXISTS);
            }
        }
    }
    public void registerNPC() throws CrossingException {
        if (u.checkCommand(command, 5)) {
            name = u.capitalize(command[1]);
            if (!u.checkCharacterExist(characters, name)) {
                study = Studies.getStudies(command[2]);
                place = Place.getPlace(command[3]);
                type = IType.getOType(command[4], true);
                characters.add(new NPC(name, study, place, type));
                System.out.println(ms.getMessage(Messages.NPC_REGISTERED));
            } else {
                throw new CrossingException(CrossingException.NPC_ALREADY_EXISTS);
            }
        }
    }

    public void createItem() throws CrossingException {
        if (u.checkCommandInRange(command, 5, 7)) {
            name = u.capitalize(command[1]);
            if (!u.checkItemExist(items, name)) {
                type = IType.getOType(command[2], false);
                study = Studies.getStudies(command[3]);
                int price = u.checkInteger(command[4]);
                u.checkNumInRange(price, 10, 200, false);
                if (type.equals(IType.MOBLE)) {
                    if (u.checkCommand(command, 5)) {
                        items.add(new Furniture(name, study, price));
                    }
                } else if (type.equals(IType.FLOR)) {
                    if (u.checkCommand(command, 6)) {
                        Color color = Color.getColor(command[5]);
                        items.add(new Flower(name, study, price, color));
                    }
                } else {
                    if (u.checkCommand(command, 7)) {
                        String desc = command[5];
                        int usages = u.checkInteger(command[6]);
                        u.checkNumInRange(usages, 1, 10, true);
                        items.add(new Tool(name, study, price, desc, usages));
                    }
                }
                System.out.println(ms.getMessage(Messages.ITEM_CREATED));
            } else {
                throw new CrossingException(CrossingException.ITEM_ALREADY_EXISTS);
            }
        }
    }

    public void infoPlayer() throws CrossingException {
        if (u.checkCommand(command, 2)) {
            name = u.capitalize(command[1]);
            players = u.getPlayers(characters);
            if (u.checkPlayerExist(players, name)) {
                Player player = u.searchPlayer(players, name);
                System.out.println("INFO JUGADOR");
                System.out.println(player);
                System.out.println("INVENTARI");
                for (Item item : player.getInventory()) {
                    System.out.println(item);
                }
                System.out.println("<< >>");
            } else {
                throw new CrossingException(CrossingException.PLAYER_NOT_FOUND);
            }
        }
    }

    public void buyItem() throws CrossingException {
        if (u.checkCommand(command, 3)) {
            name = u.capitalize(command[1]);
            players = u.getPlayers(characters);
            if (u.checkPlayerExist(players, name)) {
                String iName = u.capitalize(command[2]);
                Player player = u.searchPlayer(players, name);
                if (player.getLocation().equals(Place.BAR)) {
                    if (u.checkItemExist(items, iName)) {
                        Item item = u.searchItem(items, iName);
                        if (!player.getInventory().contains(item)) {
                            int amount = player.getCalacoins();
                            int price = item.getPrice();
                            if (amount >= price) {
                                player.buy(item);
                                System.out.println(ms.getMessage(Messages.SUCCESSFUL_PURCHASE, command));
                            } else {
                                throw new CrossingException(CrossingException.INSUFFICIENT_CALACOINS);
                            }
                        } else {
                            throw new CrossingException(CrossingException.PLAYER_ALREADY_HAS_ITEM);
                        }
                    } else {
                        throw new CrossingException(CrossingException.ITEM_NOT_FOUND);
                    }
                } else {
                    throw new CrossingException(CrossingException.PLAYER_NOT_AT_BAR);
                }
            } else {
                throw new CrossingException(CrossingException.PLAYER_NOT_FOUND);
            }
        }
    }

    public void move() throws CrossingException {
        if (u.checkCommand(command, 3)) {
            name = u.capitalize(command[1]);
            place = Place.getPlace(command[2]);
            if (u.checkCharacterExist(characters, name)) {
                Character character = u.searchCharacter(characters, name);
                character.setLocation(place);
                System.out.println(ms.getMessage(Messages.SUCCESSFUL_MOVE));
            } else {
                throw new CrossingException(CrossingException.NO_ONE_FOUND);
            }
        }
    }

    public void makeFriends() throws CrossingException {
        if (u.checkCommand(command, 4)) {
            name = u.capitalize(command[1]);
            players = u.getPlayers(characters);
            if (u.checkPlayerExist(players, name)) {
                String nName = u.capitalize(command[2]);
                npcs = u.getNPCs(characters);
                if (u.checkNPCExist(npcs, nName)) {
                    Player player = u.searchPlayer(players, name);
                    String iName = command[3];
                    Item item = u.searchItem(items, iName);
                    if (player.getInventory().contains(item)) {
                        NPC npc = u.searchNPC(npcs, nName);
                        if (player.getLocation().equals(npc.getLocation())) {
                            int points = u.winPoints(npc, item);
                            int prevLvl = player.getLvl();
                            player.riseFriendshipPoints(points);
                            String[] args = {name, String.valueOf(points), String.valueOf(player.getFriendshipPoints()), String.valueOf(player.getLvl()), String.valueOf(player.getCalacoins())};
                            if (player.getLvl() > prevLvl) {
                                System.out.println(ms.getMessage(Messages.RISE_FRIENDSHIP_POINTS_AND_LVL, args));
                            } else {
                                System.out.println(ms.getMessage(Messages.RISE_FRIENDSHIP_POINTS, args));
                            }
                        } else {
                            throw new CrossingException(CrossingException.PLAYER_AND_NPC_NOT_AT_SAME_PLACE);
                        }
                    } else {
                        throw new CrossingException(CrossingException.PLAYER_DOES_NOT_HAVE_ITEM);
                    }
                } else {
                    throw new CrossingException(CrossingException.NO_ONE_FOUND);
                }
            } else {
                throw new CrossingException(CrossingException.PLAYER_NOT_FOUND);
            }
        }
    }

    public void seeCharactersInPlace() throws CrossingException {
        if (u.checkCommand(command, 2)) {
            place = Place.getPlace(command[1]);
            if (u.charactersRegistered(characters)) {
                if (u.charactersInPlace(characters, place)) {
                    players = u.getPlayers(characters);
                    npcs = u.getNPCs(characters);
                    boolean someone = false;
                    System.out.println("JUGADORS");
                    for (Player player : players) {
                        if (player.getLocation().equals(place)) {
                            System.out.println(player);
                            someone = true;
                        }
                    }
                    if (!someone) {
                        System.out.println("No hi ha jugadors aquí");
                    }
                    someone = false;
                    System.out.println("<< >>");
                    System.out.println("PERSONAGES");
                    for (NPC npc : npcs) {
                        if (npc.getLocation().equals(place)) {
                            System.out.println(npc);
                            someone = true;
                        }
                    }
                    if (!someone) {
                        System.out.println("No hi ha personatges aquí");
                    }
                    System.out.println("<< >>");
                } else {
                    throw new CrossingException(CrossingException.NO_ONES_THERE);
                }
            } else {
                throw new CrossingException(CrossingException.NO_ONES_REGISTERED);
            }
        }
    }

    public void showAllData() throws CrossingException {
        if (u.checkCommand(command, 1)) {
            players = u.getPlayers(characters);
            npcs = u.getNPCs(characters);
            if (!(players.isEmpty() && npcs.isEmpty() && items.isEmpty())) {
                System.out.println("JUGADORS");
                for (Player player : players) {
                    System.out.println(player);
                }
                if (players.isEmpty()) {
                    System.out.println("No hi ha jugadors registrats");
                }
                System.out.println("<< >>");
                System.out.println("PERSONAGES");
                for (NPC npc : npcs) {
                    System.out.println(npc);
                }
                if (npcs.isEmpty()) {
                    System.out.println("No hi ha personatges registrats");
                }
                System.out.println("<< >>");
                System.out.println("ITEMS");
                for (Item item : items) {
                    System.out.println(item);
                }
                if (items.isEmpty()) {
                    System.out.println("No hi ha items creats");
                }
                System.out.println("<< >>");
            } else {
                System.out.println("No hi ha informació disponible");
            }
        }
    }

    public void ranking() throws CrossingException {
        if (u.checkCommand(command, 1)) {
            players = u.getPlayers(characters);
            Collections.sort(players);
            if (!players.isEmpty()) {
                System.out.println("RÀNQUING");
                String result = "";
                for (Player player: players) {
                    System.out.println(player);
                }
            } else {
                System.out.println("No hi ha jugadors registrats");
            }
        }
    }

    public void setCommand(String[] command) {
        this.command = command;
    }
}
