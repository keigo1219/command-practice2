import calc_bmi

print("bimを計算します。")
sin = int(input("身長："))
tai = int(input("体重："))
result = calc_bmi.bmi(sin, tai)
print(result)
