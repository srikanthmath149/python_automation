import requests
import json
import logging

def hit_endpoint(url):
    valid_links = []
    if url and url.lower() != "null":
        try:
            data = requests.get(url)
            dump = data.json()
            print("Total entries:", dump.get("count", 0))
            
            for link in dump.get("entries", []):
                url_to_check = link['Link'].replace("http://", "https://")
                print("Checking:", url_to_check)
                try:
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/115.0 Safari/537.36"
                    }
                    data2 = requests.get(url_to_check, headers=headers, timeout=10)
                    if data2.status_code == 200:
                        valid_links.append(url_to_check)
                        print("✅ Working:", url_to_check)
                    else:
                        print(f"❌ Status {data2.status_code} for {url_to_check}")
                except requests.exceptions.RequestException as e:
                    logging.error(f"Request failed for {url_to_check}: {e}")
        except json.JSONDecodeError:
            logging.error("Invalid JSON returned from URL.")
        except requests.RequestException as e:
            logging.error(f"Main URL request failed: {e}")
    else:
        print("Error: URL is null or empty.")

# Use raw JSON link
hit_endpoint("https://raw.githubusercontent.com/srikanthmath149/python_automation/main/entries.json")
