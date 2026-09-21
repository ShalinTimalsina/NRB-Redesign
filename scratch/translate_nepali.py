import re
from pathlib import Path
from bs4 import BeautifulSoup

translations = {
    "आर्थिक वर्ष २०८३-८४ को मौद्रिक नीति": "Monetary Policy for Fiscal Year 2026/27",
    "गभर्नर पौडेल '49th SAARCFINANCE Governors' Group Meeting and Symposium' मा सहभागी": "Governor Poudel Participates in '49th SAARCFINANCE Governors' Group Meeting and Symposium'",
    "नवनियुक्त डेपुटी गभर्नर रावलद्वारा शपथ ग्रहण र पदबहाली": "Newly Appointed Deputy Governor Rawal Takes Oath and Assumes Office",
    "नेपाल इन्भेष्टमेण्ट मेगा बैंक लिमिटेडको सम्बन्धमा जारी गरिएको प्रेस विज्ञप्ति (२०८३-०४-२८)": "Press Release regarding Nepal Investment Mega Bank Limited (2026-08-12)",
    "नेपाल राष्ट्र बैंक , कर्मचारी सेवा विनियमावली, २०६८ ( चौथो संसोधन, २०८२ )": "Nepal Rastra Bank Employee Service Bylaws, 2011 (Fourth Amendment, 2025)",
    "नेपाल राष्ट्र बैंक ऐन, २०१२": "Nepal Rastra Bank Act, 1955",
    "नेपाल राष्ट्र बैंक ऐन, २०५८": "Nepal Rastra Bank Act, 2002",
    "नेपाल राष्ट्र बैंक गैर-बैंक वित्तीय संस्था निरीक्षण तथा सुपरिवेक्षण विनियमावली, २०८१": "NRB Non-Bank Financial Institution Inspection and Supervision Bylaws, 2024",
    "नेपाल राष्ट्र बैंक निरीक्षण तथा सुपरिवेक्षण विनियमावली, २०७४ (दोस्रो संशोधन २०८०)": "NRB Inspection and Supervision Bylaws, 2017 (Second Amendment 2023)",
    "नेपाल राष्ट्र बैंक निरीक्षण तथा सुपरिवेक्षण विनियमावली, २०७४ (प्रथम संशोधन २०७९)": "NRB Inspection and Supervision Bylaws, 2017 (First Amendment 2022)",
    "नेपाल राष्ट्र बैंक मनिचेन्जर इजाजतपत्र तथा निरीक्षण विनियमावली, २०७७ (तेस्रो संशोधनसहित)": "NRB Money Changer Licensing and Inspection Bylaws, 2020 (Including Third Amendment)",
    "नेपाल राष्ट्र बैंक विदेशी लगानी तथा विदेशी ऋण व्यवस्थापन विनियमावली, २०७८ (तेस्रो संशोधनसहित – मिति २०८०|१०|२६)": "NRB Foreign Investment and Foreign Debt Management Bylaws, 2021 (Including Third Amendment)",
    "नेपाल राष्ट्र बैंक विदेशी विनिमय कारोबार इजाजतपत्र तथा निरीक्षण विनियमावली, २०७७ (दोस्रो संशोधनसहित – मितिः २०८०/०८/२५)": "NRB Foreign Exchange Transaction Licensing and Inspection Bylaws, 2020 (Including Second Amendment)",
    "नेपाल राष्ट्र बैंक समाचार ७१ औं वार्षिकोत्सव विशेषाङ्क": "Nepal Rastra Bank News 71st Anniversary Special Edition",
    "नेपाली ढाँचा": "Nepali Format",
    "बैंक तथा वित्तीय संस्था एक आपसमा गाभ्ने / गाभिने (मर्जर) तथा प्राप्ति (एक्विजिशन) सम्बन्धी विनियमावली २०७३ (पाँचौं संशोधन, २०७९)": "Bank and Financial Institution Merger and Acquisition Bylaws 2016 (Fifth Amendment, 2022)",
    "बैंक तथा वित्तीय संस्था सम्बन्धी ऐन, २०७३": "Bank and Financial Institution Act, 2017",
    "बैंक तथा वित्तीय संस्थाको मुद्दती निक्षेपमा लगानी गर्ने सम्बन्धी सूचना": "Notice Regarding Investment in Fixed Deposits of Banks and Financial Institutions",
    "बैंकका पदाधिकारी र कर्मचारीद्वारा उद्धार कोषमा रकम जम्मा (२०८३-०५-२२)": "Funds Deposited in Rescue Fund by Bank Officials and Employees",
    "बैंकिङ्ग कसूर तथा सजाय ऐन, २०६४": "Banking Offence and Punishment Act, 2008",
    "भुक्तानी तथा फर्स्यौट ऐन, २०७५": "Payment and Settlement Act, 2018",
    "मौद्रिक नीति तर्जुमा कार्यविधि, २०७३ (दोस्रो संशोधन, २०८३)": "Monetary Policy Formulation Procedure, 2016 (Second Amendment, 2026)",
    "राजस्व तथा अन्य सरकारी रकम प्रणालीमा तत्काल प्रविष्टी सम्बन्धमा": "Regarding Immediate Entry of Revenue and Other Government Funds into the System",
    "वित्तीय ग्राहक सन्तुष्टि सर्वेक्षण २०८३": "Financial Customer Satisfaction Survey 2026",
    "विदेशी विनिमय (नियमित गर्ने) ऐन, २०१९": "Foreign Exchange (Regulation) Act, 1962",
    "विनिमेय अधिकारपत्र ऐन, २०३४": "Negotiable Instruments Act, 1977",
    "विपद्‍बाट प्रभावित क्षेत्रमा बैंकिङ सेवाको निरन्तरता सम्बन्धमा जारी गरिएको प्रेस विज्ञप्ति (२०८३-०५)": "Press Release on Continuity of Banking Services in Disaster Affected Areas",
    "विपद्‍बाट प्रभावित क्षेत्रमा बैंकिङ सेवाको निरन्तरता सम्बन्धमा जारी गरिएको प्रेस विज्ञप्ति (२०८३-०५-१३)": "Press Release on Continuity of Banking Services in Disaster Affected Areas (2026-08-29)",
    "सम्पत्ति शुद्धीकरण (मनी लाउन्डरिङ्ग) निवारण ऐन, २०६४": "Anti-Money Laundering Act, 2008",
    "सह–प्रवक्ता र सूचना अधिकारी तोकिएको सम्बन्धमा (२०८३/०२/१८)।": "Regarding the Appointment of Deputy Spokesperson and Information Officer",
    "सार्वजनिक खरिद ऐन, २०६३": "Public Procurement Act, 2007",
    "सूचनाको हक सम्बन्धी ऐन, २०६४": "Right to Information Act, 2007",
    "हेजिङ्ग नियमावली, २०७९": "Hedging Rules, 2022",
    "‘मिर्मिरे’ आर्थिक अङ्क : वर्ष – ५४ अङ्क – १ पूर्णाङ्क – ३६३": "'Mirmire' Economic Issue: Year - 54 Issue - 1 Whole Number - 363"
}

