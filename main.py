def tiangle_middle(a):
    x=0
    y=0
    for hold in a:
        x = hold[0] + x
        y = hold[1] + y
    return [x/len(a),y/len(a)] 

def distance(a,b):
    return ((a[0]-b[0])*(a[0]-b[0]))+((a[1]-b[1])*(a[1]-b[1]))

def unique(a):
    tab=[]
    for x in a:
        if x not in tab:
            tab.append(x)
    return tab
points = []
with open('dane.txt','r') as file:
    file = file.read()
    points = file.split('\n')
control = 0 # --------------
field_number = int(points[0])   # number of fields
for tri_field in range(field_number): 
    print('field number',tri_field+1)
    control = control+1
    triangle_number = int(points[control])
    if int(points[control])%3 != 0:
        print('wrong number of pols in',tri_field+1,'field')
        break
    poles_fields=[]
    for post_number in range(int(triangle_number)):
        control=control+1
        tab=[]
        for x in points[control].split():
            tab.append(int(x))
        poles_fields.append(tab)
    tab=[]
    tab1=[]
    tab2=[]
    for x in poles_fields:
        tab.append(distance(x,tiangle_middle(poles_fields)))
    for sorted_tab_value in sorted(unique(tab))[::-1]:
        for index in range(triangle_number):
            if sorted_tab_value==tab[index]:
                tab1.append(index+1)
    for x in range(len(tab1))[::3]:
        hold =[]
        for y in range(3):
            hold.append(tab1[x+y])
        
        print(x/3+1,hold)