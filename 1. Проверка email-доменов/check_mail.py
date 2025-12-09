import dns.resolver

emails = [
    "user1@gmail.com",
    "test@yahoo.com",
    "hello@outlook.com",
    "info@protonmail.com",
    "mail@icloud.com",
    "someone@nonexistentdomain12345.com",
    "person@thisdomaindoesnotexist987.net",
    "check@invalid-mail-test-000999.com",
    "admin@example.com",     
    "nobody@github.io",         
    "test@wikipedia.org",
    "adwd213"       
]

def check_mail(emails: list[str]) -> list[str]:
    results = []
    
    for email in emails:
      domain = get_domain(email)
      status = check_domain(domain)
      results.append(f"{email}: {status}")
    
    return results               
    
def check_domain(domain: str) -> str:
    try:
        dns.resolver.resolve(domain, 'MX')
        return "домен валиден"
    except dns.resolver.NXDOMAIN:
        return "домен отсутствует"
    except (dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return "MX-записи отсутствуют или некорректны"
    except Exception as e:
        return f"ошибка: {type(e).__name__}"
    

def get_domain(email: str) -> str:
    return email.split('@')[-1]


for line in check_mail(emails):
    print(line)


