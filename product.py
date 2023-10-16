class Product:
    def __init__(self,productid,productname,unitprice, totalquantity):
        self.productid = productid              # 序号
        self.productname = productname          # 品名
        self.unitprice = unitprice              # 单价
        self.totalquantity = totalquantity      # 总量
        self.remainingquantity = totalquantity  # 余量

    # 显示商品信息
    def display(self):
        print("商品序号:", self.productid)
        print("商品名:", self.productname)
        print("单价:", self.unitprice)
        print("总数量:", self.totalquantity)
        print("剩余数量:", self.remainingquantity)

    # 计算已售出商品的价值
    def sold(self,soldquantity):
        if soldquantity <= self.remainingquantity:
            value = soldquantity * self.unitprice
            self.remainingquantity -= soldquantity
            return value
        else:
            print("库存不足！")

    # 修改商品信息
    def setdata(self,id,productname,unitprice,totalquantity):
        self.productname = productname
        self.productid = id
        self.unitprice = unitprice
        self.totalquantity = totalquantity
        self.remainingquantity = totalquantity


product1 = Product(101,"手机",500,50)
product1.display()
print("已售出商品价值:", product1.sold(10))
product1.display()
product1.setdata("平板电脑",800,30)
product1.display()
