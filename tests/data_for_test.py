tree = {
    "doc1": {
        "key1": "value1",
        "key2": {
            "key3": "value3"
        },
        "key6": {
            "key8": "value8"
        },
        "key7": {
            "key10": "value10"
        }
    },
    "doc2": {
        "key1": "value1",
        "key2": {
            "key3": "value3",
            "key4": "value4"
        },
        "key7": {
            "key11": "value11"
        }
    }
}

expected_result = {
    "key1": "value1",
    "key2": {
        "key3": "value3",
        "key4": "value4"
    },
    "key6": {
        "key8": "value8"
    },
    "key7": {
        "key10": "value10",
        "key11": "value11"
    }
}

error_data = {
    "doc1": {
        "key1": "value1",
        "key2": {
            "key3": "value3"
        },
        "key7": {
            "key11": "value11"
        }
    }
}