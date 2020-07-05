import json
person = {}
person["Name"] = "Hari Bahadur"
person["Age"] = 31
print("The person dictionary is:", person)
json_string = json.dumps(person)
print("The given dictionary as JSON string is:", json_string)
deserialized_person = json.loads(json_string)
print("The deserialized person dictionary from JSON string:", deserialized_person)