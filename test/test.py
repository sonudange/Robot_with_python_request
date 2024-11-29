from deepdiff import DeepDiff
import requests
#from Robot_with_python_request.utils.Fileutil import load_expected_result
from utils.Fileutil import load_expected_result

def verify_the_actual_and_expected_response_for_country(countryName) :
    print(countryName)
    response = requests.get(f"https://restcountries.com/v3.1/name/{countryName}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()

    print("Original Json")
    print(response_json)
    print("--------------Expected Json-----------------------")
    expected_data = load_expected_result("fixture/expected_result/expected.json")
    print(expected_data)
    diff = DeepDiff(response_json, expected_data)
    print("----------Printing Differance--------------")
    print(diff)

