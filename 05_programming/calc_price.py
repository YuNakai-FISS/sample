# [A]: 「税抜価格」をユーザーから取得し、数値に変換する
tax_excluded_price = int(input("税抜価格を入力してください: "))

# [B]: 「税込価格」を計算する（消費税率は10%）
tax_rate = 0.10
tax_included_price = tax_excluded_price * (1 + tax_rate)

# [C]、[D]: 送料の計算（2000円以上かどうかを判定して分岐する）
if (tax_included_price >= 2000):
    shipping_cost = 0
    print("送料は無料です")
else:
    shipping_cost = 350
    print(f"送料は{shipping_cost}円です")

# [E]: 送料込税込価格を計算して、変数に代入する
total_price = tax_included_price + shipping_cost

# 「送料込税込価格」を少数を含めずに出力する
print(f"送料込税込価格は{total_price:.0f}円です")