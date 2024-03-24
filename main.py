import cv2

#image_path="MonaLisa.jpg"
image_path="my.jpg"

image=cv2.imread(image_path)
if (image is None):
    print("image does not exist")
else:
    print("image exists!")

#use to resize
new_width=200
new_height=100

#resize the image
resize_image=cv2.resize(image,(new_width,new_height),interpolation=cv2.INTER_AREA)

#use resized image measurements.
#height,width,channel=image.shape
height,width,channel=resize_image.shape

print(f"image width: {width}, image height:{height}")
#width is 640 pixels height is 480 pixels

#prints RGB values at this x and y co-ordinate

pixel_matrix=[[(0,0,0) for _ in range(width)] for _ in range(height)]

#store the pixels in a 2d array
#image.shape[0] is height 
for y in range(resize_image.shape[0]):
    for x in range(resize_image.shape[1]):
        pixel_matrix[y][x]=image[y][x]


#create a brightness matrix
bright_matrix=[[0 for _ in range(width)] for _ in range(height)]

for y in range(height):
    for x in range(width):
        r,g,b=pixel_matrix[y][x]
        avg=sum((r,g,b))
        avg=avg/3
        bright_matrix[y][x]=avg

#brightness values ranging from 0-130

#darkest to brightest
#`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
#ASCII character matrix

char_matrix=[[0 for _ in range(width)] for _ in range(height)]

for y in range(height):
    for x in range(width):
        bright=bright_matrix[y][x]
        
        if bright==0:
            char_matrix[y][x]="`"
        elif bright in range(1,10):
            char_matrix[y][x]="^"
        elif bright in range(11,20):
            char_matrix[y][x]=":"
        elif bright in range(21,30):
            char_matrix[y][x]=";"
        elif bright in range(31,40):
            char_matrix[y][x]="I"
        elif bright in range(41,50):
            char_matrix[y][x]="l"
        elif bright in range(51,60):
            char_matrix[y][x]="!"
        elif bright in range(61,70):
            char_matrix[y][x]="+"
        elif bright in range(71,80):
            char_matrix[y][x]="_"
        elif bright in range(81,90):
            char_matrix[y][x]="-"
        elif bright in range(91,100):
            char_matrix[y][x]="?"
        elif bright in range(101,110):
            char_matrix[y][x]="]"
        elif bright in range(111,120):
            char_matrix[y][x]="["
        elif bright in range(121,130):
            char_matrix[y][x]="}"
        elif bright in range(131,140):
            char_matrix[y][x]="{"
        else:
            char_matrix[y][x]="$"




for y in range(height):
  for x in range(width):
    print(char_matrix[y][x], end="")  # Print without newline
  print()  # Print a newline after each row

cv2.imshow("Loaded Image", resize_image)
#cv2.imshow("Loaded Image", image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()