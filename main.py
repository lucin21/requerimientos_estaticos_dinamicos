from trello import Trello
from qase import Qase
import time

tarjetas = []
trello = Trello()
qase = Qase()

trello.login_trello()
tarjetas = trello.extraer()

print(tarjetas[0])
print()
print(tarjetas[1])
print()
print(tarjetas[2])
print()

# with open("tarjeta.txt", "a") as file:
#     for tarjeta in tarjetas:
#         file.write(str(tarjeta))

# qase.login_qase()

# for tarjeta in tarjetas:
#     print(tarjeta[0][0])
#     print(tarjeta[0][1])
#     print(tarjeta[0][2])
    # qase.selector_suite_qase_3d(tarjeta[0][0], tarjeta[0][1], tarjeta[0][2])

time.sleep(10)










        # time.sleep(2)
        # driver.quit()


# ff = UsingWrappers1()
# ff.test()

