package org.solar.persistence;

import org.solar.model.Device;
import org.solar.model.House;
import org.solar.model.Panel;
import org.solar.view.Utilities;

import java.io.*;
import java.util.ArrayList;

public class SaveData {
    private String pathHouseFile;
    private File folderFile;
    private File houseFile;
    private static BufferedWriter bw;
    private static BufferedReader br;
    private Utilities util = new Utilities();

    public SaveData(){
        String folder = "data";
        String housesFileName = "houses.txt";
        pathHouseFile = folder + File.separator + housesFileName;
        folderFile = new File(folder);
        houseFile = new File(pathHouseFile);

    }
    private void fileCheck() {
        if(!folderFile.exists()){
            folderFile.mkdir();
        }
    }
    public void writeHouse(House house) {
        fileCheck();
        try {
            bw = new BufferedWriter(new FileWriter(pathHouseFile, true));
            bw.write("*");
            bw.newLine();
            String comm;
            bw.write(house.getNif() + "|" + house.getName() + "|" + house.getSurface() + "|" + util.commuteCheckHouse(house));
            bw.newLine();
            bw.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    public void overrideHouse(ArrayList<House> houses) {
        fileCheck();
        try {
            bw = new BufferedWriter(new FileWriter(pathHouseFile));
            for (House house : houses) {
                bw.write("*");
                bw.newLine();
                bw.write(house.getNif() + "|" + house.getName() + "|" + house.getSurface() + "|" + util.commuteCheckHouse(house));
                bw.newLine();
                bw.write("P");
                bw.newLine();
                for (Panel panel: house.getPanels()) {
                    bw.write(panel.getSurface() + "|" + panel.getPrice() + "|" + panel.getPower());
                    bw.newLine();
                }
                bw.write("D");
                bw.newLine();
                for (Device device : house.getDevices()) {
                    bw.write(device.getName() + "|" + device.getPower() + "|" + util.commuteCheckDevice(device));
                    bw.newLine();
                }
            }
            bw.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    public ArrayList<House> readHouses() {
        ArrayList<House> houses = new ArrayList<>();
        if (folderFile.exists() && houseFile.exists()) {
            try {
                br = new BufferedReader(new FileReader(houseFile));
                String line;
                boolean newContH = false;
                boolean newContP = false;
                boolean newContD = false;
                int inx = -1;
                while ((line = br.readLine()) != null) {
                    if (line.equals("*")) {
                        newContD = false;
                        newContH = true;
                        inx += 1;
                    } else if (line.equals("P")) {
                        newContP = true;
                    } else if (line.equals("D")) {
                        newContP = false;
                        newContD = true;
                    }else if (newContH) {
                        String[] data = line.split("\\|");
                        String nif = data[0];
                        String name = data[1];
                        int suf = Integer.parseInt(data[2]);
                        boolean commuted = util.checkCommuteInFile(data[3]);
                        houses.add(new House(nif, name, suf, commuted));
                        newContH = false;
                    } else if (newContP) {
                            String[] data = line.split("\\|");
                            int suf = Integer.parseInt(data[0]);
                            float price = Float.parseFloat(data[1]);
                            int power = Integer.parseInt(data[2]);
                            houses.get(inx).addPanel(new Panel(suf, price, power));
                    } else if (newContD) {
                        String[] data = line.split("\\|");
                        String name = data[0];
                        int power = Integer.parseInt(data[1]);
                        boolean commuted = util.checkCommuteInFile(data[2]);
                        houses.get(inx).addDevice(new Device(name, power, commuted));
                    }
                }
                br.close();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return houses;
    }
}

