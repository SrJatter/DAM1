package col.hotel.view;

import col.hotel.exceptions.HotelException;

public class Menu {
    InputData input = new InputData();
    Options op = new Options();

    public void menu() {
        String option;
        do {
            System.out.print("> ");
            String[] command = input.askStr().trim().split(" ");
            op.setCommand(command);
            option = command[0].toLowerCase();
            try {
                switch (option) {
                    case "room":

                    case "exit":
                        System.out.println("Saliendo...");
                        break;
                    default:
                        throw new HotelException(HotelException.WRONG_OPERATION);
                }
            } catch (HotelException e) {
                System.out.println(e.getMessage());
            }
        } while (!option.equals("exit"));
    }
}
