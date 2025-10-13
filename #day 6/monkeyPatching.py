import time

""" External Library Code"""
class ExternalService:
    def fetch_data(self):
        print("Starting slow network call")
        time.sleep(5)
        return "Real Data from server"

api_service = ExternalService()

""" End of External Library"""

def run_original_call():
    # calling of monkey patching
    api.service.fetch_data=mock_fetch_data
    start_time = time.time()
    result = api_service.fetch_data()
    end_time = time.time()
    print("Result:" , result)
    print("Time taken: {}".format(end_time-start_time))

# monkey patching
def mock_fetch_data():
    print("Mock - Bypass network call")
    return "Mocked Test Data"

def run_patched_call():
    # monkey patching
    api_service.fetch_data= mock_fetch_data

    start_time = time.time()
    result = api_service.fetch_data()
    end_time = time.time()
    print("Result:",result)
    print("Time Taken:{}".format(end_time-start_time))

if __name__=="__main__":
    # run_original_call()
    run_patched_call()