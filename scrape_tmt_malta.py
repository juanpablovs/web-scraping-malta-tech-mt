from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()
company_names = []
telephones = []
emails = []
sectors = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


for i in range(1,50,1):
    url = f"https://tech.mt/members-directory/?pg={i}"
    print(url)
    r = session.get(url, headers=headers)
    r.html.render(sleep=5, keep_page=True, scrolldown=1)

    comps = r.html.find(".tmt-member-title")
    tels = r.html.find(".tmt-member-phone")
    ems = r.html.find(".tmt-member-email")
    sct = r.html.find(".tmt-member-sectors")

    for num in range(0,len(comps)):
        company_names.append(comps[num].text.strip() if comps[num].text else None)
        telephones.append(tels[num].text.removeprefix('Phone:').strip() if tels[num].text else None)
        emails.append(ems[num].text.removeprefix('Email:').strip() if ems[num].text else None)
        sectors.append(sct[num].text.strip() if sct[num].text else None)


data = {
            "Company Name": company_names,
            "Telephone": telephones,
            "Email": emails,
            "Sectors": sectors
        }


df = pd.DataFrame(data)

output_file = "tmt_company_details.xlsx"
df.to_excel(output_file, index=False)

print(f"Company details saved to {output_file} successfully.")
