import tui
import csv
import visual

def read_data(file_path):
    data = []

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            data.append(row)
    print("Dataset has been read.\n")
    print(f"Number of rows in Dataset: {len(data)}\n")
    return data

def process_submenu_a(data):
    while True:
        submenu_choice = tui.submenu_a()
        if submenu_choice == 'A':
            visual.park(data)
        elif submenu_choice == 'B':
            visual.specific_park(data)
        elif submenu_choice == 'C':
            visual.average(data)
        elif submenu_choice == 'D':
            visual.avg_score_per_park_by_location(data)
        else:
            break

def process_submenu_b(data):
    while True:
        submenu_choice = tui.submenu_b()
        if submenu_choice == 'A':
            visual.pie_chart_reviews_per_park(data)
        elif submenu_choice == 'B':
            visual.bar_chart_avg_scores_per_park(data)
        elif submenu_choice == 'C':
            visual.top_locations(data)
        elif submenu_choice == 'D':
            visual.avg_rating_per_month(data)
        else:
            break
