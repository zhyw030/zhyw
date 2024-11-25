import sqlite3
import datetime
import random

# 数据库连接
conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()

# 创建商品表
cursor.execute('''
CREATE TABLE IF NOT EXISTS goods (
    barcodes INTEGER PRIMARY KEY,
    goodsname TEXT NOT NULL,
    goodsnumber INTEGER NOT NULL,
    singleprices REAL NOT NULL,
    goodssumprice REAL NOT NULL
)
''')
conn.commit()

# 商品信息：条码 -> {"name": 品名, "price": 单价, "quantity": 库存}
goods_dict = {}
# 销售统计：条码 -> {"name": 品名, "sales": 销量}
sales_data = {}
# 总销售额
total_sales = 0

# 从数据库加载商品信息
def load_goods():
    global goods_dict, sales_data
    cursor.execute('SELECT barcodes, goodsname, goodsnumber, singleprices FROM goods')
    rows = cursor.fetchall()
    for row in rows:
        bar_code, name, quantity, price = row  # 解包 4 列数据
        goods_dict[bar_code] = {"name": name, "price": price, "quantity": quantity}
        sales_data[bar_code] = {"name": name, "sales": 0}


# 保存商品信息到数据库
def save_goods():
    for bar_code, info in goods_dict.items():
        total_price = info['price'] * info['quantity']
        cursor.execute('''
        INSERT OR REPLACE INTO goods (barcodes, goodsname, goodsnumber, singleprices, goodssumprice) 
        VALUES (?, ?, ?, ?, ?)
        ''', (bar_code, info['name'], info['quantity'], info['price'], total_price))
    conn.commit()


# 更新总销售额
def update_total_sales():
    global total_sales
    total_sales = 0
    for bar_code, info in sales_data.items():
        item_sales = info["sales"] * goods_dict[bar_code]["price"]
        total_sales += item_sales

# 保存销售统计信息
def save_statistics():
    global total_sales
    for bar_code, info in sales_data.items():
        cursor.execute('''
        UPDATE goods SET goodsnumber = goodsnumber + ?, goodssumprice = goodssumprice + ?
        ''', (info["sales"], info["sales"] * goods_dict[bar_code]["price"]))
    conn.commit()
    cursor.execute('UPDATE goods SET goodsnumber = 0, goodssumprice = 0 WHERE barcodes = ?', (bar_code,))
    conn.commit()

# 增加商品
def add_goods():
    while True:
        bar_code = input("请输入商品条码号 (按回车退出): ")
        if bar_code == "":
            break

        # 检查商品是否在数据库中存在
        cursor.execute('SELECT goodsname, goodsnumber, singleprices FROM goods WHERE barcodes = ?', (bar_code,))
        result = cursor.fetchone()

        if result:  # 商品已存在
            name, quantity, price = result
            new_quantity = quantity + 1
            goods_dict[bar_code] = {"name": name, "price": price, "quantity": new_quantity}

            # 更新数据库中的库存和总价
            cursor.execute('''
                UPDATE goods
                SET goodsnumber = ?, goodssumprice = ?
                WHERE barcodes = ?
            ''', (new_quantity, new_quantity * price, bar_code))
            conn.commit()

            print(f"商品 {name} 已存在，库存+1，当前库存为 {new_quantity}。\n")
        else:  # 商品不存在，需录入完整信息
            name = input("请输入商品名称: ")
            while True:
                try:
                    price = float(input("请输入商品单价: "))
                    break
                except ValueError:
                    print("无效价格，请重新输入。\n")

            while True:
                try:
                    quantity = int(input("请输入商品数量: "))
                    if quantity < 0:
                        print("库存数量不能为负数，请重新输入。")
                        continue
                    break
                except ValueError:
                    print("无效输入，请输入整数。\n")

            goods_dict[bar_code] = {"name": name, "price": price, "quantity": quantity}

            # 插入新商品到数据库
            cursor.execute('''
                INSERT INTO goods (barcodes, goodsname, goodsnumber, singleprices, goodssumprice) 
                VALUES (?, ?, ?, ?, ?)
            ''', (bar_code, name, quantity, price, price * quantity))
            conn.commit()

            print(f"新商品 {name} 已添加！当前库存为 {quantity}。\n")



    # 询问是否接着进入收银模块
    checkout_choice = input("是否立即进行收银？(y/n): ").strip().lower()
    if checkout_choice == 'y':
        checkout()
    elif checkout_choice == 'n':
        print("返回主菜单。\n")
    else:
        print("无效输入，请选择 'y' 或 'n'。\n")

            

