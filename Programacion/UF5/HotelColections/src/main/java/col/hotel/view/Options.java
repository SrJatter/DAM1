package col.hotel.view;

import col.hotel.controller.Hotel;
import col.hotel.view.messages.Message;

public class Options {
    private String[] command;
    private Hotel m = Hotel.getInstance();
    private Message ms = new Message();

    public void addRoom() {

    }

    public void setCommand(String[] command) {
        this.command = command;
    }
}
