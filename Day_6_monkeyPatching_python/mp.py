import time

# External library code
class ExternalServices:
    def fetch_data(self):
        print("Fetching data...")
        time.sleep(5)
        return "Real data form the server"
    
api_services = ExternalServices()
# End of external library code


def run_original_call():
    start_time=time.time()
    result=api_services.fetch_data()
    end_time = time.time()
    print("Result: ",result)
    print("Time taken: {} sec".format(end_time-start_time))

def mock_fetch_data():
    print("Bypassing the real fetch_data function..")
    return "Mock data for testing"

# here we patching the data means replacing the original "fetch_data" with the "mock_fetch_data"
def run_pached_call():
    api_services.fetch_data=mock_fetch_data
    start_time=time.time()
    result=api_services.fetch_data()
    end_time = time.time()
    print("Result: ",result)
    print("Time taken: {} sec".format(end_time-start_time))

if __name__ == "__main__":
    run_pached_call()

