#all plant name
Asparagus_Fern="Asparagus Fern"
Cactus="Cactus"
Peace_lily="Peace lily"
Spider_plant="Spider plant"
Money_tree="Money Tree"
Phelodendron="Phelodendron"
Dragon_tree="Dragon Tree"
ZZ_Plant="ZZ Tree"
Coffee_Plant="Coffee plant"
Gia="Gia"
Croton="Croton"
Wax_Begonia="Wax Begonia"
Creeping_jenny="Creeping jenny"
Cannas="Cannas"
a=('Asparagus Fern, Cactus, Peace lily, Spider plant, Money tree, Phelodendron, Dragon tree, ZZ Plant, Coffee Plant' )
b=('Gia, Cactus, Croton, Wax begonia, Creeping jenny, Cannas')
print("Welcome to the plant finder")
answer=input("(a) do you want indoor plants (b) do you want outdoor plants?")
if answer == "a":
    print(a)
elif answer=="b":
    print(b)
answer=input('Choose a plant')   
if answer=="Asparagus Fern":
     print("Although it’s neither asparagus nor fern, this plant has been popular for decades. As long as it has plenty of water and light, it’ll thrive as a climbing, trailing or upright plant.")
elif answer=="Cactus":
    print("Cactus can be grown indoors as long as you place them in a spot where they receive at least 4 to 6 hours of daily sunlight.")
elif answer=="Money tree":
    print("its awesome too")
elif answer== "Gia":
    print("Watering once a week should do the trick, though you might need to experiment with the frequency based on humidity in your home. They are toxic to animals")
elif answer=="Croton":
    print("The leathery rainbow-hued leaves thrive in full sun and only require moderate watering.")
elif answer=="Wax Begonia":
    print("Fleshy stem help patio begonias tolerate drought and plants are equally happy in sun or shade, but never put then in direct harsh sunlight.")
elif answer=="Creeping jenny":
    print("The plants like constant moisture and fare better in partial sun than in stronger afternoon sun, which bleach the leaves.")
elif answer=="Cannas":
    print=("Cannas are very hungry and thirsty plants, so keep them very moist and feed them with balanced plant fertilizer to help to reach them their potential.")

