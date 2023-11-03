from project.computer_store_app import ComputerStoreApp

if __name__ == '__main__':
    cs = ComputerStoreApp()
    print(cs.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
    print(cs.sell_computer(10000, "Apple M1 Pro", 32))
    print()