# 删除商品
def delete_goods():
    bar_code = input("请输入要删除的商品条码号: ")
    if bar_code in goods_dict:
        del goods_dict[bar_code]
        del sales_data[bar_code]
        cursor.execute('DELETE FROM goods WHERE barcodes = ?', (bar_code,))
        conn.commit()
        print("商品已删除！\n")
    else:
        print("未找到该商品。\n")

# 修改商品
def update_goods():
    bar_code = input("请输入商品条码号: ")
    if bar_code in goods_dict:
        print(f"当前商品信息：{goods_dict[bar_code]}")
        name = input("新的商品名称 (回车跳过): ") or goods_dict[bar_code]["name"]
        price = input("新的单价 (回车跳过): ")
        price = float(price) if price else goods_dict[bar_code]["price"]
        quantity = input("新的库存数量 (回车跳过): ")
        quantity = int(quantity) if quantity else goods_dict[bar_code]["quantity"]
        goods_dict[bar_code] = {"name": name, "price": price, "quantity": quantity}
        cursor.execute('''
        UPDATE goods SET goodsname = ?, goodsnumber = ?, singleprices = ?, goodssumprice = ?
        ''', (name, quantity, price, price * quantity))
        conn.commit()
        print("商品信息已更新！\n")
    else:
        print("未找到该商品。\n")


# 查询商品
def query_goods():
    bar_code = input("请输入商品条码号: ")
    if bar_code in goods_dict:
        info = goods_dict[bar_code]
        print(f"商品信息：\n条码号:{bar_code}\n名称:{info['name']}\n单价:{info['price']}\n库存:{info['quantity']}\n")
    else:
        print("未找到该商品。\n")

# 显示统计信息
def statistics():
    if total_sales == 0:
        print("\n\n尚无任何销售记录，请先进行收银。")
    else:
        print(f"交易总销售额：{total_sales:.2f}元")
    
    # 查询热销商品前三
    cursor.execute('''
        SELECT barcodes, goodsname, goodsnumber 
        FROM goods 
        ORDER BY goodsnumber DESC 
        LIMIT 3
    ''')
    hot_sales = cursor.fetchall()
    print("热销商品前三：")
    for bar_code, name, quantity in hot_sales:
        print(f"{bar_code}. {name} - 销量：{quantity}")
    
    # 排除热销商品的条码
    hot_sales_barcodes = [str(item[0]) for item in hot_sales]  # 获取条码列表
    placeholders = ', '.join('?' for _ in hot_sales_barcodes)  # 构造占位符
    query = f'''
        SELECT barcodes, goodsname, goodsnumber 
        FROM goods 
        WHERE barcodes NOT IN ({placeholders})
    '''
    cursor.execute(query, hot_sales_barcodes)
    other_rows = cursor.fetchall()

    # 显示“其他商品销量”
    print("\n其他商品销量：")
    if not other_rows:
        print("无其他商品记录。")
    else:
        for bar_code, name, quantity in other_rows:
            print(f"{bar_code}. {name} - 销量：{quantity}")

