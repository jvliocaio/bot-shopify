import pexpect, subprocess, time

# Replace username and password with your ProtonVPN login credentials
username = "juliocaionouv@gmail.com"
password = "!1023440911.Jc"

try:
    # Spawn the protonvpn-cli login process
    protonvpn_login = pexpect.spawn("protonvpn-cli login " + username)

    # Expect the "Enter your ProtonVPN password:" prompt and send the password
    protonvpn_login.expect("Enter your Proton.*password:")
    protonvpn_login.sendline(password)

    retorno = protonvpn_login.expect([pexpect.EOF, "You are already logged in.", "Successful login."])

    if retorno == 1 or retorno == 2:
        print("Protonvpn-cli logged")
    # Wait for the process to complete
    protonvpn_login.wait()


except Exception as e:
    print(e)

subprocess.run('protonvpn-cli disconnect', shell=True, capture_output=True, text=True)
print("Disconnected from ProtonVPN.")

time.sleep(5)

subprocess.run('protonvpn-cli connect --fastest', shell=True, capture_output=True, text=True)
print("Connected in to ProtonVPN.")
