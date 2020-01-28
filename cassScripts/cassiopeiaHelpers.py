from cassiopeia.datastores.riotapi.common import APIError
import time

def auto_retry(api_call_method):
    """ A decorator to automatically retry 500/503s (Service Unavailable) and skip 400s (Bad Request) or 404 (Not Found). """

    def call_wrapper(*args, **kwargs):
        try:
            return api_call_method(*args, **kwargs)
        except APIError as error:
            # try again once
            if error.error_code in [500, 503]:
                try:
                    print("Got a 500 or 503, trying again after 5 seconds...")
                    time.sleep(5)
                    return api_call_method(*args, **kwargs)
                except APIError as another_error:
                    if another_error.error_code in [500, 503, 400, 404]:
                        pass
                    else:
                        raise another_error

            # skip
            elif error.error_code in [400, 404]:
                print("Got a 400 or 404")
                pass  # may make match None in auto_retry(riotapi.get_match)!

            # fatal
            else:
                raise error

    return call_wrapper
