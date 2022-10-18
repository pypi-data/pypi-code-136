import subprocess

def is_nvidia_gpu_available():
   try:
      subprocess.check_output('nvidia-smi')
      return True
   except Exception:
      return False