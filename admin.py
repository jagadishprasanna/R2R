from r2r import R2RClient

client = R2RClient("https://sciphi-f5f0e37b-38ec-44c5-80cc-fdf5f490a45c-qwpin2swwa-ue.a.run.app")

# Login as admin
login_result = client.login("admin@example.com", "reProp123")
# logs = client.logs()

# change_password_result = client.change_password("change_me_immediately", "reProp123")
# print(change_password_result)

register_user = client.register("admin@reprop.com","reProp123")
print(register_user)