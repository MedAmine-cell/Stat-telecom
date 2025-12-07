
import random

first_names=["James","John","Michael","Robert","David","Daniel","Andrew","Chris","Mark","Kevin","Jason","Brian","Eric","Steven","Paul"]
last_names=["Smith","Johnson","Brown","Williams","Jones"]
ops=["Verizon","AT&T","T-Mobile"]

verizon_numbers=[
"(212) 555-0143","(347) 555-0294","(646) 555-8832","(718) 555-6610","(917) 555-4382",
"(201) 555-9022","(206) 555-1129","(323) 555-7641","(310) 555-9921","(415) 555-3318"
]

att_numbers=[
"(305) 555-1988","(404) 555-7740","(512) 555-6641","(713) 555-0027","(214) 555-8374",
"(281) 555-5599","(615) 555-7201","(702) 555-3452","(832) 555-4690","(901) 555-7433"
]

tmobile_numbers=[
"(602) 555-1900","(480) 555-7722","(702) 555-8830","(503) 555-6619","(720) 555-2190",
"(619) 555-4771","(408) 555-9033","(916) 555-7442","(971) 555-3390","(414) 555-6628"
]

users=[]
v_i=0
a_i=0
t_i=0

for op in ops:
    i=0
    while i<10:
        fn=random.choice(first_names)
        ln=random.choice(last_names)
        n=fn+" "+ln
        y=random.randint(2018,2025)

        if op=="Verizon":
            num=verizon_numbers[v_i]
            v_i+=1
        elif op=="AT&T":
            num=att_numbers[a_i]
            a_i+=1
        else:
            num=tmobile_numbers[t_i]
            t_i+=1

        users.append({"name":n,"operator":op,"year":y,"number":num})
        i=i+1


print("\nUSA Phone Users")
print("1) Verizon")
print("2) AT&T")
print("3) T-Mobile")
print("4) All")

c=input("Pick (1-4): ")

if c=="1":
    t="Verizon Users"
    show=[]
    for u in users:
        if u["operator"]=="Verizon":
            show.append(u)
elif c=="2":
    t="AT&T Users"
    show=[]
    for u in users:
        if u["operator"]=="AT&T":
            show.append(u)
elif c=="3":
    t="T-Mobile Users"
    show=[]
    for u in users:
        if u["operator"]=="T-Mobile":
            show.append(u)
else:
    t="All Users"
    show=users


print("\n===============================")
print("    "+t)
print("===============================")
print(f"{'Name':<22} {'Operator':<10} {'Year':<6} {'Phone'}")
print("-------------------------------")
for u in show:
    print(f"{u['name']:<22} {u['operator']:<10} {u['year']:<6} {u['number']}")
print("-------------------------------")