Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forwarg(100)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tao.forwarg(100)
AttributeError: 'Turtle' object has no attribute 'forwarg'
>>> tao.forword(100)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tao.forword(100)
AttributeError: 'Turtle' object has no attribute 'forword'
>>> tao.foeward(100)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tao.foeward(100)
AttributeError: 'Turtle' object has no attribute 'foeward'
>>> tao.forward(90)
>>> tao.right(90)
>>> tao.left(180)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(90)
>>> tao.reset()
>>> for i in range(4) :
	tao.forward(100)
	tao.left(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5);
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> for i in range(8) :
	tao.forward(100)
	tao.left(45)

	
>>> tao.reset()
>>> >>> for i in range(8) :
	tao.forward(100)
	tao.left(45)
	
SyntaxError: invalid syntax
>>> for i in range(8) :
	tao.forward(100)
	tao.left(45)

	
>>> for i in range(8) :
	tao.forward(100)
	tao.left(45)

	
>>> for i in range(4);
SyntaxError: invalid syntax
>>> for i in ranga(4):
	for i in range(8);
	
SyntaxError: invalid syntax
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(90)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> 
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(180)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> 
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(135)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x0000000002D0E8B0>>
>>> tao.reset()
>>> for i in range(10):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(36)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
8 เหลี่ยมรูปที่ 4
8 เหลี่ยมรูปที่ 5
8 เหลี่ยมรูปที่ 6
8 เหลี่ยมรูปที่ 7
8 เหลี่ยมรูปที่ 8
8 เหลี่ยมรูปที่ 9
>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> regtangle
<function regtangle at 0x00000000030BE9D0>
>>> regtangle()
>>> for i in range(10)
SyntaxError: invalid syntax
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
>>> 