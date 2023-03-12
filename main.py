import retrieveInfo as req
import interface

if __name__ == "__main__":
    url = "https://dstock.vndirect.com.vn/"
    
    print("Running...")
    print(req.getAPIreq(url,80).json())
