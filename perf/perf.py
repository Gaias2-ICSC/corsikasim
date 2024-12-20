import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def convert_to_seconds(time_str):
    minu, sec = time_str.split("m")
    s = sec[:-1]
    seconds = float(s)
    minutes = float(minu)
    return minutes * 60 + seconds

df = pd.read_csv('test_prod_logs.csv')
data = df.dropna()

data["real_time_seconds"] = data["real_time"].apply(convert_to_seconds)
data["user_time_seconds"] = data["user_time"].apply(convert_to_seconds)
data["sys_time_seconds"] = data["sys_time"].apply(convert_to_seconds)


dataproc09 = data[data.cpuname=="slurmstepd-dataproc09"]
dataproc10 = data[data.cpuname=="slurmstepd-dataproc10"]
dataproc11 = data[data.cpuname=="slurmstepd-dataproc11"]
dataproc12 = data[data.cpuname=="slurmstepd-dataproc12"]


Ngen_L = 1e4
Ngen_M = 1e3
Ngen_H = 1e2
Ngen_UH = 10

dataproc09L = dataproc09[dataproc09.minimal_energy == 1e3]
dataproc10L = dataproc10[dataproc10.minimal_energy == 1e3]
dataproc11L = dataproc11[dataproc11.minimal_energy == 1e3]
dataproc12L = dataproc12[dataproc12.minimal_energy == 1e3]

dataproc09M = dataproc09[dataproc09.minimal_energy == 1e5]
dataproc10M = dataproc10[dataproc10.minimal_energy == 1e5]
dataproc11M = dataproc11[dataproc11.minimal_energy == 1e5]
dataproc12M = dataproc12[dataproc12.minimal_energy == 1e5]

dataproc09H = dataproc09[dataproc09.minimal_energy == 1e7]
dataproc10H = dataproc10[dataproc10.minimal_energy == 1e7]
dataproc11H = dataproc11[dataproc11.minimal_energy == 1e7]
dataproc12H = dataproc12[dataproc12.minimal_energy == 1e7]

dataproc09UH = dataproc09[dataproc09.minimal_energy == 1e8]
dataproc10UH = dataproc10[dataproc10.minimal_energy == 1e8]
dataproc11UH = dataproc11[dataproc11.minimal_energy == 1e8]
dataproc12UH = dataproc12[dataproc12.minimal_energy == 1e8]


binst = np.logspace(-1 , 4.5)
binstsys = np.logspace(-5 , 2)


plt.hist(dataproc09[dataproc09.minimal_energy == 1e8].real_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e7].real_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e5].real_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e3].real_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("real time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc09")
plt.legend()
plt.savefig("plots/dataproc09_real.png")
plt.show()

plt.hist(dataproc10[dataproc10.minimal_energy == 1e8].real_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e7].real_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e5].real_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e3].real_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("real time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc10")
plt.legend()
plt.savefig("plots/dataproc10_real.png")
plt.show()


plt.hist(dataproc11[dataproc11.minimal_energy == 1e8].real_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e7].real_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e5].real_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e3].real_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("real time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc11")
plt.legend()
plt.savefig("plots/dataproc11_real.png")
plt.show()



plt.hist(dataproc12[dataproc12.minimal_energy == 1e8].real_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e7].real_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e5].real_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e3].real_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("real time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc12")
plt.legend()
plt.savefig("plots/dataproc12_real.png")
plt.show()



plt.hist(dataproc09[dataproc09.minimal_energy == 1e8].user_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e7].user_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e5].user_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e3].user_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("user time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc09")
plt.legend()
plt.savefig("plots/dataproc09_user.png")
plt.show()


plt.hist(dataproc10[dataproc10.minimal_energy == 1e8].user_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e7].user_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e5].user_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e3].user_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("user time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc10")
plt.legend()
plt.savefig("plots/dataproc10_user.png")
plt.show()


plt.hist(dataproc11[dataproc11.minimal_energy == 1e8].user_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e7].user_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e5].user_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e3].user_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("user time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc11")
plt.legend()
plt.savefig("plots/dataproc11_user.png")
plt.show()


