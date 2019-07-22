# coding: windows-1252
import platform

# Retorna o sistema operacional
print(platform.system())

# Retorna a arquitetura do SO
print(platform.machine())

# Retorna a versão do python em que o sistema está rodando
print(platform.python_version())

# Retorna o nome de rede do computador
print(platform.node())

# Identifica o compilador do python
print(platform.python_compiler())

# Retorna a release do SO 
print(platform.release())