# Modulos importantes
import subprocess
import os
import dotenv

# Carregando variaveis de ambiente
dotenv.load_dotenv()

# Configurando variaveis de ambiente
MITMPROXY_HOST=os.getenv('MITMPROXY_HOST')
MITMPROXY_MIN_PORT=int(os.getenv('MITMPROXY_MIN_PORT'))
MITPROXY_MAX_PORT=int(os.getenv('MITPROXY_MAX_PORT'))

# Configurando as informações
MITMPROXY_PORTAS = [porta for porta in range(MITMPROXY_MIN_PORT, MITPROXY_MAX_PORT)]

# Caminho do projeto
ROOT = os.path.dirname(os.path.abspath(__file__))

# Ler proxies txt
PROXIES: list[str]
with open(os.path.join(ROOT, 'proxies.txt'), 'r') as proxies:
    PROXIES = [proxie.strip('\n') for proxie in proxies.readlines()]

# Verificando a quantidade de proxies
assert len(PROXIES) == len(MITMPROXY_PORTAS)



# Iniciar o mitmproxie
for proxie, porta in zip(PROXIES, MITMPROXY_PORTAS):
    auth, proxie = proxie.replace('http://', '').split('@')
    print(auth, proxie)
    print(porta)
    subprocess.Popen(['mitmdump', '-p', str(porta), '--mode', f'upstream:http://{proxie}', '--upstream-auth', auth])

    


