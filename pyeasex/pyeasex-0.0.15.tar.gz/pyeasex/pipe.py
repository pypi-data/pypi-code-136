import os 

def suppress():
    null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
    save = os.dup(1), os.dup(2)
    os.dup2(null_fds[0], 1)
    os.dup2(null_fds[1], 2)
    return null_fds, save

def resume(null_fds, save):
	os.dup2(save[0], 1)
	os.dup2(save[1], 2)
	os.close(null_fds[0])
	os.close(null_fds[1])	    