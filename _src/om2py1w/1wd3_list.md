# Date Structures List

- list method
- 用于
	- 进出`客栈` 
	- `排队` 结合 `collenctions`模块的`deque`
	- `函数工具` `filter(function, seque)`, `map(function, seque)`, `reduce(function, seque)`
- 更多理解
	- 直接用list 简化 一个循环赋值
		- `squares = [x**2 for x in range(10)]`
	- 嵌套 注意主次 加()
		- 矩阵表示 提取
		- zip()
- PS `lambda` expression 相当于 一个函数

> the expression lambda arguments: expression yields a function object. 

	lambda_expr     ::=  "lambda" [parameter_list]: expression

	def name(arguments):
    	return expression

[代码1wd3](https://github.com/JeremiahZhang/OMOOC2py/tree/master/_src/om2py1w/1wd3)