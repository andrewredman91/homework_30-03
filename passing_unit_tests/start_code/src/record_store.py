def get_name(record_store):
    return record_store["name"]

def find_record_by_title(record_name,record_store_dict):
    list_of_records = record_store_dict["records"]
    for record in record_store_dict["records"]:
        if record["title"] == record_name:
            return record

def sell_record(record,record_store):
    record_store["money"] += record["price"]
    record_store["records"].remove(record)