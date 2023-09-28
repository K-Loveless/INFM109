def main():
    product_data = None

    while True:
        print("\nMain Menu:")
        print("1. Load Product Data from a CSV File.")
        print("2. Analyze Product Data.")
        print("3. Exit.")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename of the CSV file: ")
            product_data = load_product_data(filename)
            if product_data:
                print("Data loaded successfully.")
            else:
                print("Failed to load data.Check file or data form.")

        elif choice == "2":
            if product_data:
                analysis_result = analyze_product_data(product_data)
                print("\nAnalysis Results:")
                print(analysis_result)
            else:
                print("No data loaded.Load data before analyzing.")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Select a valid option.")

if __name__ == "__main__":
    main()
