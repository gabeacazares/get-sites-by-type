import argparse
import csv
import logging
import sys

def main():
    
    ## Argument parsing
    parser = argparse.ArgumentParser(description="Program to parse WTC site CSVs, filter, and return names of site names.")
    parser.add_argument('-p', '--path', action='store', dest='csv_path', default='./whc-sites.csv', help='Path to the WTC CSV file')
    parser.add_argument('-c', '--filtering-column',action='store', dest='filtering_column', default='category', help='Column to filter by')
    parser.add_argument('-v', '--filtering-column-value',action='store', dest='filtering_column_value', default='Music', help='Value to filter by')
    parser.add_argument('-o', '--out-column',action='store', dest='filtered_landmarks_columns_to_print', default='name_en', help='Column to print')
    args = parser.parse_args()
    csv_path = args.csv_path
    filtering_column = args.filtering_column
    filtering_column_value = args.filtering_column_value
    filtered_landmarks_columns_to_print = args.filtered_landmarks_columns_to_print

    landmarks_data,landmarks_header = csv_loader(csv_path)
    filtering_column_number = get_column_by_name(landmarks_header, filtering_column)
    filtered_rows = get_row_by_filtered_column(landmarks_data,filtering_column_number,filtering_column_value)
    filtered_columns_to_print = get_column_by_name(landmarks_header, filtered_landmarks_columns_to_print)
    print_filtered_landmark_names(filtered_rows,filtered_columns_to_print)

## Loads CSV file
def csv_loader(csv_path):
    csv_data = []
    try:
        with open(csv_path, mode='r',encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            for row in reader:
                csv_data.append(row)
    except FileNotFoundError as file_not_found_error:
        logging.exception(file_not_found_error)
        sys.exit(1)
    return csv_data,header

## Retrieves column number by name
def get_column_by_name(landmarks_header, filtering_column):
    column_index = []
    landmarks_header_list = list(landmarks_header)
    for item in landmarks_header_list:
        if item.lower() == filtering_column.lower():
            column_index.append(landmarks_header_list.index(item))
    if len(column_index) <= 0:
        logging.exception("Column not found")
        sys.exit(1)
    if len(column_index) > 1:
        logging.exception("Multiple columns found")
        sys.exit(1)
    else:
        return column_index[0]
## Filters row by value of column
def get_row_by_filtered_column(landmarks_data,filtering_column_number,filtering_column_value):
    filtered_data = []
    for row in landmarks_data:
        if row[filtering_column_number].lower() == filtering_column_value.lower():
            filtered_data.append(row)
    if filtered_data == []:
        logging.exception("No data found for filter: " + filtering_column_value)
        sys.exit(1)
    return filtered_data

## Prints out the filtered data
def print_filtered_landmark_names(filtered_rows,filtered_columns_to_print):
    for row in filtered_rows:
        print(row[filtered_columns_to_print])

if __name__ == "__main__":
    main()