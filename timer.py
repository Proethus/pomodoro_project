import datetime
import time


class Timer:
    def __init__(self):
        self.current_iteration = 0
        self.interval = 25
        self.general_break = 5
        self.cycle_end_break = 25
        self.time = datetime.timedelta(seconds=self.interval * 60)
        self.timer = "%02d:%02d" % divmod(self.time.seconds, 60)
        self.title = "Work"

    def start(self):
        while self.current_iteration < 4:
            self.iteration()

        self.time = datetime.timedelta(seconds=self.cycle_end_break * 60)
        self.update_title("Break")
        while self.time.total_seconds() > 0:
            time.sleep(1)
            self.time = datetime.timedelta(seconds=self.time.total_seconds() - 1)
            self.update_time()

    def iteration(self):
        self.update_title("Work")
        self.time = datetime.timedelta(seconds=self.interval * 60)
        while self.time.total_seconds() > 0:
            time.sleep(1)
            self.time = datetime.timedelta(seconds=self.time.total_seconds() - 1)
            self.update_time()

        self.update_title("Break")
        self.time = datetime.timedelta(seconds=self.general_break * 60)
        while self.time.total_seconds() > 0:
            self.time = datetime.timedelta(seconds=self.time.total_seconds() - 1)
            self.update_time()

    def update_time(self):
        self.timer = f"{time}"

    def update_title(self, title_arg):
        self.title = f"{title_arg}"
