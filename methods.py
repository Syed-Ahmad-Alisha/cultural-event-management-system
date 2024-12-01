class EventManager:
    def __init__(self, event_date):
        self.events = {}
        self.event_date = event_date

    def view_events(self, status_filter=None):
        filtered_events = {k: v for k, v in self.events.items() if v['status'] == status_filter} if status_filter else self.events
        if not filtered_events:
            print(f"No {status_filter or ''} events to show.")
        else:
            print("\n--- List of Events ---")
            for event_id, details in filtered_events.items():
                print(f"ID: {event_id} | Name: {details['name']} | Time: {details['time']} | Status: {details['status']}")

    def update_status(self, event_id, status):
        if event_id in self.events:
            if status == "completed" or status == "not completed":
                self.events[event_id]['status'] = status
                print(f"Event ID {event_id} status updated to {status}.")
            else:
                print("Invalid status. Use 'completed' or 'not completed'.")
        else:
            print("Event not found.")

    def delete_event(self, event_id):
        if event_id in self.events:
            if self.events[event_id]['status'] == "upcoming":
                del self.events[event_id]
                print(f"Event ID {event_id} deleted.")
            else:
                print("Cannot delete a completed event.")
        else:
            print("Event not found.")

    def add_event(self, name, time):
        event_id = str(len(self.events) + 1)
        self.events[event_id] = {
            "name": name,
            "time": time,
            "date": self.event_date,
            "status": "upcoming"  # Automatically categorized as 'upcoming'
        }
        print(f"Event '{name}' added with ID: {event_id}. Status: Upcoming")

