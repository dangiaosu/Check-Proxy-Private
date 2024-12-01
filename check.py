import aiohttp
import asyncio
import pandas as pd
from aiohttp import BasicAuth
from colorama import init, Fore, Style

# Khởi tạo colorama
init(autoreset=True)

# Token ipinfo.io
IPINFO_TOKEN = "YOUR_ACCESS_TOKEN"

# Tiêu đề và mô tả chương trình
def print_header():
    print(f"{Fore.BLUE}Code Python check proxy private by Đan Giáo Sư vs ChatGPT")
    print(f"{Fore.RED}Chuyên lùa gà, nhưng vẫn ghét fake news")
    print(f"{Fore.CYAN}Thông tin liên hệ:")
    print(f"{Fore.BLUE}Telegram: https://t.me/dangiaosu/")
    print(f"{Fore.MAGENTA}Facebook: https://fb.com/prof.danta/")
    print(f"{Fore.GREEN}Zalo: https://zalo.me/0828092390/\n")

# Hàm đọc proxy từ file proxy.txt
def read_proxies_from_file(filename):
    proxy_list = []
    with open(filename, 'r') as file:
        for line in file:
            proxy_info = line.strip().split(':')
            if len(proxy_info) == 4:
                proxy_url = f"{proxy_info[0]}:{proxy_info[1]}"
                username = proxy_info[2]
                password = proxy_info[3]
                proxy_list.append({
                    'proxy_url': proxy_url,
                    'username': username,
                    'password': password
                })
    print(f"{Fore.GREEN}[INFO] Đọc thành công {len(proxy_list)} proxy từ file {filename}")
    return proxy_list

# Hàm kiểm tra IP public của proxy
async def get_public_ip(proxy, semaphore):
    proxy_url = f"http://{proxy['proxy_url']}"
    async with semaphore:
        try:
            timeout = aiohttp.ClientTimeout(total=5)
            auth = BasicAuth(proxy['username'], proxy['password'])
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get('http://api64.ipify.org?format=json', proxy=proxy_url, proxy_auth=auth) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"{Fore.GREEN}[INFO] Lấy thành công IP public: {data['ip']} từ proxy: {proxy['proxy_url']}")
                        return data['ip']
                    else:
                        print(f"{Fore.RED}[ERROR] Không thể lấy IP public từ proxy: {proxy['proxy_url']} (Status: {response.status})")
        except asyncio.TimeoutError:
            print(f"{Fore.YELLOW}[WARNING] Proxy timeout: {proxy['proxy_url']}")
        except aiohttp.ClientError as e:
            print(f"{Fore.RED}[ERROR] Lỗi kết nối cho proxy {proxy['proxy_url']}: {e}")
    return "die"

# Hàm lấy thông tin từ ipinfo.io
async def get_ip_info(ip, session):
    api_url = f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}"
    try:
        async with session.get(api_url) as response:
            if response.status == 200:
                return await response.json()
    except aiohttp.ClientError as e:
        print(f"{Fore.RED}[ERROR] Lỗi khi kết nối tới ipinfo.io: {e}")
    return None

# Kiểm tra proxy
async def process_proxy(proxy, seen_ips, semaphore, session):
    public_ip = await get_public_ip(proxy, semaphore)
    if public_ip == "die":
        return {"Proxy": proxy['proxy_url'], "Status": "die"}
    if public_ip in seen_ips:
        return {"Proxy": proxy['proxy_url'], "IP": public_ip, "Status": "duplicate"}
    seen_ips.add(public_ip)
    ip_info = await get_ip_info(public_ip, session)
    return {"Proxy": proxy['proxy_url'], "IP": public_ip, "Status": "active", **(ip_info or {})}

async def check_proxies(proxy_list):
    semaphore = asyncio.Semaphore(50)
    seen_ips = set()
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [process_proxy(proxy, seen_ips, semaphore, session) for proxy in proxy_list]
        for task in asyncio.as_completed(tasks):
            results.append(await task)
    return results

def export_to_excel(results):
    df = pd.DataFrame(results)
    df.to_excel('proxy_check_results.xlsx', index=False)
    print(f"{Fore.GREEN}[INFO] Kết quả đã được lưu vào proxy_check_results.xlsx")

async def main():
    print_header()
    input(f"{Fore.YELLOW}Nhấn Enter để bắt đầu kiểm tra proxy...")
    proxy_list = read_proxies_from_file('proxy.txt')
    results = await check_proxies(proxy_list)
    export_to_excel(results)

if __name__ == "__main__":
    asyncio.run(main())
