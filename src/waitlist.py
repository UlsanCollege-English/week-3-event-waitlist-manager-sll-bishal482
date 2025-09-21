class Waitlist:
    def __init__(self):
        """Initializes a new, empty waitlist."""
        self.queue = []

    def __len__(self):
        """Returns the number of people on the waitlist."""
        return len(self.queue)

    def join(self, name):
        """Adds a name to the end of the waitlist."""
        self.queue.append(name)

    def to_list(self):
        """Returns the waitlist as a Python list."""
        return self.queue

    def find(self, name):
        """Returns True if a name is on the waitlist, False otherwise."""
        return name in self.queue

    def cancel(self, name):
        """
        Removes a name from the waitlist.
        Returns True if the name was found and removed, False otherwise.
        """
        if name in self.queue:
            self.queue.remove(name)
            return True
        return False

    def bump(self, name):
        """
        Moves a name to the front of the waitlist.
        Returns True if the name was found and moved, False otherwise.
        """
        if name in self.queue:
            self.queue.remove(name)
            self.queue.insert(0, name)
            return True
        return False