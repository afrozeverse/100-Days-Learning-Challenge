FILE_NAME="cities.txt"

def read_all_records():
    try:
        with open(FILE_NAME,'r') as file:
            records=[line.strip() for line in file if line.strip()]
        return records
    except:
        return []

def write_all_records(records):
    try:
        with open(FILE_NAME,'w') as file:
            for record in records:
                file.write(record+'\n')
    except:
        print("ERROR: Write error!")

"""CRUD Operations"""
def create_record(new_record):
    try:
        with open(FILE_NAME,'a') as file:
            if new_record:
                file.write(new_record+'\n')
    except:
        print("ERROR: Couldn't create a new recorrd.")

def display_records():
    records=read_all_records()
    try:
        with open(FILE_NAME,'r') as file:
            if not records:
                print("\n--- Records not found ---")
                return records
            print("\n----- Current Records -----")
            for index, record in enumerate(records):
                print(index+1," ",record)
            print("-------------------------------")
            return records
    except:
        print("File opening error")
def update_record(index,new_item):
    records=read_all_records()
    idx=index-1
    if 0>=idx<len(records):
        records[idx]=new_item
        write_all_records(records)
        print("Record updated successfully")
    else:
        print("Error: Invalid record number.")
        
def delete_record(index):
    records=read_all_records()
    idx=index-1
    if 0 <= idx < len(records):
        records.pop(idx)
        write_all_records(records)
        print("Record deleted successfully")
    else:
        print("ERROR: delete error.")


def main():
    while True:
        print("\n======File CRUD menu====")
        print("1. Create new record (Add new)")
        print("2. Read all records (View all)")
        print("3. Update record (Update record)")
        print("4. Delete a record (Remove)")
        print("5. Exit")
        print("============================")
        choice=int(input("Enter your choice(1-5) "))
        match choice:
            case 1:
                new_item = input("Enter city name: ")
                if new_item:
                    create_record(new_item)
                else:
                    print("WARNING: Record cannot be empty!")
            case 2:
                display_records()
            case 3:
                records=display_records()
                if records:
                    try:
                        record_num=int(input("Enter record number to update: "))
                        new_item=input("Enter new city name: ")
                        if(new_item):
                            update_record(record_num,new_item)
                        else:
                            print("WARNING: Record cannot be empty!")
                    except ValueError:
                        print("Invalid operation")
            case 4:
                records=display_records()
                if records:
                    try:
                        record_num=int(input("Enter record number: "))
                        if record_num:
                            delete_record(record_num)
                    except ValueError:
                        print("Invalid operation!")
            case 5:
                print("Thank you, Goodbye!")
                break #this will break the loop, not the match case, match case doesnt need break keyword
            case _:
                print("Invalid entry retry!")
if __name__ == '__main__':
    main()