redundant_terms = [
    "प्रवक्ता", 
    "श्री गुरुप्रसाद पौडेल", 
    "सह प्रवक्ता तथा सूचना अधिकारी",
    "श्री सुधा श्रेष्ठ",
    "सहायक सूचना अधिकारी",
    "डा. संजय प्रसाद मिश्र"
]

redundant_replacements = {
    "Archives of investment related notices ((लगानी सम्बन्धि) सूचना) regarding fixed deposit investments in banks and financial institutions, published by Nepal Rastra Bank.": "Archives of investment related notices regarding fixed deposit investments in banks and financial institutions, published by Nepal Rastra Bank.",
    "Archives of investment related notices ((लगानी सम्बन्धि) सूचना) regarding fixed deposit investments in banks and financial institutions.": "Archives of investment related notices regarding fixed deposit investments in banks and financial institutions."
}

count = 0
for p in Path('.').rglob('*.html'):
    if 'scratch' in p.parts:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
        
    original_html = html
    
    # 1. Do direct replacements for the partial strings first
    for k, v in redundant_replacements.items():
        html = html.replace(k, v)
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 2. Decompose redundant nodes (like the nepali translations under english titles in info-officers)
    for tag in soup.find_all(string=True):
        if tag.parent.name not in ['script', 'style']:
            text = tag.strip()
            if text in redundant_terms:
                # Remove the parent p tag if it only contains this text
                if tag.parent.name == 'p' and tag.parent.text.strip() == text:
                    tag.parent.decompose()
                else:
                    tag.extract()
            elif text in translations:
                tag.replace_with(translations[text])
    
    new_html = str(soup)
    
    if original_html != new_html:
        # format output slightly better for decompose
        new_html = new_html.replace('</p>\n\n<h3', '</p>\n<h3')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_html)
        count += 1

print(f'Translated/cleaned Nepali text in {count} files.')
