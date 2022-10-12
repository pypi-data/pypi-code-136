import os
import logging

logger = logging.getLogger()

try:
    from watchdog.events import PatternMatchingEventHandler

    class FrameFileEventHandler(PatternMatchingEventHandler):
        """docstring for ClassName"""

        def __init__(self, queue):
            super().__init__(patterns=["*.gwf", "*.hdf5", "*.h5"])
            self.queue = queue

        def on_created(self, event):

            if event.is_directory:
                return

            self.queue.put(event.src_path)

except ImportError:
    import threading
    import inotify.adapters

    # Thread to watch over watch_dir
    def monitor_dir_inotify(queue, watch_dir):

        # create a watcher thread only watching for in close write event
        i = inotify.adapters.Inotify()
        i.add_watch(watch_dir, inotify.constants.IN_CLOSE_WRITE)

        # Get the current thread
        t = threading.currentThread()

        # Check if this thread should stop
        while not t.stop:

            # Loop over the events and check when a file has been created
            for event in i.event_gen(yield_nones=False, timeout_s=1):

                # Check if the event was a close write
                (_, _, path, filename) = event

                # Add the filename to the queue
                queue.put(os.path.join(path, filename))

        # Remove the watch
        i.remove_watch(watch_dir)


def write_frame(file_name, frame_data, fl_ringn, file_name_dq):

    # write to disk
    with open(file_name, "wb") as fl_file:
        fl_file.write(frame_data)
        fl_file.close()

        #
        # ring of frame_log files?
        if fl_ringn:
            #
            # name queue full?
            if len(file_name_dq) == fl_ringn:
                old_file = file_name_dq.popleft()
                try:
                    os.unlink(old_file)
                except OSError:
                    logger.error(
                        f"Error: could not delete file [{old_file}]"
                    )

            #
            # add this file to queue
            file_name_dq.append(file_name)
