from time import perf_counter
class Stopwatch:

    """ Initializes stopwatch objects that that programmers
    can use to time the execution time of portions of
    a program. """
    def __init__(self):
        """ Makes a new stopwatch ready for timing. """
        self.reset()

    def start(self):
        """ Starts the stopwatch, unless it is already running.
        This method does not affect any time that may have
        already accumulated on the timer. """
        if not self._running:
            self._start_time = perf_counter() - self._elapsed
            self._running = True # Clock now running

    def stop(self):
        """ Stops the stopwatch, unless it is not running.
        Updates the accumulated elapsed time. """
        if self._running:
            self._elapsed = perf_counter() - self._start_time
            self._running = False # Clock stopped

    def reset(self):
        """ Resets stopwatch to zero. """
        self._start_time = self._elapsed = 0
        self._running = False

    def elapsed(self):
        """ Reveals the stopwatch running time since it was last reset. """
        if not self._running:
            return self._elapsed
        else:
            return perf_counter() - self._start_time