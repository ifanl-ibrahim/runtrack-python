def draw_rectangle(width, height):
    print("+{}+".format("-" * (width-2)))
    
    for i in range(height-2):
        print("|{}|".format(" " * (width-2)))
        
    print("+{}+".format("-" * (width-2)))

draw_rectangle(10, 3)