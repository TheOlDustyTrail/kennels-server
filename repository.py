import resource


DATABASE = {
    "animals":
    [{
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
        {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
        {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }],
    "customers": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        }
    ],
    "employees": [
        {
            "id": 1,
            "name": "Jenna Solis"
        }
    ],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]
}


def expand(key, data):
    resource = key[:-2]+"s"
    matching_data = retrieve(resource, data[key])
    new_key = key[:-2]
    data[new_key] = matching_data
    del data[key]


def all(resource):
    return DATABASE[resource]


def retrieve(resource, id):
    requested_data = None

    for data in DATABASE[resource]:
        if data["id"] == id:
            requested_data = data

            if resource == "animals":
                foreign_keys = ["locationId", "customerId"]

                for key in foreign_keys:
                    expand(key, requested_data)

    return requested_data


def create(resource, data):
    max_id = DATABASE[resource][-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    data["id"] = new_id

    # Add the animal dictionary to the list
    DATABASE[resource].append(data)

    # Return the dictionary with `id` property added
    return data


def update(id, new_data, resource):
    """For PUT requests to a single resource"""
    for index, data in enumerate(DATABASE[resource]):
        if data["id"] == id:
            # Found the animal. Update the value.
            DATABASE[resource][index] = new_data
            break


def delete(resource, id):
    data_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, data in enumerate(DATABASE[resource]):
        if data["id"] == id:
            # Found the animal. Store the current index.
            data_index = index

        # If the animal was found, use pop(int) to remove it from list
        if data_index >= 0:
            DATABASE[resource].pop(data_index)
