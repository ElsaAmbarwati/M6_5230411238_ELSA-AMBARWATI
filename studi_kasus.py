class Order:
    def __init__(self, ID, name, details):
        self.ID = ID
        self.name = name
        self.details = details

    def displayOrder(self):
        print(f"Order ID: {self.ID}, Name: {self.name}, Details: {self.details}")


class Delivery:
    def __init__(self, id, name, information, date, address):
        self.id = id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def displayDelivery(self):
        print(f"Delivery ID: {self.id}, Name: {self.name}, Information: {self.information}, Date: {self.date}, Address: {self.address}")


daftar_Order = [
    Order("1", "jimin", "es"),
    Order("2", "Olivia Rodrigo", "seblak"),
    Order("3", "khensin", "nasg0r"),
    Order("4", "sunjae", "pop es"),
    Order("5", "esa", "es teh"),
]

daftar_deliveries = [
    Delivery("11", "jia", "es", "12-12-2024", "Jl.Raya"),
    Delivery("22", "Oli Rodrigo", "seblak", "11-11-2024", "Jl.rr"),
    Delivery("33", "esin", "nasg0r", "13-12-2024", "Jl.ww"),
    Delivery("44", "sun", "pop es", "14-12-2024", "Jl.dd"),
    Delivery("55", "lala", "es teh", "15-12-2024", "Jl.qq"),
]


def delete_order():
    order_id = input("Masukkan ID Pesanan yang ingin dihapus: ")
    for order in daftar_Order:
        if order.ID == order_id:
            daftar_Order.remove(order)
            print(f"Order dengan ID {order_id} berhasil dihapus.")
            return
    print(f"Order dengan ID {order_id} tidak ditemukan.")


def delete_delivery():
    delivery_id = input("Masukkan ID Pengiriman yang ingin dihapus: ")
    for delivery in daftar_deliveries:
        if delivery.id == delivery_id:
            daftar_deliveries.remove(delivery)
            print(f"Delivery dengan ID {delivery_id} berhasil dihapus.")
            return
    print(f"Delivery dengan ID {delivery_id} tidak ditemukan.")


def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Tambah Order Baru")
        print("2. Display Semua Orders")
        print("3. Delete Order")
        print("4. Tambah Delivery Baru")
        print("5. Display Semua Deliveries")
        print("6. Delete Delivery")
        print("0. Keluar")
        choice = input("Masukkan pilihan : ")

        if choice == '1':
            ID = input("Masukkan ID Pesanan: ")
            name = input("Masukkan Nama Pemesan: ")
            details = input("Masukkan Detail Pesanan: ")
            order = Order(ID, name, details)
            daftar_Order.append(order)
            print("Order berhasil ditambahkan!")

        elif choice == '2':
            print("\nDaftar Order:")
            if daftar_Order:
                for order in daftar_Order:
                    order.displayOrder()
            else:
                print("Tidak ada pesanan.")

        elif choice == '3':
            delete_order()

        elif choice == '4':
            id = input("Masukkan ID Pengiriman: ")
            name = input("Masukkan Nama Pengirim: ")
            information = input("Masukkan Informasi Pengiriman: ")
            date = input("Masukkan Tanggal Pengiriman: ")
            address = input("Masukkan Alamat Pengiriman: ")
            delivery = Delivery(id, name, information, date, address)
            daftar_deliveries.append(delivery)
            print("Delivery berhasil ditambahkan!")

        elif choice == '5':
            print("\nDaftar Delivery:")
            if daftar_deliveries:
                for delivery in daftar_deliveries:
                    delivery.displayDelivery()
            else:
                print("Tidak ada delivery.")

        elif choice == '6':
            delete_delivery()

        elif choice == '0':
            print("Keluar dari program. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


main_menu()