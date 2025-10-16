FILE_NAME = 'cities.txt'

def read_all_records():
    try:
        with open(FILE_NAME, 'r') as file:
            records = [line.strip() for line in file if line.strip()]
        return records
    except FileNotFoundError:
        return []
    except:
        return []

def write_all_records(records):
    try:
        with open(FILE_NAME, 'w') as file:
            for record in records:
                file.write(record + '\n')
    except:
        print("ERROR: Write Error")

# ------------ CRUD Operations ------------
def create_record(new_record):
    try:
        with open(FILE_NAME, 'a') as file:
            file.write(new_record + '\n')
    except:
        print("ERROR: Could not create record")

def display_records():
    records = read_all_records()
    if not records:
        print("\n--- No Record Found ---")
        return records
    print("\n--- Current Records ---")
    for index, record in enumerate(records, start=1):
        print(f"{index}. {record}")
    print("-----------------------")
    return records

def update_record(index, new_value):
    records = read_all_records()
    idx = index - 1
    if 0 <= idx < len(records):
        old_value = records[idx]
        records[idx] = new_value
        write_all_records(records)
        print(f"Record Updated: '{old_value}' → '{new_value}'")
    else:
        print("Error: Invalid record number")

def delete_record(index):
    records = read_all_records()
    idx = index - 1
    if 0 <= idx < len(records):
        deleted_record = records.pop(idx)
        write_all_records(records)
        print(f"Record Deleted: '{deleted_record}'")
    else:
        print("Error: Invalid record number")
# ------------ End CRUD ------------

def main():
    while True:
        print("\n======= File CRUD Menu =======")
        print("1. Create new record (Add New)")
        print("2. Read all records (View All)")
        print("3. Update record (Update Record)")
        print("4. Delete a record (Remove)")
        print("5. Exit")
        print("==============================")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("ERROR: Please enter a valid number")
            continue

        match choice:
            case 1:
                new_item = input("Enter city name: ").strip()
                if new_item:
                    create_record(new_item)
                else:
                    print("WARNING: Record cannot be empty")
            case 2:
                display_records()
            case 3:
                records = display_records()
                if records:
                    try:
                        record_num = int(input("Enter record number to update: "))
                        if 0 < record_num <= len(records):
                            new_item = input("Enter new city name: ").strip()
                            if new_item:
                                update_record(record_num, new_item)
                            else:
                                print("WARNING: New city name cannot be empty")
                        else:
                            print("ERROR: Record number out of range")
                    except ValueError:
                        print("ERROR: Invalid input. Please enter a number")
            case 4:
                records = display_records()
                if records:
                    try:
                        record_num = int(input("Enter record number to delete: "))
                        delete_record(record_num)
                    except ValueError:
                        print("ERROR: Invalid input. Please enter a number")
            case 5:
                print("Thank you, Goodbye!")
                break
            case _:
                print("ERROR: Invalid choice, retry")

if __name__ == '__main__':
    main()
