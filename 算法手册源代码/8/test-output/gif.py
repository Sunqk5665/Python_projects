import imageio,os
images = []
images.append(imageio.imread('8.jpg'))
filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('gif.gif', images,duration=1,loop=1)
