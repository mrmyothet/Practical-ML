import psutil
import platform
import subprocess
import tensorflow as tf


def get_system_specs():
    """Gathers and prints information about the system's hardware."""
    print("=" * 40)
    print("SYSTEM & HARDWARE INFORMATION")
    print("=" * 40)

    # OS Info
    print(f"OS: {platform.system()} {platform.release()}")

    # CPU Info
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")

    # RAM Info
    ram_gb = psutil.virtual_memory().total / (1024**3)
    print(f"Total RAM: {ram_gb:.2f} GB")


def get_system_specs_details():
    """Gathers and prints information about the system's hardware."""
    print("=" * 40)
    print("SYSTEM & HARDWARE INFORMATION")
    print("=" * 40)

    # OS Info
    print(f"OS: {platform.system()} {platform.release()}")

    # CPU Info
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")

    # RAM Info
    ram_gb = psutil.virtual_memory().total / (1024**3)
    print(f"Total RAM: {ram_gb:.2f} GB")

    # GPU Info
    gpus = tf.config.list_physical_devices("GPU")
    if gpus:
        print(f"Detected {len(gpus)} GPU(s):")
        for i, gpu in enumerate(gpus):
            # Using nvidia-smi to get more detailed info as tf.config is limited
            try:
                # The command is split for better readability
                cmd = [
                    "nvidia-smi",
                    "--query-gpu=name,memory.total,driver_version",
                    "--format=csv,noheader,nounits",
                ]
                result = (
                    subprocess.check_output(cmd, encoding="utf-8")
                    .strip()
                    .split("\n")[i]
                )
                name, mem_total, driver = result.split(", ")

                print(
                    f"  - GPU {i}: {name}, VRAM: {float(mem_total)/1024:.2f} GB, Driver: {driver}"
                )
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(
                    f"  - GPU {i}: (nvidia-smi not found or failed, using TensorFlow info)"
                )
                details = tf.config.experimental.get_device_details(gpu)
                print(f"    Name: {details.get('device_name', 'N/A')}")

    else:
        print("No GPU detected by TensorFlow. Training will be on CPU.")
    print("=" * 40, "\n")


# get_system_specs()
get_system_specs_details()


# Note: GPU support on native-Windows is only available for 2.10 or earlier versions,
# starting in TF 2.11, CUDA build is not supported for Windows.
# For using TensorFlow GPU on Windows, you will need to build/install TensorFlow in WSL2
# or use tensorflow-cpu with TensorFlow-DirectML-Plugin
