import tui
import process
from exporter import DataExporter

def export_data(data):
    exporter = DataExporter(data)
    while True:
        export_choice = tui.export_menu()
        if export_choice == 'A':
            file_path = input("Enter the file path for the TXT export: ")
            exporter.export_to_txt(file_path)
            print(f"Data exported to {file_path}")
        elif export_choice == 'B':
            file_path = input("Enter the file path for the CSV export: ")
            exporter.export_to_csv(file_path)
            print(f"Data exported to {file_path}")
        elif export_choice == 'C':
            file_path = input("Enter the file path for the JSON export: ")
            exporter.export_to_json(file_path)
            print(f"Data exported to {file_path}")
        elif export_choice == 'D':
            return tui.menu()
        else:
            print("Invalid choice. Please try again.")

def run():
    print("-" * 26)
    print("Disneyland Review Analyzer")
    print("-" * 26)

    data = process.read_data("disneyland_reviews.csv")
    while True:
        selection = tui.menu()
        if selection == 'A':
            print("You have chosen option A - View Data\n")
            process.process_submenu_a(data)
        elif selection == 'B':
            print("You have chosen option B - Visualise Data\n")
            process.process_submenu_b(data)
        elif selection == 'C':
            print("You have chosen option C - Export data\n")
            export_data(data)
        elif selection == 'X':
            print("Have a great day!")
            break
        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    run()
