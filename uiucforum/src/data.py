import csv

csv_file = r'C:\Users\Mirza\Downloads\course-catalog.csv'
def extract(csv_file):
    subject_number_set = set()

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)


        for row in reader:
            subject_number_set.add((row['Subject'], row['Number'], row['Name']))

    return subject_number_set

unique = extract(csv_file)
uniquesort = sorted(unique)

print(uniquesort)

def convert_set_to_csv(grok_set, output_file):
    fieldnames = ['Class', 'Number', 'Name']
    
    # Open CSV file for writing
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(fieldnames)
        
        # Write set elements into CSV file, filling missing columns with empty strings
        for row in grok_set:
            writer.writerow(row[:3])  # Take first three elements of each set row


output_csv_file = 'class_data.csv'
convert_set_to_csv(uniquesort, output_csv_file)