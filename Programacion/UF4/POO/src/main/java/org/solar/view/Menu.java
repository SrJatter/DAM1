package org.solar.view;

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
            switch (option) {
                case "addcasa":
                    op.addCasa();
                    break;
                case "addplaca":
                    op.addPlaca();
                    break;
                case "addaparell":
                    op.addAparell();
                    break;
                case "oncasa":
                    op.onCasa();
                    break;
                case "onaparell":
                    op.onAparell();
                    break;
                case "offaparell":
                    op.offAparell();
                    break;
                case "list":
                    op.list();
                    break;
                case "info":
                    op.info();
                    break;
                case "quit":
                    option = op.quit();
                    break;
                default:
                    System.out.println("ERROR: Comando incorrecto.");
            }
        } while (!option.equals("quit"));
    }
}
