import capsolver
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set your API key here
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_linkedin():
    logging.info("Attempting to solve LinkedIn CAPTCHA")
    try:
        solution = capsolver.solve({
            "type": "FunCaptchaTaskProxyLess",
            "websiteURL": "",
            "websitePublicKey": "",
            "funcaptchaApiJSSubdomain": "",
            "data": "{\"blob\":\"Put the dynamic value obtained per session here.\"}"
        })
        logging.info("CAPTCHA solved successfully")
        return solution
    except Exception as e:
        logging.error("Failed to solve CAPTCHA: %s", e)
        return None

def main():
    logging.info("Solving LinkedIn CAPTCHA")
    solution = solve_funcaptcha_linkedin()
    if solution is not None and "token" in solution:
        token = solution["token"]
        logging.info("Token Solution: %s", token)
    else:
        logging.error("Failed to obtain a valid token")

if __name__ == "__main__":
    main()
