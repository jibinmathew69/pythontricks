import threading

def task():
    print("Hello from : {}".format(threading.current_thread()))

task()

thread_task = threading.Thread(target=task)
thread_task.start()


# Output


# Hello from : <_MainThread(MainThread, started 140058010548032)>
# Hello from : <Thread(Thread-1, started 140057985287936)>