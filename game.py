import requests, json
import sys

def checkin(host, email):

    data = {
        "email": email,
        "code": ""
    }
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json; charset=UTF-8',
        'Referer': host+"/",
    }
    response = requests.post(host+'/portal/api/checkIn', headers=headers, data=json.dumps(data), verify=False)
    if response.status_code == 200:
        print("Execute successfully.")
    else:
        print("Failed")

    return 1

if __name__ == "__main__":
    checkin(sys.argv[1], sys.argv[2])