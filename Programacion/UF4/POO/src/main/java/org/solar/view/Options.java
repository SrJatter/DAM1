package org.solar.view;

import org.solar.model.Device;
import org.solar.model.House;
import org.solar.model.Panel;
import org.solar.persistence.SaveData;
import java.util.ArrayList;

public class Options {
    private ArrayList<House> houses;
    private House house;
    private Device device;
    private String[] command;
    private Utilities util = new Utilities();
    private SaveData sd = new SaveData();
    private String nif;
    private String name;
    private int power;
    private int suf;

    public Options() {
        houses = sd.readHouses();
    }
    public void addCasa(){
        if (util.checkCommand(command, 4, "Uso: addCasa [nif] [nom] [superfície]")) {
            nif = command[1];
            if (!House.nifExists(nif)) {
                if (util.checkInt(command[3],"Error: La superficie ha de ser un numero entero." , "Error: La superficie ha de ser mayor a 10.", 10) != null) {
                    name = command[2];
                    suf = Integer.parseInt(command[3]);
                    house = new House(nif, name, suf);
                    houses.add(house);
                    sd.writeHouse(house);
                    System.out.println("OK: Casa registrada.");
                }
            } else {
                System.out.println("Error: Ya hay una casa con el este nif.");
            }
        }
    }
    public void addPlaca(){
        if (util.checkCommand(command, 5, "Uso: addPlaca [nif] [superfície] [preu] [potencia]")) {
            if (util.checkHouseNotVoid(houses)) {
                nif = command[1];
                if (House.nifExists(nif)) {
                    house = util.searchHouseByNif(houses, nif);
                    if (!util.isHouseSurfaceFull(house)) {
                        if (util.checkInt(command[2], "Error: La superficie ha de ser un numero entero.", "Error: La superficie ha de ser mayor a 0.", 0) != null) {
                            if (util.checkFloat(command[3], "Error: El precio ha de ser un numero entero o decimal.", "Error: El precio ha de ser mayor a 0.", 0) != null) {
                                if (util.checkInt(command[4], "Error: La potencia ha de ser un numero entero.", "Error: La superficie ha de ser mayor a 0.", 0) != null) {
                                    suf = Integer.parseInt(command[2]);
                                    if (util.checkTotalPanelSurface(house, suf)) {
                                        float price = Float.parseFloat(command[3]);
                                        power = Integer.parseInt(command[4]);
                                        house.addPanel(new Panel(suf, price, power));
                                        sd.overrideHouse(houses);
                                        System.out.println("OK: Placa agregada correctamente.");
                                    } else {
                                        System.out.println("Error: No hay espacio disponìble para instalar la placa.");
                                    }
                                }
                            }
                        }
                    }
                } else {
                    System.out.println("Error: No hay ninguna casa registrada con este nif.");
                }
            } else {
                System.out.println("No hay casas registradas.");
            }
        }

    }
    public void addAparell(){
        if (util.checkCommand(command, 4, "Uso: addAparell [nif] [nom] [potencia]")) {
            if (util.checkHouseNotVoid(houses)) {
                nif = command[1];
                if (House.nifExists(nif)) {
                    if (util.checkInt(command[3], "Error: La potencia ha de ser un numero entero.", "Error: La potencia ha de ser mayor a 0.", 0) != null) {
                        name = command[2];
                        house = util.searchHouseByNif(houses, nif);
                        if (!house.deviceNameExists(name)) {
                            power = Integer.parseInt(command[3]);
                            house.addDevice(new Device(name, power));
                            sd.overrideHouse(houses);
                            System.out.println("OK: Dispositivo agregado correctamente.");
                        } else {
                            System.out.println("Error: Ya existe un dispositivo con este nombre en la casa indicada.");
                        }
                    }
                } else {
                    System.out.println("Error: No hay ninguna casa registrada con este nif.");
                }
            } else {
                System.out.println("No hay casas registradas.");
            }
        }
    }
    public void onCasa(){
        if (util.checkCommand(command, 2, "Uso: onCasa [nif]")) {
            if (util.checkHouseNotVoid(houses)) {
                nif = command[1];
                if (House.nifExists(nif)) {
                    house = util.searchHouseByNif(houses, nif);
                    if (!house.isCommute()) {
                        house.setCommute(true);
                        sd.overrideHouse(houses);
                        System.out.println("OK: Interruptor general encendido.");
                    } else {
                        System.out.println("Error: La casa ya tiene el interruptor encendido.");
                    }
                } else {
                    System.out.println("Error: No hay ninguna casa registrada con este nif.");
                }
            } else {
                System.out.println("No hay casas registradas.");
            }
        }
    }
    public void onAparell(){
        if (util.checkCommand(command, 3, "Uso: offAparell [nif] [nom]")) {
            if (util.checkHouseNotVoid(houses)) {
                nif = command[1];
                if (House.nifExists(nif)) {
                    name = command[2];
                    house = util.searchHouseByNif(houses, nif);
                    if (house.deviceNameExists(name)){
                        if (house.isCommute()) {
                            device = util.searchDeviceByName(house, name);
                            if (!device.isCommute()) {
                                device.setCommute(true);
                                if (!util.overPowered(house)) {
                                    sd.overrideHouse(houses);
                                    System.out.println("OK: Dispositivo encendido.");
                                }
                            } else {
                                System.out.println("Error: El dispositivo ya estaba encendido.");
                            }
                        } else {
                            System.out.println("Error: No se puede encender el dispositivo. El interruptor general está apagado.");
                        }
                    } else {
                        System.out.println("Error: No hay ningun dispositivo con ese nombre en la casa indicada.");
                    }
                } else {
                    System.out.println("Error: No hay ninguna casa registrada con este nif.");
                }
            } else {
                System.out.println("No hay casas registradas.");
            }
        }
    }
    public void offAparell(){
        if (util.checkCommand(command, 3, "Uso: offAparell [nif] [nom]")) {
            if (util.checkHouseNotVoid(houses)) {
                nif = command[1];
                if (House.nifExists(nif)) {
                    name = command[2];
                    house = util.searchHouseByNif(houses, nif);
                    if (house.deviceNameExists(name)){
                        device = util.searchDeviceByName(house, name);
                        if (device.isCommute()) {
                            device.setCommute(false);
                            sd.overrideHouse(houses);
                            System.out.println("OK: Dispositivo apagado.");
                        } else {
                            System.out.println("Error: El dispositivo ya estaba apagado.");
                        }
                    } else {
                        System.out.println("Error: No hay ningun dispositivo con ese nombre en la casa indicada.");
                    }
                } else {
                    System.out.println("Error: No hay ninguna casa registrada con este nif.");
                }
            } else {
                System.out.println("No hay casas registradas.");
            }
        }
    }
    public void list(){
        if (util.checkCommand(command, 1, "Uso: list")) {
            if (util.checkHouseNotVoid(houses)) {
                System.out.println("--- Endolls Solars, S.L. ---");
                System.out.println("Casas registradas: " + houses.size());
                int numHouse = 1;
                for (House house : houses) {
                    System.out.println();
                    System.out.println("Casa " + numHouse);
                    System.out.println("Client: " + house.getNif() + " - " + house.getName());
                    System.out.println("Superficie tejado: " + house.getSurface());
                    System.out.println("Superficie disponible: " + util.avalibleHouseSurface(house));
                    System.out.println("Interruptor general: " + util.commutedHouse(house));
                    int panelsI = house.getPanels().size();
                    if (panelsI > 0) {
                        System.out.println("Placas solares instaladas: " + panelsI);
                    } else {
                        System.out.println("No tiene placas solares instaladas.");
                    }
                    int devicesR = house.getDevices().size();
                    if (devicesR > 0) {
                        System.out.println("Dispositivos registrados: " + devicesR);
                    } else {
                        System.out.println("No tiene ningun dispositivo eléctrico registrado.");
                    }
                    numHouse += 1;
                }
            } else {
                System.out.println("No hay casas registradas.");
            }
        }
    }
    public void info(){
        if (util.checkCommand(command, 2, "Uso: info [nif]")) {
            nif = command[1];
            if (House.nifExists(nif)) {
                house = util.searchHouseByNif(houses, nif);
                System.out.println("Client: " + house.getNif() + " - " + house.getName());
                System.out.println("Placas solares instaladas: " + house.getPanels().size());
                System.out.println("Potencia total: " + util.totalPower(house) + "W");
                System.out.println("Inversion total: " + util.totalInversion(house) + "€");
                System.out.println("Dispositivos registrados: " + house.getDevices().size());
                int consumo = util.actualConsum(house);
                System.out.println("Consumo actual: " + consumo + "W");
                if (consumo > 0) {
                    util.showDevicesName(house);
                }
            } else {
                System.out.println("Error: No hay ninguna casa registrada con este nif.");
            }
        }
    }
    public String quit() {
        if (util.checkCommand(command, 1)) {
            return "quit";
        } else {
            return "";
        }
    }
    public void setCommand(String[] command) {
        this.command = command;
    }
}
