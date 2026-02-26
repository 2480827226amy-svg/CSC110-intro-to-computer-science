# ------------------------------------------------------
#        Name: Amy Tang
#       Peers: NA
#  References: https://www.youtube.com/watch?v=DqhzxdkdQS0&list=PLAEQD0ULngi6bAFRfcqgpKP4T4SnoxoAz
# ------------------------------------------------------
from graphics import *
import random
#######################################################################
WIDTH = 1400
HEIGHT = 800


def clouds(win, x:float, y:float) -> list:
  """ This function takes in the window that the output will be on and the x,y position for the clouds so that multiple clouds can be produced.
  :param win: the window that the cloud will be shown on
  :param x:(float) The set x-coordinate for the cloud.
  :param y:(float) The set y-coordinate for the cloud.
  :return:(str) A list of graphical objects representing the cloud.
  """
  cloud_parts = []
  cloud_1_shade = Oval(Point(x+40, y+80), Point(x+180, y+170)) # the shade of the cloud 1 needs to be drawn first
  cloud_1_shade.setFill(color_rgb(198,195,190))
  cloud_1_shade.setOutline(color_rgb(198,195,190))
  cloud_parts.append(cloud_1_shade) # make a list of clouds to make the movement easier. 

  cloud_2_shade = Oval(Point(x+110, y+60), Point(x+250, y+150)) 
  cloud_2_shade.setFill(color_rgb(198,195,190)) 
  cloud_2_shade.setOutline(color_rgb(198,195,190))
  cloud_parts.append(cloud_2_shade)

  cloud_1_shade.draw(win) 
  cloud_2_shade.draw(win) # the cloud is composed of two ovals, and we have to draw the two shade ovals first so it's on the back

  cloud_1 = Oval(Point(x+50, y+60), Point(x+180, y+150)) 
  cloud_1.setFill("white")
  cloud_1.setOutline("white")
  cloud_parts.append(cloud_1)

  cloud_2 = Oval(Point(x+120, y+40), Point(x+260, y+130))
  cloud_2.setFill("white")
  cloud_2.setOutline("white")
  cloud_parts.append(cloud_2)

  cloud_1.draw(win)
  cloud_2.draw(win)

  return cloud_parts # return the list of cloud objects

def moveClouds(cloud_parts):
  """ It moves all cloud parts vertically. 
  :param cloud_parts: A list of cloud shapes to be moved.
  """
  for i in range(15): 
    for clouds in cloud_parts:
      clouds.move(0,10) # move the cloud parts upward
    for clouds in cloud_parts:
       clouds.move(0,-10) # move the cloudp arts downward

def lake(win):
    """ Draw the dark blue lake
    :param win: the window that the lake is drawn
    """
    lake = Rectangle(Point(0,600), Point(1400,800))
    lake.setFill(color_rgb(82,150,213))
    lake.setOutline(color_rgb(82,150,213))
    lake.draw(win)


def mountains(win):
   """ Draw the mountains
   :param win: the window that the mountain is drawn
   """
   m1_shade = Polygon(Point(200, 150), Point(30,500), Point(150, 600)) # the mountain is composed of the dark grey shade and the white mountain.
   m1_shade.setFill(color_rgb(150,150,150))
   m1_shade.setOutline(color_rgb(150,150,150))
   m1_shade.draw(win)

   m2_shade = Polygon(Point(600, 200), Point(550,600), Point(400, 500))
   m2_shade.setFill(color_rgb(150,150,150))
   m2_shade.setOutline(color_rgb(150,150,150))
   m2_shade.draw(win)

   m1 = Polygon(Point(200, 150), Point(500,600), Point(150, 600))
   m1.setFill("white")
   m1.setOutline("white")
   m1.draw(win)

   m2 = Polygon(Point(600, 200), Point(550,600), Point(900, 600))
   m2.setFill("white")
   m2.setOutline("white")
   m2.draw(win)

def grass(win):
   """Draw the green grass
   :param win: the window that the grass is drawn
   """
   grass1 = Polygon(Point(0, 450), Point(0,650), Point(1000, 600)) # the grass part is composed to two triangles
   grass1.setFill(color_rgb(119,184,86))
   grass1.setOutline(color_rgb(119,184,86))
   grass1.draw(win)

   grass2 = Polygon(Point(1400, 450), Point(1400,650), Point(800, 600))
   grass2.setFill(color_rgb(119,184,86))
   grass2.setOutline(color_rgb(119,184,86))
   grass2.draw(win)

