import os
from dotenv import load_dotenv

load_dotenv()


def my_shiny_wrapper(function_to_wrap):
    def the_wrapper():
        print("✨✨✨✨✨✨✨✨✨✨")
        function_to_wrap()
        print("✨✨✨✨✨✨✨✨✨✨")

    return the_wrapper


def test_method():
    ML_Summer_School_ID = os.getenv("ML_Summer_School_ID")
    print(f"Hello, {ML_Summer_School_ID} School")


test_method()
print("---------------------")

wraper_method = my_shiny_wrapper(test_method)
print("Check Type : ", type(wraper_method))
wraper_method()


print("---------------------")
my_shiny_wrapper(test_method)()