plt.hist(dataproc12[dataproc12.minimal_energy == 1e8].user_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binst)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e7].user_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binst)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e5].user_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binst)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e3].user_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binst)
plt.xscale("log")
plt.xlabel("user time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc12")
plt.legend()
plt.savefig("plots/dataproc12_user.png")
plt.show()


plt.hist(dataproc09[dataproc09.minimal_energy == 1e8].sys_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binstsys)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e7].sys_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binstsys)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e5].sys_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binstsys)
plt.hist(dataproc09[dataproc09.minimal_energy == 1e3].sys_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binstsys)
plt.xscale("log")
plt.xlabel("sys time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc09")
plt.legend()
plt.savefig("plots/dataproc09_sys.png")
plt.show()



plt.hist(dataproc10[dataproc10.minimal_energy == 1e8].sys_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binstsys)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e7].sys_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binstsys)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e5].sys_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binstsys)
plt.hist(dataproc10[dataproc10.minimal_energy == 1e3].sys_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binstsys)
plt.xscale("log")
plt.xlabel("sys time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc10")
plt.legend()
plt.savefig("plots/dataproc10_sys.png")
plt.show()


plt.hist(dataproc11[dataproc11.minimal_energy == 1e8].sys_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binstsys)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e7].sys_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binstsys)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e5].sys_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binstsys)
plt.hist(dataproc11[dataproc11.minimal_energy == 1e3].sys_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binstsys)
plt.xscale("log")
plt.xlabel("sys time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc11")
plt.legend()
plt.savefig("plots/dataproc11_sys.png")
plt.show()


plt.hist(dataproc12[dataproc12.minimal_energy == 1e8].sys_time_seconds/Ngen_UH, alpha = 0.5, label = 'UH', bins = binstsys)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e7].sys_time_seconds/Ngen_H, alpha = 0.5, label = 'H', bins = binstsys)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e5].sys_time_seconds/Ngen_M, alpha = 0.5, label = 'M', bins = binstsys)
plt.hist(dataproc12[dataproc12.minimal_energy == 1e3].sys_time_seconds/Ngen_L, alpha = 0.5, label = 'L', bins = binstsys)
plt.xscale("log")
plt.xlabel("sys time per event (s)")
plt.ylabel("n jobs")
plt.title("dataproc12")
plt.legend()
plt.savefig("plots/dataproc12_sys.png")
plt.show()


egrid = [1e4, 1e6, 3e7, 3e8]

