import functions_framework

@functions_framework.cloud_event
def firestore_trigger(cloud_event):
    # Print event details
    print(f"Event ID: {cloud_event['id']}")
    print(f"Event Type: {cloud_event['type']}")
    print(f"Event Data: {cloud_event['data']}")

    return 'Event received', 200
