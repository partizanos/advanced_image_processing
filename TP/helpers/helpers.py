def showImgs(images, title, colormap):
    fig, ax = plt.subplots(
        ncols=4,
        sharex=True,
        sharey=True,
        figsize=(18, 14)
    )

    for index, im in enumerate(images):
        ax[index].imshow(im.data, colormap)
        ax[index].set_title(im.name + title)