import psutil
import platform


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


get_system_specs()
