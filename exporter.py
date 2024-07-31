import csv
import json

class DataExporter:
    def __init__(self, data):
        self.data = data
        self.aggregated_data = self.aggregate_data()

    def aggregate_data(self):
        park_data = {}
        for row in self.data:
            park = row[4]
            location = row[3]
            rating = int(row[1])
            if park not in park_data:
                park_data[park] = {
                    'num_reviews': 0,
                    'positive_reviews': 0,
                    'total_rating': 0,
                    'countries': set()
                }
            park_data[park]['num_reviews'] += 1
            if rating >= 4:  # Assuming 4 and 5 are positive ratings
                park_data[park]['positive_reviews'] += 1
            park_data[park]['total_rating'] += rating
            park_data[park]['countries'].add(location)
        
        for park in park_data:
            park_data[park]['avg_review_score'] = park_data[park]['total_rating'] / park_data[park]['num_reviews']
            park_data[park]['num_countries'] = len(park_data[park]['countries'])
        
        return park_data

    def export_to_txt(self, file_path):
        with open(file_path, 'w') as file:
            for park, data in self.aggregated_data.items():
                file.write(f"Park: {park}\n")
                file.write(f"Number of reviews: {data['num_reviews']}\n")
                file.write(f"Number of positive reviews: {data['positive_reviews']}\n")
                file.write(f"Average review score: {data['avg_review_score']:.2f}\n")
                file.write(f"Number of countries: {data['num_countries']}\n")
                file.write("\n")

    def export_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Park", "Number of Reviews", "Number of Positive Reviews", "Average Review Score", "Number of Countries"])
            for park, data in self.aggregated_data.items():
                writer.writerow([
                    park, 
                    data['num_reviews'], 
                    data['positive_reviews'], 
                    f"{data['avg_review_score']:.2f}", 
                    data['num_countries']
                ])

    def export_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.aggregated_data, file, indent=4, default=lambda x: list(x) if isinstance(x, set) else x)