# 打印小票
def print_receipt(items, pricesinglelist, itemnumbers, pricelist, sumup, sumnum):
    ticket = random.randint(211111111111111111, 299999999999999999)
    frontdesk = random.randint(1, 99)
    casher = random.randint(1000000000, 9999999999)

    print("\n-------------------------------------------")
    print("青青草原超市（欢迎光临）")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(f"票单：{ticket}")
    print(f"款台: {frontdesk}  收银员: {casher}")
    print("-------------------------------------------")
    print(f"{'商品名':<9} {'单价':<9} {'数量':<8} {'总价':<8}")
    for i in range(len(items)):
        print(f"{items[i]:<12} {pricesinglelist[i]:<11.2f} {itemnumbers[i]:<10} {pricelist[i]:<8.2f}")
    print(f"\n金额小计：{sumup:.2f}")
    print(f"数量小计：{sumnum}")
    print("\n\n谢谢惠顾！期待你的下次光临！")
    print("-------------------------------------------")
    

# 收银
def checkout():
    global total_sales

    # 查询数据库，获取所有销售数据（库存大于 0 的商品）
    cursor.execute("SELECT barcodes, goodsname, singleprices, goodsnumber FROM goods WHERE goodsnumber > 0")
    rows = cursor.fetchall()

    if not rows:
        print("\n没有销售记录或库存不足，无法生成小票。\n")
        return

    # 准备小票数据
    items = []
    pricesinglelist = []
    itemnumbers = []
    pricelist = []

    # 总金额和数量初始化
    sumup = 0
    sumnum = 0

    for row in rows:
        bar_code, name, unit_price, quantity = row
        total_price = unit_price * quantity
        items.append(name)
        pricesinglelist.append(unit_price)
        itemnumbers.append(quantity)
        pricelist.append(total_price)

        # 累计总金额和总数量
        sumup += total_price
        sumnum += quantity

    # 打印小票
    print_receipt(items, pricesinglelist, itemnumbers, pricelist, sumup, sumnum)
    total_sales += sumup


    # 确认付款
    while True:
        cod = input("请出示付款码 (18位，前两位为10-15): ")
        if len(cod) == 18 and cod[:2] in {"10", "11", "12", "13", "14", "15"}:
            print("付款成功！交易完成。\n")
            break
        elif cod == "":
            print("未输入付款码，交易取消。\n")
            return
        else:
            print("不是有效付款码，请重试。\n")



# 清除所有商品数量
def clear_stock():
    cursor.execute("UPDATE goods SET goodsnumber = 0")
    conn.commit()
    for bar_code in goods_dict:
        goods_dict[bar_code]["quantity"] = 0
    print("所有商品的数量已清零，但保留了商品的基本信息。\n")


# 清除所有数据库的数据
def clear_all_data():
    cursor.execute('DELETE FROM goods')  # 删除所有商品数据
    conn.commit()
    print("是否确认清除所有商品数据？(y/n): ")
    choice = input().strip().lower()
    if choice == 'y':
        cursor.execute('DELETE FROM goods')  # 删除所有商品数据
        conn.commit()
        print("所有商品数据已清除。\n")
    else:
        print("取消清除。\n")


# 主菜单
def main():
    load_goods()
    while True:
        print("\n\n")
        print("1. 增加商品")
        print("2. 删除商品")
        print("3. 修改商品")
        print("4. 查询商品")
        print("5. 统计信息")
        print("6. 收银")
        print("7. 清除所有商品库存")
        print("8. 清除所有数据库数据")
        print("9. 退出系统")

        choice = input("请输入选择：")
        if choice == "1":
            add_goods()
        elif choice == "2":
            delete_goods()
        elif choice == "3":
            update_goods()
        elif choice == "4":
            query_goods()
        elif choice == "5":
            statistics()
        elif choice == "6":
            checkout()
        elif choice == "7":
            clear_stock()  
        elif choice == "8":
            clear_all_data()  
        elif choice == "9":
            print("感谢使用，系统已退出。")
            break
        else:
            print("无效输入，请重新选择。\n")

if __name__ == "__main__":
    main()

#防止程序自己退出
input("\n")