package col.hotel.model;

import col.hotel.model.enums.RoomServices;
import col.hotel.model.enums.RoomStatus;

import java.util.HashSet;
import java.util.Set;

public class Room {
    private String code;
    private int capacity;
    private Set<RoomServices> services;
    private RoomStatus status;
    private Set<Worker> workers;
    private int customerDni;
    private int nrCustomers;

    public Room(String code, int capacity, Set<RoomServices> services) {
        this.code = code;
        this.capacity = capacity;
        this.services = new HashSet<>(services);
    }

    @Override
    public String toString() {
        return "capacity: " + capacity + " services:" + services + " status: " + status + " client: " + customerDni + "(" + nrCustomers + ")";
    }

    public void setStatus(RoomStatus status) {
        this.status = status;
    }

    public void setCustomer(int customerDni, int nrCustomers) {
        this.customerDni = customerDni;
        this.nrCustomers = nrCustomers;
    }

    public String getCode() {
        return code;
    }

    public int getCapacity() {
        return capacity;
    }

    public Set<RoomServices> getServices() {
        return services;
    }

    public RoomStatus getStatus() {
        return status;
    }

    public int getCustomerDni() {
        return customerDni;
    }

    public int getNrCustomers() {
        return nrCustomers;
    }
}