def bigtree(win) -> list:
   """ draw the big tree
   :param win: the window that the big tree is drawn
   :return :(list) A list of graphical objects representing the big tree.
   """
   entireBigTree = []
   tree1 = Polygon(Point(1100, 250), Point(1000,350), Point(1200, 350)) # the big tree is composed of three traingles and a rectangle
   tree1.setFill(color_rgb(49, 113, 65))
   tree1.setOutline(color_rgb(49, 113, 65))
   tree1.draw(win)
   entireBigTree.append(tree1)

   tree2 = Polygon(Point(1100, 300), Point(950,450), Point(1250, 450))
   tree2.setFill(color_rgb(49, 113, 65))
   tree2.setOutline(color_rgb(49, 113, 65))
   tree2.draw(win)
   entireBigTree.append(tree2)

   tree3 = Polygon(Point(1100, 370), Point(900,570), Point(1310, 570))
   tree3.setFill(color_rgb(49, 113, 65))
   tree3.setOutline(color_rgb(49, 113, 65))
   tree3.draw(win)
   entireBigTree.append(tree3) #since the list is for the purpose of moving the tree and I'm only moving the green part of the tree so I only include the tree1-tree3 in the list. 

   tree4 = Rectangle(Point(1070,570),Point(1120,800))
   tree4.setFill(color_rgb(145,104,68))
   tree4.setOutline(color_rgb(145,104,68))
   tree4.draw(win)

   return entireBigTree
  

def smalltree(win) -> list:
   """draw the small tree
   :param win: the window that the small tree is drawn
   :return :(list) A list of graphical objects representing the small tree.
   """
   entireSmallTree = []
   tree11 = Polygon(Point(970, 350), Point(900,430), Point(1040, 430))
   tree11.setFill(color_rgb(60,133,81))
   tree11.setOutline(color_rgb(60,133,81))
   tree11.draw(win)
   entireSmallTree.append(tree11)

   tree21 = Polygon(Point(970, 400), Point(850,500), Point(1090, 500))
   tree21.setFill(color_rgb(60,133,81))
   tree21.setOutline(color_rgb(60,133,81))
   tree21.draw(win)
   entireSmallTree.append(tree21)

   tree31 = Polygon(Point(970, 470), Point(800,600), Point(1150, 600))
   tree31.setFill(color_rgb(60,133,81))
   tree31.setOutline(color_rgb(60,133,81))
   tree31.draw(win)
   entireSmallTree.append(tree31)


   tree41 = Rectangle(Point(950,600),Point(990,800))
   tree41.setFill(color_rgb(145,110,57))
   tree41.setOutline(color_rgb(145,110,57))
   tree41.draw(win)

   return entireSmallTree

def moveTrees(entireSmallTree,entireBigTree):
   """ Moves the small tree left to right and big tree left to right.
   :param entireSmallTree: List of graphical objects that's in the small tree
   :param entireBigTree: List of graphical objects that's in the big tree
   """
   for i in range (30):
      for trees in entireSmallTree: #iterates each item in the small tree, including three triangles. 
         trees.move(2,0)
      for trees in entireBigTree:
         trees.move(-2,0)
      for trees in entireSmallTree:
         trees.move(-2,0)
      for trees in entireBigTree:
         trees.move(2,0)
   

def main() -> None:
  """ Draws the entire graph.
  """
  win = GraphWin("Mountain waterfall", WIDTH, HEIGHT)
  win.setBackground(color_rgb(147,202,234))

  cloud1 = clouds(win,30,5)
  cloud2 = clouds(win,300,65)
  cloud3 = clouds(win,700,15)
  cloud4 = clouds(win,1100,30)
  allclouds = cloud1 + cloud2 + cloud3 + cloud4

  lake(win)

  mountains(win)

  grass(win)

  tree_1 = bigtree(win)
  tree_2 = smalltree(win)

  win.getMouse()
  moveClouds(allclouds)
  moveTrees(tree_1, tree_2)
 

  win.getMouse()
  win.close

if __name__ == "__main__":
    main()