class Point:
  def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

class Rectangle:
  def __init__(self):
      self.lt = Point()  # left-top point
      self.rb = Point()  # right-bottom point

  def setPoints(self, x1, y1, x2, y2):
      self.lt.x = x1
      self.lt.y = y1
      self.rb.x = x2
      self.rb.y = y2

  def show(self):
      print(f"좌측 상단 꼭지점이 ({self.lt.x}, {self.lt.y})이고 우측 하단 꼭지점이 ({self.rb.x}, {self.rb.y})인 사각형입니다.")

  def getWidth(self):
      return self.rb.x - self.lt.x

  def getHeight(self):
      return self.rb.y - self.lt.y

  def getArea(self):
      return self.getWidth() * self.getHeight()

  def getPerimeter(self):
      return 2 * (self.getWidth() + self.getHeight())

# 주 프로그램부
r1 = Rectangle()
r1.setPoints(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
