import time

def predict_time_decorator(function_to_wrap):

    def wrapper():
        start_time = time.time()
        function_to_wrap()
        end_time = time.time()
        print(f"(This method took {end_time - start_time:.2f} seconds)")
    return wrapper

@predict_time_decorator
def predict_image():
    print("Image prediction method is running...")
    time.sleep(3)



@predict_time_decorator
def generate_text():
    print("Generate text method is running...")
    time.sleep(1)


predict_image()

generate_text()