r_epos_geisha_L = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_geisha_M = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_geisha_H = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_geisha_UH = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                      & (dataproc10['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_geisha = [r_epos_geisha_L, r_epos_geisha_M, r_epos_geisha_H, r_epos_geisha_UH]

r_syb_geisha_L = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_geisha_M = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_geisha_H = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_geisha_UH = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                     & (dataproc10['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_geisha = [r_syb_geisha_L, r_syb_geisha_M, r_syb_geisha_H, r_syb_geisha_UH]


r_epos_urqmd_L = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_urqmd_M = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_urqmd_H = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_urqmd_UH = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                     & (dataproc10['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_urqmd = [r_epos_urqmd_L, r_epos_urqmd_M, r_epos_urqmd_H, r_epos_urqmd_UH]


r_syb_urqmd_L = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_urqmd_M = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_urqmd_H = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_urqmd_UH = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                    & (dataproc10['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_urqmd = [r_syb_urqmd_L, r_syb_urqmd_M, r_syb_urqmd_H, r_syb_urqmd_UH]

plt.scatter(egrid, r_epos_geisha, color = 'r', label = 'EPOS + GEISHA')
plt.scatter(egrid, r_epos_urqmd, color = 'b', label = 'EPOS + URQMD')
plt.scatter(egrid, r_syb_geisha, color = 'g', label = 'Sybill + GEISHA')
plt.scatter(egrid, r_syb_urqmd, color = 'orange', label = 'Sybill + URQMD')

plt.legend()
plt.xlim(1e3, 1e9)
plt.ylim(1e-2, 1e4)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("primary energy [GeV]")
plt.ylabel("real time per event [s]")
plt.title("dataproc10")
plt.savefig("plots/dataproc10_real_him.png")
plt.show()


r_epos_geisha_L = np.mean(dataproc09[(dataproc09['container_version'] == 72310) 
                                     & (dataproc09['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_geisha_M = np.mean(dataproc09[(dataproc09['container_version'] == 72310) 
                                     & (dataproc09['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_geisha_H = np.mean(dataproc09[(dataproc09['container_version'] == 72310) 
                                     & (dataproc09['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_geisha_UH = np.mean(dataproc09[(dataproc09['container_version'] == 72310) 
                                      & (dataproc09['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_geisha = [r_epos_geisha_L, r_epos_geisha_M, r_epos_geisha_H, r_epos_geisha_UH]

r_syb_geisha_L = np.mean(dataproc09[(dataproc09['container_version'] == 76310) 
                                    & (dataproc09['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_geisha_M = np.mean(dataproc09[(dataproc09['container_version'] == 76310) 
                                    & (dataproc09['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_geisha_H = np.mean(dataproc09[(dataproc09['container_version'] == 76310) 
                                    & (dataproc09['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_geisha_UH = np.mean(dataproc09[(dataproc09['container_version'] == 76310) 
                                     & (dataproc09['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_geisha = [r_syb_geisha_L, r_syb_geisha_M, r_syb_geisha_H, r_syb_geisha_UH]


r_epos_urqmd_L = np.mean(dataproc09[(dataproc09['container_version'] == 72110) 
                                    & (dataproc09['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_urqmd_M = np.mean(dataproc09[(dataproc09['container_version'] == 72110) 
                                    & (dataproc09['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_urqmd_H = np.mean(dataproc09[(dataproc09['container_version'] == 72110) 
                                    & (dataproc09['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_urqmd_UH = np.mean(dataproc09[(dataproc09['container_version'] == 72110) 
                                     & (dataproc09['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_urqmd = [r_epos_urqmd_L, r_epos_urqmd_M, r_epos_urqmd_H, r_epos_urqmd_UH]


r_syb_urqmd_L = np.mean(dataproc09[(dataproc09['container_version'] == 76110) 
                                   & (dataproc09['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_urqmd_M = np.mean(dataproc09[(dataproc09['container_version'] == 76110) 
                                   & (dataproc09['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_urqmd_H = np.mean(dataproc09[(dataproc09['container_version'] == 76110) 
                                   & (dataproc09['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_urqmd_UH = np.mean(dataproc09[(dataproc09['container_version'] == 76110) 
                                    & (dataproc09['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_urqmd = [r_syb_urqmd_L, r_syb_urqmd_M, r_syb_urqmd_H, r_syb_urqmd_UH]

plt.scatter(egrid, r_epos_geisha, color = 'r', label = 'EPOS + GEISHA')
plt.scatter(egrid, r_epos_urqmd, color = 'b', label = 'EPOS + URQMD')
plt.scatter(egrid, r_syb_geisha, color = 'g', label = 'Sybill + GEISHA')
plt.scatter(egrid, r_syb_urqmd, color = 'orange', label = 'Sybill + URQMD')

print(egrid)
print(r_epos_geisha)

plt.legend()
plt.xlim(1e3, 1e9)
plt.ylim(1e-2, 1e4)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("primary energy [GeV]")
plt.ylabel("real time per event [s]")
plt.title("dataproc09")
plt.savefig("plots/dataproc09_real_him.png")
plt.show()



r_epos_geisha_L = np.mean(dataproc11[(dataproc11['container_version'] == 72310) 
                                     & (dataproc11['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_geisha_M = np.mean(dataproc11[(dataproc11['container_version'] == 72310) 
                                     & (dataproc11['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_geisha_H = np.mean(dataproc11[(dataproc11['container_version'] == 72310) 
                                     & (dataproc11['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_geisha_UH = np.mean(dataproc11[(dataproc11['container_version'] == 72310) 
                                      & (dataproc11['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_geisha = [r_epos_geisha_L, r_epos_geisha_M, r_epos_geisha_H, r_epos_geisha_UH]

r_syb_geisha_L = np.mean(dataproc11[(dataproc11['container_version'] == 76310) 
                                    & (dataproc11['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_geisha_M = np.mean(dataproc11[(dataproc11['container_version'] == 76310) 
                                    & (dataproc11['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_geisha_H = np.mean(dataproc11[(dataproc11['container_version'] == 76310) 
                                    & (dataproc11['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_geisha_UH = np.mean(dataproc11[(dataproc11['container_version'] == 76310) 
                                     & (dataproc11['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_geisha = [r_syb_geisha_L, r_syb_geisha_M, r_syb_geisha_H, r_syb_geisha_UH]


r_epos_urqmd_L = np.mean(dataproc11[(dataproc11['container_version'] == 72110) 
                                    & (dataproc11['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_urqmd_M = np.mean(dataproc11[(dataproc11['container_version'] == 72110) 
                                    & (dataproc11['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_urqmd_H = np.mean(dataproc11[(dataproc11['container_version'] == 72110) 
                                    & (dataproc11['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_urqmd_UH = np.mean(dataproc11[(dataproc11['container_version'] == 72110) 
                                     & (dataproc11['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_urqmd = [r_epos_urqmd_L, r_epos_urqmd_M, r_epos_urqmd_H, r_epos_urqmd_UH]


r_syb_urqmd_L = np.mean(dataproc11[(dataproc11['container_version'] == 76110) 
                                   & (dataproc11['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_urqmd_M = np.mean(dataproc11[(dataproc11['container_version'] == 76110) 
                                   & (dataproc11['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_urqmd_H = np.mean(dataproc11[(dataproc11['container_version'] == 76110) 
                                   & (dataproc11['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_urqmd_UH = np.mean(dataproc11[(dataproc11['container_version'] == 76110) 
                                    & (dataproc11['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_urqmd = [r_syb_urqmd_L, r_syb_urqmd_M, r_syb_urqmd_H, r_syb_urqmd_UH]

plt.scatter(egrid, r_epos_geisha, color = 'r', label = 'EPOS + GEISHA')
plt.scatter(egrid, r_epos_urqmd, color = 'b', label = 'EPOS + URQMD')
plt.scatter(egrid, r_syb_geisha, color = 'g', label = 'Sybill + GEISHA')
plt.scatter(egrid, r_syb_urqmd, color = 'orange', label = 'Sybill + URQMD')

plt.legend()
plt.xlim(1e3, 1e9)
plt.ylim(1e-2, 1e4)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("primary energy [GeV]")
plt.ylabel("real time per event [s]")
plt.title("dataproc11")
plt.savefig("plots/dataproc11_real_him.png")
plt.show()



r_epos_geisha_L = np.mean(dataproc12[(dataproc12['container_version'] == 72310) 
                                     & (dataproc12['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_geisha_M = np.mean(dataproc12[(dataproc12['container_version'] == 72310) 
                                     & (dataproc12['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_geisha_H = np.mean(dataproc12[(dataproc12['container_version'] == 72310) 
                                     & (dataproc12['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_geisha_UH = np.mean(dataproc12[(dataproc12['container_version'] == 72310) 
                                      & (dataproc12['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_geisha = [r_epos_geisha_L, r_epos_geisha_M, r_epos_geisha_H, r_epos_geisha_UH]

r_syb_geisha_L = np.mean(dataproc12[(dataproc12['container_version'] == 76310) 
                                    & (dataproc12['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_geisha_M = np.mean(dataproc12[(dataproc12['container_version'] == 76310) 
                                    & (dataproc12['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_geisha_H = np.mean(dataproc12[(dataproc12['container_version'] == 76310) 
                                    & (dataproc12['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_geisha_UH = np.mean(dataproc12[(dataproc12['container_version'] == 76310) 
                                     & (dataproc12['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_geisha = [r_syb_geisha_L, r_syb_geisha_M, r_syb_geisha_H, r_syb_geisha_UH]


r_epos_urqmd_L = np.mean(dataproc12[(dataproc12['container_version'] == 72110) 
                                    & (dataproc12['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_epos_urqmd_M = np.mean(dataproc12[(dataproc12['container_version'] == 72110) 
                                    & (dataproc12['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_epos_urqmd_H = np.mean(dataproc12[(dataproc12['container_version'] == 72110) 
                                    & (dataproc12['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_epos_urqmd_UH = np.mean(dataproc12[(dataproc12['container_version'] == 72110) 
                                     & (dataproc12['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_epos_urqmd = [r_epos_urqmd_L, r_epos_urqmd_M, r_epos_urqmd_H, r_epos_urqmd_UH]


r_syb_urqmd_L = np.mean(dataproc12[(dataproc12['container_version'] == 76110) 
                                   & (dataproc12['minimal_energy'] == 1e3)].real_time_seconds/Ngen_L)
r_syb_urqmd_M = np.mean(dataproc12[(dataproc12['container_version'] == 76110) 
                                   & (dataproc12['minimal_energy'] == 1e5)].real_time_seconds/Ngen_M)
r_syb_urqmd_H = np.mean(dataproc12[(dataproc12['container_version'] == 76110) 
                                   & (dataproc12['minimal_energy'] == 1e7)].real_time_seconds/Ngen_H)
r_syb_urqmd_UH = np.mean(dataproc12[(dataproc12['container_version'] == 76110) 
                                    & (dataproc12['minimal_energy'] == 1e8)].real_time_seconds/Ngen_UH)

r_syb_urqmd = [r_syb_urqmd_L, r_syb_urqmd_M, r_syb_urqmd_H, r_syb_urqmd_UH]

plt.scatter(egrid, r_epos_geisha, color = 'r', label = 'EPOS + GEISHA')
plt.scatter(egrid, r_epos_urqmd, color = 'b', label = 'EPOS + URQMD')
plt.scatter(egrid, r_syb_geisha, color = 'g', label = 'Sybill + GEISHA')
plt.scatter(egrid, r_syb_urqmd, color = 'orange', label = 'Sybill + URQMD')

plt.legend()
plt.xlim(1e3, 1e9)
plt.ylim(1e-2, 1e4)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("primary energy [GeV]")
plt.ylabel("real time per event [s]")
plt.title("dataproc12")
plt.savefig("plots/dataproc12_real_him.png")
plt.show()


u_epos_geisha_L = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e3)].user_time_seconds/Ngen_L)
u_epos_geisha_M = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e5)].user_time_seconds/Ngen_M)
u_epos_geisha_H = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e7)].user_time_seconds/Ngen_H)
u_epos_geisha_UH = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                      & (dataproc10['minimal_energy'] == 1e8)].user_time_seconds/Ngen_UH)

u_epos_geisha = [u_epos_geisha_L, u_epos_geisha_M, u_epos_geisha_H, u_epos_geisha_UH]

u_syb_geisha_L = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e3)].user_time_seconds/Ngen_L)
u_syb_geisha_M = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e5)].user_time_seconds/Ngen_M)
u_syb_geisha_H = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e7)].user_time_seconds/Ngen_H)
u_syb_geisha_UH = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                     & (dataproc10['minimal_energy'] == 1e8)].user_time_seconds/Ngen_UH)

u_syb_geisha = [u_syb_geisha_L, u_syb_geisha_M, u_syb_geisha_H, u_syb_geisha_UH]


u_epos_urqmd_L = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e3)].user_time_seconds/Ngen_L)
u_epos_urqmd_M = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e5)].user_time_seconds/Ngen_M)
u_epos_urqmd_H = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e7)].user_time_seconds/Ngen_H)
u_epos_urqmd_UH = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                     & (dataproc10['minimal_energy'] == 1e8)].user_time_seconds/Ngen_UH)

u_epos_urqmd = [u_epos_urqmd_L, u_epos_urqmd_M, u_epos_urqmd_H, u_epos_urqmd_UH]


u_syb_urqmd_L = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e3)].user_time_seconds/Ngen_L)
u_syb_urqmd_M = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e5)].user_time_seconds/Ngen_M)
u_syb_urqmd_H = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e7)].user_time_seconds/Ngen_H)
u_syb_urqmd_UH = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                    & (dataproc10['minimal_energy'] == 1e8)].user_time_seconds/Ngen_UH)

u_syb_urqmd = [u_syb_urqmd_L, u_syb_urqmd_M, u_syb_urqmd_H, u_syb_urqmd_UH]

plt.scatter(egrid, u_epos_geisha, color = 'r', label = 'EPOS + GEISHA')
plt.scatter(egrid, u_epos_urqmd, color = 'b', label = 'EPOS + URQMD')
plt.scatter(egrid, u_syb_geisha, color = 'g', label = 'Sybill + GEISHA')
plt.scatter(egrid, u_syb_urqmd, color = 'orange', label = 'Sybill + URQMD')

plt.legend()
plt.xlim(1e3, 1e9)
plt.ylim(1e-2, 1e4)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("primary energy [GeV]")
plt.ylabel("user time per event [s]")
plt.title("dataproc10")
plt.savefig("plots/dataproc10_user_him.png")
plt.show()


s_epos_geisha_L = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e3)].sys_time_seconds/Ngen_L)
s_epos_geisha_M = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e5)].sys_time_seconds/Ngen_M)
s_epos_geisha_H = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                     & (dataproc10['minimal_energy'] == 1e7)].sys_time_seconds/Ngen_H)
s_epos_geisha_UH = np.mean(dataproc10[(dataproc10['container_version'] == 72310) 
                                      & (dataproc10['minimal_energy'] == 1e8)].sys_time_seconds/Ngen_UH)

s_epos_geisha = [s_epos_geisha_L, s_epos_geisha_M, s_epos_geisha_H, s_epos_geisha_UH]

s_syb_geisha_L = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e3)].sys_time_seconds/Ngen_L)
s_syb_geisha_M = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e5)].sys_time_seconds/Ngen_M)
s_syb_geisha_H = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                    & (dataproc10['minimal_energy'] == 1e7)].sys_time_seconds/Ngen_H)
s_syb_geisha_UH = np.mean(dataproc10[(dataproc10['container_version'] == 76310) 
                                     & (dataproc10['minimal_energy'] == 1e8)].sys_time_seconds/Ngen_UH)

s_syb_geisha = [s_syb_geisha_L, s_syb_geisha_M, s_syb_geisha_H, s_syb_geisha_UH]


s_epos_urqmd_L = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e3)].sys_time_seconds/Ngen_L)
s_epos_urqmd_M = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e5)].sys_time_seconds/Ngen_M)
s_epos_urqmd_H = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                    & (dataproc10['minimal_energy'] == 1e7)].sys_time_seconds/Ngen_H)
s_epos_urqmd_UH = np.mean(dataproc10[(dataproc10['container_version'] == 72110) 
                                     & (dataproc10['minimal_energy'] == 1e8)].sys_time_seconds/Ngen_UH)

s_epos_urqmd = [s_epos_urqmd_L, s_epos_urqmd_M, s_epos_urqmd_H, s_epos_urqmd_UH]


s_syb_urqmd_L = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e3)].sys_time_seconds/Ngen_L)
s_syb_urqmd_M = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e5)].sys_time_seconds/Ngen_M)
s_syb_urqmd_H = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                   & (dataproc10['minimal_energy'] == 1e7)].sys_time_seconds/Ngen_H)
s_syb_urqmd_UH = np.mean(dataproc10[(dataproc10['container_version'] == 76110) 
                                    & (dataproc10['minimal_energy'] == 1e8)].sys_time_seconds/Ngen_UH)

s_syb_urqmd = [s_syb_urqmd_L, s_syb_urqmd_M, s_syb_urqmd_H, s_syb_urqmd_UH]

plt.scatter(egrid, s_epos_geisha, color = 'r', label = 'EPOS + GEISHA')
plt.scatter(egrid, s_epos_urqmd, color = 'b', label = 'EPOS + URQMD')
plt.scatter(egrid, s_syb_geisha, color = 'g', label = 'Sybill + GEISHA')
plt.scatter(egrid, s_syb_urqmd, color = 'orange', label = 'Sybill + URQMD')

plt.legend()
plt.xlim(1e3, 1e9)
plt.ylim(1e-5, 1e2)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("primary energy [GeV]")
plt.ylabel("sys time per event [s]")
plt.title("dataproc10")
plt.savefig("plots/dataproc10_sys_him.png")
plt.show()








