import matplotlib.pyplot as plt

def park(data):
    review_park = input("Which park would you like to see the reviews for?\n").capitalize()
    reviews = [row[1] for row in data if review_park in row[4]]
    for review in reviews:
        print(f"The review for {review_park} is: {review}")
    else:
        print(f"No reviews found for {review_park}.")
        
def specific_park(data):
    review_park = input("Which park would you like to see the reviews for?\n").capitalize()
    location_reviews = input("From which location? \n").capitalize()
    num_review = sum(1 for row in data if review_park in row[4] and location_reviews in row[3])
    print(f"The number of reviews from {location_reviews} for {review_park} is: {num_review}")

def average(data):
    review_park = input("Which park would you like to see the reviews for?\n").capitalize()
    year = input("Which year? \n")
    total_rating = sum(int(row[1]) for row in data if review_park in row[4] and year in row[2])
    count = sum(1 for row in data if review_park in row[4] and year in row[2])
    
    if count > 0:
        average_rating = total_rating / count
        print(f"The average rating for {review_park} in {year} is: {average_rating:.2f}")
    else:
        print(f"No reviews found for {review_park} in {year}")

def avg_score_per_park_by_location(data):
    parks = {}
    for row in data:
        park = row[4]
        location = row[3]
        rating = int(row[1])
        if park not in parks:
            parks[park] = {}
        if location not in parks[park]:
            parks[park][location] = []
        parks[park][location].append(rating)
    
        avg_scores_by_location = {park: {location: sum(ratings) / len(ratings) for location, ratings in locations.items()} for park, locations in parks.items()}
    
    for park, locations in avg_scores_by_location.items():
        plt.figure()
        plt.bar(locations.keys(), locations.values())
        plt.title(f'Average Score per Park by Reviewer Location - {park}')
        plt.xlabel('Location')
        plt.ylabel('Average Rating')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

def pie_chart_reviews_per_park(data):
    park_counts = {}
    for row in data:
        park = row[4]
        if park not in park_counts:
            park_counts[park] = 0
        park_counts[park] += 1
    
    plt.figure()
    plt.pie(park_counts.values(), labels=park_counts.keys(), autopct='%1.1f%%')
    plt.title('Number of Reviews per Park')
    plt.show()


def bar_chart_avg_scores_per_park(data):
    park_ratings = {}
    for row in data:
        park = row[4]
        rating = int(row[1])
        if park not in park_ratings:
            park_ratings[park] = []
        park_ratings[park].append(rating)
    
    avg_scores = {park: sum(ratings) / len(ratings) for park, ratings in park_ratings.items()}
    
    plt.figure()
    plt.bar(avg_scores.keys(), avg_scores.values())
    plt.title('Average Review Scores per Park')
    plt.xlabel('Park')
    plt.ylabel('Average Score')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def top_locations(data):
    review_park = input("Enter the park name: ").capitalize()
    location_ratings = {}
    for row in data:
        park = row[4]
        if park == review_park:
            location = row[3]
            rating = int(row[1])
            if location not in location_ratings:
                location_ratings[location] = []
            location_ratings[location].append(rating)
    
    avg_scores = {location: sum(ratings) / len(ratings) for location, ratings in location_ratings.items()}
    top_locations = dict(sorted(avg_scores.items(), key=lambda item: item[1], reverse=True)[:10])
    
    plt.figure()
    plt.bar(top_locations.keys(), top_locations.values())
    plt.title(f'Top 10 Locations by Average Rating for {review_park}')
    plt.xlabel('Location')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def avg_rating_per_month(data):
    review_park = input("Enter the park name: ").capitalize()
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_ratings = {month: [] for month in month_names}
    
    for row in data:
        park = row[4]
        if park == review_park:
            year_month = row[2]
            rating = int(row[1])
            month = month_names[int(year_month.split('-')[1]) - 1]
            month_ratings[month].append(rating)
    
    avg_monthly_ratings = {month: sum(ratings) / len(ratings) if ratings else 0 for month, ratings in month_ratings.items()}
    
    plt.figure()
    plt.bar(avg_monthly_ratings.keys(), avg_monthly_ratings.values())
    plt.title(f'Average Monthly Rating for {review_park}')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()