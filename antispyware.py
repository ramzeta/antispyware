import os
import subprocess

# Define una lista de archivos sospechosos o conocidos de spyware
spyware_files = [
    "C:\Windows\System32\drivers\etc\hosts", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\etc\networks", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\etc\services", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\etc\protocols", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\etc\netstat.bat", # si se ha creado recientemente
    "C:\Program Files (x86)\Common Files\System\ado\msado15.dll", # si se ha creado recientemente
    "C:\Program Files (x86)\Common Files\System\ado\msado10.dll", # si se ha creado recientemente
    "C:\Windows\System32\drivers\atapi.sys", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\iastor.sys", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\intelide.sys", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\msahci.sys", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\pciide.sys", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\volsnap.sys", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\wd.sys", # si se ha modificado para redirigir sitios web
    "C:\Windows\System32\drivers\etc\netstat.bat", # si se ha creado recientemente
    "C:\Windows\System32\drivers\etc\curl.exe", # si se ha creado recientemente
    "C:\Windows\System32\drivers\etc\wget.exe", # si se ha creado recientemente
    "C:\Windows\System32\drivers\etc\nc.exe", # si se ha creado recientemente
    "C:\Windows\System32\drivers\etc\netcat.exe", # si se ha creado recientemente
    "C:\Windows\System32\drivers\etc\putty.exe" # si se ha creado recientemente
]

# Define una lista de procesos sospechosos o conocidos de spyware
spyware_processes =  [
    "bpk.exe",
    "conime.exe",
    "conhost.exe",
    "csrss.exe",
    "dssagent.exe",
    "explorer.exe", # si se ejecuta desde una ubicación no estándar
    "lsass.exe", # si se ejecuta desde una ubicación no estándar
    "msiexec.exe", # si se ejecuta desde una ubicación no estándar
    "rundll32.exe", # si se ejecuta desde una ubicación no estándar
    "services.exe", # si se ejecuta desde una ubicación no estándar
    "smss.exe",
    "spoolsv.exe", # si se ejecuta desde una ubicación no estándar
    "svchost.exe", # si se ejecuta desde una ubicación no estándar
    "taskhostw.exe",
    "taskmgr.exe", # si se ejecuta desde una ubicación no estándar
    "winlogon.exe", # si se ejecuta desde una ubicación no estándar
    "wmiprvse.exe",
    "wscript.exe" # si se ejecuta desde una ubicación no estándar
]

# Define una lista de rutas de registro sospechosas o conocidas de spyware
spyware_registry_paths = [    
    "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run",
    "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows"
]

# Define una función para buscar archivos sospechosos
def search_spyware_files():
    try:
        for root, files in os.walk("C:\\"):
            for file in files:
                if file in spyware_files:
                    print("Se encontró un archivo de spyware: " + os.path.join(root, file))
    except  Exception as e:
        print(f"Ocurrió un error al : {e}")

# Define una función para buscar procesos sospechosos
def search_spyware_processes():
    try:
        bytes_data = subprocess.check_output(["tasklist"])
        decoded_data = bytes_data.decode("utf-8", errors="replace")
        print(decoded_data)
        for process in spyware_processes:
            if process in decoded_data:
                print("Se encontró un proceso de spyware: " + process)
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error al ejecutar el comando: {e}")

# Define una función para buscar rutas de registro sospechosas
def search_spyware_registry_paths():
    for path in spyware_registry_paths:
        try:
            output = subprocess.check_output(["reg", "query", path]).decode("utf-8")
        except subprocess.CalledProcessError as e:
            print(f"Ocurrió un error al ejecutar el comando: {e}")
            if output:
                print("Se encontró una ruta de registro de spyware: " + path)

# Ejecuta las funciones de detección de spyware
search_spyware_files()
search_spyware_processes()
search_spyware_registry_paths()
