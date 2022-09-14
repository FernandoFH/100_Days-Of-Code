from random import randint
from node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(3, 6)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def paly(self):
        print(f"Count of tracks: {self.count}")

        while self.count > 0 and self.head is not None:
            current_track = self.dequeue()
            print(f"Playing: {current_track.title} ({current_track.length} seconds)")
            sleep(current_track.length)